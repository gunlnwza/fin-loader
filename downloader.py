import pandas as pd
from provider import DataProvider


class Downloader:
    def __init__(self, provider: DataProvider):
        self.provider = provider
    
    def _save(self, data: pd.DataFrame, symbol, time_frame, time_range):
        # TODO: make name nice?
        name = self.provider.__class__.__name__ + str(symbol) + time_frame + str(time_range) + ".csv"
        data.to_csv(name)

    def download(self, symbol, time_frame, time_range):
        data = self.provider.get(symbol, time_frame, time_range)
        self._save(data, symbol, time_frame, time_range)
