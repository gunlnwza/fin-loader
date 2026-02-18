from pathlib import Path
import pandas as pd
import logging

from core import ForexSymbol, Timeframe
from provider import DataProvider


class Downloader:
    DATA_DIR = "data"

    def __init__(self, provider: DataProvider):
        self.provider = provider

        self._provider_dir = Path(__file__).parent / Downloader.DATA_DIR / self.provider.name
        self._provider_dir.mkdir(exist_ok=True)

    def _symbol_dir(self, s: ForexSymbol):
        dir = self._provider_dir / str(s)
        dir.mkdir(exist_ok=True)
        return dir

    def _get_filename(self, s: ForexSymbol, tf: Timeframe):
        return f"{self.provider.name}_{s.base}{s.quote}_{tf.length}{tf.unit}.csv"

    def _get_filepath(self, s: ForexSymbol, tf: Timeframe):
        return self._symbol_dir(s) / self._get_filename(s, tf)

    def _save(self, data: pd.DataFrame, s: ForexSymbol, tf: Timeframe):
        # Ensure incoming data index is UTC and named correctly
        if data.index.tz is None:
            raise ValueError("Incoming data index must be timezone-aware UTC")
        if str(data.index.tz) != "UTC":
            raise ValueError("Incoming data index must be UTC")

        filepath = self._get_filepath(s, tf)
        if filepath.exists():
            existing = pd.read_csv(filepath, index_col="time")
            existing.index = pd.to_datetime(existing.index, utc=True)

            # Concatenate and remove duplicate timestamps (keep latest)
            combined = pd.concat([existing, data])
            combined = combined[~combined.index.duplicated(keep="last")]
            combined = combined.sort_index()
        else:
            combined = data.sort_index()

        combined.to_csv(filepath)
        logging.info(f"Save '{self._get_filename(s, tf)}'")

    def _last_time_in_file(self, filepath: Path):
        df = pd.read_csv(filepath, index_col="time")
        df.index = pd.to_datetime(df.index, utc=True)
        return df.index[-1]

    def _get_time_start(self, s: ForexSymbol, tf: Timeframe):
        DEFAULT_TIME_START = pd.Timestamp("2000-01-01", tz="UTC")

        filepath = self._get_filepath(s, tf)
        if not filepath.exists():
            return DEFAULT_TIME_START

        last_time_in_file = self._last_time_in_file(filepath)
        logging.debug(f"last_time_in_file: {last_time_in_file}")
        return last_time_in_file

    def download(self, s: ForexSymbol, tf: Timeframe):
        """
        Orchestrate downloading process:
        - Download all the (`s`, `tf`)'s data its `DataProvider` can get.
        - Download everything if file does not exist.
        - Download only from latest data if file exists.
        """
        time_start = self._get_time_start(s, tf)
        data = self.provider.get(s, tf, time_start)
        self._save(data, s, tf)
