import os
from dotenv import load_dotenv
from provider import AlphaVantage, Massive, TwelveData
from downloader import Downloader


if __name__ == "__main__":
    load_dotenv()

    # provider = AlphaVantage(os.getenv("ALPHA_VANTAGE_API_KEY"))
    provider = Massive(os.getenv("MASSIVE_API_KEY"))
    # provider = TwelveData(os.getenv("TWELVE_DATA_API_KEY"))

    downloader = Downloader(provider)

    symbol = ("USD", "JPY")
    time_frame = "1D"
    time_range = ("2025-01-01", "2025-02-15")
    downloader.download(symbol, time_frame, time_range)
