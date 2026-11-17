import os
import time

from src.systempulse.config import load_config
from src.systempulse.monitor import check_multiple_websites


def run_monitoring(path):
    while True:
        data = load_config(path)

        urls = data["websites"]

        interval = int(
            os.getenv("CHECK_INTERVAL", data["check_interval"])
        )

        results = check_multiple_websites(urls)

        for result in results:
            print(result)

        time.sleep(interval)
