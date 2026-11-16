from src.systempulse.scheduler import run_monitoring


def main():
    try:
        run_monitoring("./config.json")

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")


if __name__ == "__main__":
    main()




