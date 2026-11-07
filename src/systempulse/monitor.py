import requests
import time



def check_website(url):

    try: 

        #sends HTTP-GET request and returns response-object   
        start_time = time.perf_counter()

        response = requests.get(url,timeout=5)
        
        end_time = time.perf_counter()

        response_time_ms = (end_time - start_time) * 1000
        

        if 200 <= response.status_code <= 399:
           status = "UP"
        else:
            status = "DOWN"

        result = {
            "url" : url,
            "status" : status,
            "status_code" : response.status_code,
            "response_time_ms" : response_time_ms

        }

        return result

    
    except requests.exceptions.RequestException:
        return {
            "url": url,
            "status": "DOWN",
            "status_code": None,
            "response_time_ms": None
            }


def check_multiple_websites(urls: list[str]):

    results = []

    for url in urls:
        result = check_website(url)
        results.append(result)

    return results

def summarize_results(results: list[dict]):

    up_count = 0
    down_count = 0

    total = len(results)

    for result in results:
        if result["status"] == "UP":
            up_count +=1

        else: down_count +=1

    return {"total websites" : total,
            "websites down" : down_count,
            "websites up" : up_count}


if __name__ == "__main__":
    status = check_website("https://www.youtube.com/")
    print(status)
    print("\n###########")
    urls = [
    "https://github.com/",
    "https://google.com/",
    "https://youtube.com/"
     ]
    
    multi_status = check_multiple_websites(urls)
    for result in multi_status:
        print(result)
 
    test_results = [
    {"url": "https://github.com/", "status": "UP"},
    {"url": "https://google.com/", "status": "UP"},
    {"url": "https://example.com/", "status": "DOWN"}
    
    ]
    
    print("#####################\n")
    summary = summarize_results(test_results)
    print(summary) 



