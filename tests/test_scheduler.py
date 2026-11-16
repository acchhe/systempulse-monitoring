
import pytest
from unittest.mock import patch

from src.systempulse.scheduler import run_monitoring


def test_run_monitoring():
    with patch("src.systempulse.scheduler.load_config") as mock_config, \
         patch("src.systempulse.scheduler.check_multiple_websites") as mock_check, \
         patch("src.systempulse.scheduler.time.sleep") as mock_sleep:

        # Simulate configuration
        mock_config.return_value = {
            "websites": ["https://example.com"],
            "check_interval": 5
        }

        # Simulate website check results
        mock_check.return_value = [
            {
                "url": "https://example.com",
                "status": "UP",
                "status_code": 200,
                "response_time_ms": 120
            }
        ]

        # Stop the infinite loop when sleep is called
        mock_sleep.side_effect = KeyboardInterrupt

        # Verify that the monitoring loop can be interrupted
        with pytest.raises(KeyboardInterrupt):
            run_monitoring("test_config.json")

        # Verify that configuration was loaded
        mock_config.assert_called_once_with("test_config.json")

        # Verify that websites were checked
        mock_check.assert_called_once_with(
            ["https://example.com"]
        )

        # Verify that the correct interval was used
        mock_sleep.assert_called_once_with(5)


