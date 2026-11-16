
from unittest.mock import patch
from main import main


def test_main_keyboard_interrupt(capsys):

    # Simulate Ctrl+C without starting real monitoring
    with patch("main.run_monitoring") as mock_monitor:
        mock_monitor.side_effect = KeyboardInterrupt

        # Run the main function
        main()

        # Verify that monitoring was started
        mock_monitor.assert_called_once_with("./config.json")

    # Capture terminal output
    captured = capsys.readouterr()

    # Verify the shutdown message
    assert "Monitoring stopped by user." in captured.out
