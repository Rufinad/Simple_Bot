import random
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


def get_horoscope(zodiac: str):
    ua = UserAgent()
    headers = {'User-Agent': ua.chrome}
    url = f'https://horo.mail.ru/prediction/{zodiac}/today/'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    if response.status_code == 200:
        horo = soup.find('div', class_=['article__item article__item_alignment_left article__item_html']).text
        return horo


if __name__ == '__main__':
    get_horoscope('scorpio')

