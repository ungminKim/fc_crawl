import requests
import lxml.html

def main():
    response = requests.get("https://www.skyscanner.co.kr")

    urls = scrape_trip_plan(response)

    # for url in urls:
        # print(url.headers())

def scrape_trip_plan(response):
    urls = []
    root = lxml.html.fromstring(response.content)
    print(root)

if __name__ == "__main__":
    main()