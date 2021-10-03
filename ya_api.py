import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path}
        resp = requests.get(upload_url, headers=headers, params=params)
        url = resp.json().get('href', '')
        requests.put(url=url, data=open('ya_test.txt', 'rb'))


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'ya_test.txt'
    token = ''
    uploader = YaUploader(token)
    uploader.upload(path_to_file)