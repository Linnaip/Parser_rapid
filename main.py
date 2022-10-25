import requests
import csv

from bs4 import BeautifulSoup


def get_image(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('data-original', class_='img')
    for item in items:
        return item


def get_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('li', class_="type-product")
    result = []
    for i, row in enumerate(items, start=1):
        itemName = row.find('h2', class_='woo-loop-product__title').text.strip()
        itemPrice = row.find('span', class_='price').text.split(" CFA")[0]
        itemDescription = row.find('div', class_="woocommerce-product-details__short-description")
        itemImage = row.find('href', class_='mf-product-thumbnail')

        row_data = {'h4': itemName,
                'h5': itemPrice,
                'description': itemDescription,
                'src': itemImage,
                }
        result.append(row_data)
    
    write_csv(result)
    
    return result


def write_csv(row_list):
    with open('listfromsite.csv', 'a') as open_file:
        recorder = csv.DictWriter(open_file, fieldnames=['h4', 'h5', 'description', 'src'])
        recorder.writeheader()
        recorder.writerows(row_list)


def main():
    url = 'https://market.rapidos.sn/categorie/electromenager/gros-electromenager-electromenager/'
    print(get_data(url))


if __name__ == '__main__':
    main()
