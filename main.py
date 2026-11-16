from src.systempulse.config import load_config
from src.systempulse.monitor import check_multiple_websites

path = "./config.json"

data = load_config(path)

urls = data['websites']

results = check_multiple_websites(urls)

for url in results:
    print(url)


