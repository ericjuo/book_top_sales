import requests
import bs4
from typing import Dict
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from datetime import date
import re
from collections import defaultdict
    
def extract_html(url, method) -> BeautifulSoup:
    if method == "requests":
        headers = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            print("Bad connection. Web scraping failed!")
        return bs4.BeautifulSoup(r.text, "html.parser")
    elif method == "selenium":
        chrome_options = Options() 
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome("../d00_utils/chromedriver")
        driver.get(url)
        html = driver.page_source
        driver.quit()
        return bs4.BeautifulSoup(html, "html.parser")
    else:
        print("Unknown method")
        return
    
# 博客來
def books_scraper() -> Dict:
    url = 'https://www.books.com.tw/web/sys_saletopb/books/'
    soup = extract_html(url, method="requests")
    books = soup.find_all(class_="type02_bd-a")[:10]
    top_ten = defaultdict(list)
    rank = 1
    for b in books:
        top_ten['rank'].append(rank)
        top_ten['name'].append(b.h4.a.string)
        top_ten['price'].append(int(b.find_all('b')[1].string))
        top_ten['url'].append(b.h4.a.get("href"))
        rank += 1
    return top_ten

# 金石堂
def kingstone_scraper() -> Dict:
    today = date.today()
    if today.month -1 == 0:
        y = today.year - 1
        m = 12
    else:
        y = today.year
        m = today.month -1

    url = 'https://www.kingstone.com.tw/bestseller/best/book?ranktype=m&y=%s&d=%s' % (y, m)
    soup = extract_html(url, method="requests")
    books = soup.find_all(class_='modProList')[:10]
    topten = defaultdict(list)
    rank = 1
    for b in books:
        topten['rank'].append(rank)
        topten['name'].append(b.find_all("a")[1].string)
        topten['price'].append(int(b.find_all("b")[1].string))
        topten['url'].append("https://www.kingstone.com.tw" + books[0].find_all("a")[1].get("href"))
        rank += 1
    return topten

# 城邦
def cite_scraper() -> Dict:
    url = 'https://www.cite.com.tw/bestseller/index/parade/hit/all'
    soup = extract_html(url, method="requests")
    books = books = soup.find_all(class_="col-md-2 col-sm-4 col-xs-6 item")[:10]
    pattern = re.compile(r"(\d+)")
    topten = defaultdict(list)
    rank = 1
    for b in books:
        topten['rank'].append(rank)
        topten['name'].append(b.h3.a.string)
        topten['price'].append(int(pattern.search(str(b.find(class_="red"))).group(0)))
        topten['url'].append("https://www.cite.com.tw" + b.h3.a.get("href"))
        rank += 1
    return topten    


# 三民
def sanmin_scraper() -> Dict:
    url = 'https://www.sanmin.com.tw/Promote/Top/MBYY'
    soup = extract_html(url, method="requests")
    books = soup.find_all(class_="searchprod")[:10]
    topten = defaultdict(list)
    pattern = re.compile(r'(\d+)\.(.+)')
    rank = 1
    for b in books:
        topten['rank'].append(rank)
        topten['name'].append(pattern.search(str(b.h3.a.string)).group(2))
        topten['price'].append(int(b.span.find(style="color: red; font-size: 20px").string))
        topten['url'].append("https://www.sanmin.com.tw/" + books[0].h3.a.get("href"))
        rank += 1
    return topten

# 墊腳石
def tcsb_scraper() -> Dict:
    url = "https://www.tcsb.com.tw/v2/official/SalePageCategory/264475?sortMode=Sales"
    soup = extract_html(url, method="selenium")
    books = soup.find_all(class_="product-card__vertical product-card__vertical--hover")[:10]
    pattern = re.compile(r"(\d+)")
    topten = defaultdict(list)
    rank =1
    for b in books:
        topten['rank'].append(rank)
        topten['name'].append(b.find(class_="sc-fzXfNO cjNSCe").string)
        topten['price'].append(int(pattern.search(str(b.find(class_="sc-fzXfNR bsRQkb").string)).group(1)))
        topten['url'].append("https://www.tcsb.com.tw/" + books[0].a.get("href"))
        rank += 1
    return topten

# 讀冊
def taaze_scraper() -> Dict:
    url = 'https://www.taaze.tw/rwd_listViewB.html?t=01&k=00&d=00&l=00&a=01'
    soup = extract_html(url, "selenium")
    topten = defaultdict(list)
    books = soup.find_all(class_="bookGridByListView")[:10]
    rank = 1
    for b in books:
        topten['rank'].append(rank)
        topten['name'].append(b.find_all("a")[1].string)
        topten['price'].append(int(b.find_all("span")[1].string))
        topten['url'].append("https://www.taaze.tw/" + books[0].find_all("a")[1].get("href"))
        rank += 1
    return topten