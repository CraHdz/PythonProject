import requests
from bs4 import BeautifulSoup
from lxml import etree

def main():
    url = "http://www.baidu.com"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
    response = requests.get(url, headers = headers)
    html = response.content
    page1 = etree.HTML(html)
    # print(html)
    with open("baidu.html", "wb") as f:
        f.write(html)
    element = page1.xpath('//*[@id="s-top-left"]/a[5]')
    print(element[0].xpath('./@href'))
    soupObj = BeautifulSoup(html, "lxml")



if __name__ == "__main__":
    main()