from unittest.mock import patch, Mock
from src.systempulse.monitor import check_website,check_multiple_websites
import requests



def test_web_up():

    mock_response = Mock()
    mock_response.status_code = 200

    with patch("src.systempulse.monitor.requests.get") as mock_get:

        mock_get.return_value = mock_response

        result = check_website("https://www.youtube.com/")

        assert result["status"] == "UP"

        assert result["status_code"] == 200

def test_web_down():

    mock_response = Mock()
    mock_response.status_code = 500

    with patch("src.systempulse.monitor.requests.get") as mock_get:

        mock_get.return_value = mock_response

        result = check_website("https://github.com/")

        assert result["status"] == "DOWN"

        assert result["status_code"] == 500

def test_connection_error():


    with patch("src.systempulse.monitor.requests.get") as mock_get:

        mock_get.side_effect = requests.exceptions.ConnectionError

        result = check_website("https://github.com/")

        assert result["status"] == "DOWN"

        assert result["status_code"] is None

        assert result["response_time_ms"] is None

def test_timeout():

    with patch("src.systempulse.monitor.requests.get") as mock_get:

        mock_get.side_effect = requests.exceptions.Timeout

        result = check_website("https://github.com/")

        
        assert result["status"] == "DOWN"

        assert result["status_code"] is None

        assert result["response_time_ms"] is None


def test_multiple_websites():

     urls = [
            "https://github.com/",
            "https://google.com/",
            "https://youtube.com/"
            ]

     with patch("src.systempulse.monitor.check_website") as mock_check:

         results = check_multiple_websites(urls)

         assert mock_check.call_count == 3

         assert (len(results)) == 3

         mock_check.assert_any_call("https://github.com/")

         mock_check.assert_any_call("https://google.com/")

         mock_check.assert_any_call("https://youtube.com/")

             

             


         

