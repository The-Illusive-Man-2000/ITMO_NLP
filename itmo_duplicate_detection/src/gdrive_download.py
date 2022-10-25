import re

import requests
from urllib.parse import urlencode


class YDrive:
    def __init__(self, public_key):
        self.__public_key = public_key
        self.__destination = None
        self.URL = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
        self.link = public_key


    def __make_final_url(self):
        return self.URL + urlencode(dict(public_key=self.__public_key))

    @property
    def link(self):
        # Получаем загрузочную ссылку
        return self.__link

    @link.setter
    def link(self, new_publik_key):
        # Получаем загрузочную ссылку
        self.__public_key = new_publik_key
        response = requests.get(self.__make_final_url())
        self.__link = response.json()['href']

    @property
    def public_key(self, new_publik_key):
        self.__public_key = new_publik_key

    @public_key.setter
    def public_key(self):
        return self.__public_key

    @property
    def destination(self):
        return self.__destination

    @destination.setter
    def destination(self, new_value):
        self.__destination = new_value

    def download_from_yandex(self, destination):
        # Загружаем файл и сохраняем его
        download_response = requests.get(self.__link)
        self.save_response_content(download_response, destination)
        print(f'Файл скачан: {destination}')

    @staticmethod
    def save_response_content(response, destination):
        """
        Сохраняем файл
        """
        with open(destination, "wb") as f:
            f.write(response.content)


if __name__ == "__main__":
    from pathlib import Path

    link = 'https://disk.yandex.ru/d/eK15uq89IOUgfg'
    raw_fn = 'train.xlsx'
    data_dir = Path.cwd().parent / 'data' / 'raw'
    yd = YDrive(link)

    yd.download_from_yandex(destination=data_dir / raw_fn)