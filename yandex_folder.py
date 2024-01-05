import requests

with open('ya-tok.txt', 'r') as file_object:
    ya_token = file_object.read().strip()


def make_yandex_dir():
    url = 'https://cloud-api.yandex.net:443/v1/disk/resources/'
    headers = {'Authorization': ya_token}
    params = {'path' : 'yandex_folder'}
    response = requests.put(url, headers=headers, params=params)
    return response.status_code

if __name__ == '__main__':
    print(make_yandex_dir())