# parser for https://ninjasushi.com.ua/
import requests
from bs4 import BeautifulSoup


def get_list_of_sushi_info(url):
    response = requests.get(url)
    html = BeautifulSoup(response.text, features='html5lib')
    sushi_divs = html.find_all("div", {"class": "cat-slide swiper-slide"})

    sushi_data = []

    for div in sushi_divs:
        name = div.select_one('.cat-slide-content > .cat-slide-name > a')
        weight = div.select_one('.cat-slide-content > .cat-slide-desc > span')
        price = div.select_one('.cat-slide-content > .cat-slide-buy > .price')
        image = div.select_one('.cat-image > a > img')

        single_sushi_tuple = (name.text, weight.text, price.text, image.get('src'))

        sushi_data.append(single_sushi_tuple)

    return sushi_data
