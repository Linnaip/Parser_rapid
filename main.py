import requests
import csv

from bs4 import BeautifulSoup


def get_image(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('data-original', class_='product-inner  clearfix')
    for item in items:
        return item


def get_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('div', class_="mf-product-details-hover")
    for n, i in enumerate(items, start=1):
        itemName = i.find('h2', class_='woo-loop-product__title').text.strip()
        itemPrice = i.find('span', class_='price').text
        itemImage = get_image(url)
        #iteddiscription =

        data = {'h4': itemName,
                'h5': itemPrice,
                'src': itemImage}
        #write_csv(data)
        return data


def write_csv(data):
    with open('listfromsite.csv', 'a') as open_file:
        recorder = csv.writer(open_file)
        recorder.writerow((data['h4'],
                           data['h5'],
                           data['src']))


def main():
    url = 'https://market.rapidos.sn/categorie/electromenager/gros-electromenager-electromenager/'
    print(get_data(url))


if __name__ == '__main__':
    main()