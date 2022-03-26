# Top sales books in Taiwan
## Goals
- [] List top sales books in each platform in Taiwan
    - [] book name, price, number sold (if possible)
    - [] Parallel comparison table
    - [] Show ranks by row
    - [] Aim for top 10
    - [] Web crawler
    - [] Document the software I use

- [] Build a sqlite database
    - [] The data will be overwrite every week, update data on each monday morning
    - [] The data should include book name, price, platform, href link to the product page.

- [] Publish to a webpage (through github)



## Enviroment
```
$ conda create --name books
```
environment location: /home/ericjuo/miniconda3/envs/books

## Software
Python
```
$ python --version
Python 3.10.0
```
BeautifulSoup4
```
import requests
print(requests.__version__)

2.27.1
```
Selenium
```
import selenium
print(selenium.__version__)

3.141.0
```


