import requests
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_image(url):
    f = urlopen(url)
    page = f.read()
    f.close()
    soup = BeautifulSoup(page)
    for link in soup.findAll('img'):
        return "IMAGE LINKS:", link.get('data-src')
    #response = requests.get(url)
    #soup = BeautifulSoup(response.text, 'lxml')
    #items = soup.find_all('img', class_="card-img-top img-fluid")
    #for item in items:
    #    item = item.find('src')
    #    return item


def main():
    url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
    print(get_image(url))


if __name__ == '__main__':
    main()