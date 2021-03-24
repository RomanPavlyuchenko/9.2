import requests
import os
from Ya_token import YANDEX_DISK_TOKEN


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': os.path.basename(file_path), 'overwrite': 'true'}
        response = requests.get(url, headers=self.get_headers(), params=params)
        if response.status_code == 200:
            upload_url = response.json()['href']
            with open(file_path, 'rb') as s:
                response = requests.put(upload_url, data=s)
            if response.status_code == 201:
                return 'Success'


if __name__ == '__main__':
    uploader = YaUploader(YANDEX_DISK_TOKEN)
    result = uploader.upload('/home/test.txt')
    print(result)
