import pandas as pd
from provider import DataProvider


class Downloader:
    def __init__(self, provider: DataProvider):
        self.provider = provider
    
    def _save(self, data: pd.DataFrame, symbol, time_frame, time_range):
        base, quote = symbol
        start, end = time_range

        name = f"{self.provider.__class__.__name__}_{base}{quote}_{time_frame}_{start}_{end}.csv"
        data.to_csv(name)

    def download(self, symbol, time_frame, time_range):
        data = self.provider.get(symbol, time_frame, time_range)
        self._save(data, symbol, time_frame, time_range)
