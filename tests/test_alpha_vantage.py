from unittest.mock import patch, Mock
import pytest
import pandas as pd

from finloader.core import ForexSymbol, Timeframe
from finloader.provider import AlphaVantage
from finloader.exceptions import TemporaryRateLimit, DailyRateLimit


def mock_alpha_vantage_rate_limit(*args, **kwargs):
    mock_resp = Mock()
    mock_resp.status_code = 200

    mock_resp.headers = {
        "Content-Type": "application/json"
    }

    mock_resp.json.return_value = {
        "Information":
        "Thank you for using Alpha Vantage! "
        "Please consider spreading out your free API requests more sparingly (1 request per second). "
        "You may subscribe to any of the premium plans at https://www.alphavantage.co/premium/ "
        "to lift the free key rate limit (25 requests per day), "
        "raise the per-second burst limit, and instantly unlock all premium endpoints"
    }
    return mock_resp


@patch("requests.get", side_effect=mock_alpha_vantage_rate_limit)
def test_alpha_vantage_rate_limit(mock_get):
    provider = AlphaVantage(api_key="fake")

    with pytest.raises(TemporaryRateLimit):
        provider._call_api(
            ForexSymbol("EUR", "USD"),
            Timeframe(1, "day"),
            pd.Timestamp("2025-01-01", tz="UTC")
        )
