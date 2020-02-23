import requests
import lxml.html

def main():
    response = requests.get("https://www.naver.com/")

    urls = scrape_trip_plan(response)

    for url in urls:
        print(url)

def scrape_trip_plan(response):
    urls = []
    root = lxml.html.fromstring(response.content)
    
    for a in root.cssselect('#PM_ID_themecastBody > div > div > div.area_themecast > ul > li > a'):
        url = a.get('href')
        urls.append(url)
    return urls

if __name__ == "__main__":
    main()