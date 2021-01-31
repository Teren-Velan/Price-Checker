import requests
from bs4 import BeautifulSoup

URL = "https://coldstorage.com.sg/beers-wines-spirits"

page = requests.get(URL)
parsed_data = BeautifulSoup(page.content, "html.parser")

product_tile = parsed_data.find_all('div', class_="product_box")

filename = 'coldstorage.csv'
f = open(filename, 'w')
headers = 'Product , Price \n'
f.write(headers)

for product in product_tile:
    product_name = product.find('b').text.strip()
    product_desc = product.find('div', class_='product_name').text.strip()
    product_price = product.find('div', class_="price_now").text.strip()

    f.write(product_name + " " + product_desc + ',' + product_price + "\n")

f.close()
