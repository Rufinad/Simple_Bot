from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


def get_exchange_rate():
    ua = UserAgent()
    # print(ua.random)
    headers = {'User-Agent': ua.chrome}
    url = 'https://www.cbr-xml-daily.ru/latest.js'
    response = requests.get(url, headers=headers).json()
    return (f"Курс <b>доллара</b> на сегодня составляет: {round(1/float(response['rates']['USD']), 2)}\n"
            f"Курс <b>евро</b> на сегодня составляет: {round(1/float(response['rates']['EUR']), 2)}")


if __name__ == '__main__':
    get_exchange_rate()