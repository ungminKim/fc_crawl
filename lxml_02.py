import requests
from lxml.html import fromstring, tostring

def main():
    session = requests.Session()
    response = session.get("https://www.naver.com")
    urls = scrape_news_list_page(response)

    for k, v in urls.items():
        print(k, "->", v)

    
def scrape_news_list_page(response):
    urls = {}
    root = fromstring(response.content)

    for a in root.xpath("//ul[@class='api_list']/li[@class='api_item']/a[@class='api_link']"):
        name, url = extract_contents(a)
        urls[name] = url
    
    return urls

def extract_contents(dom):
    link = dom.get("href")
    name = dom.xpath('./img')[0].get('alt')

    return name, link

if __name__ == "__main__":
    main()
