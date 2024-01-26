import random

from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


def get_joke():
    ua = UserAgent()
    headers = {'User-Agent': ua.chrome}
    url = 'https://anekdotme.ru/random/'
    response = requests.get(url, headers=headers)
    # response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    if response.status_code == 200:
        jokes = soup.find_all('div', class_=['anekdot_text'])
        lst_jokes = [joke.text for joke in jokes]
        res_joke = random.choice(lst_jokes)
        return res_joke.encode()


if __name__ == '__main__':
    get_joke()