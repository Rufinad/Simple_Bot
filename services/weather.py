from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


def get_weather_data():
    ua = UserAgent()
    print(ua.random)
    headers = {'User-Agent': ua.chrome}
    url = 'https://www.gismeteo.ru/weather-sankt-peterburg-pulkovo-12967/'
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    if response.status_code == 200:
        # Извлечение данных о погоде из HTML-страницы
        temperature = soup.find('span', {'class': 'unit unit_temperature_c'}).text.strip()
        weather_feel = soup.find('span', {'class': 'unit unit_temperature_c'}).text.strip()

        # Формирование строки с прогнозом погоды
        weather_data = f"Погода на сегодня:\nТемпература: {temperature}\n Ощущается: {weather_feel}"

        return weather_data
    else:
        print(f"Не удалось получить доступ к странице, статус-код: {response.status_code}")


if __name__ == '__main__':
    get_weather_data()