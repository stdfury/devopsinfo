import requests


def upload_item(data, url_prefix):
    url = "https://korneplod.xyz/api/" + url_prefix
    response = requests.post(url, data=data)
    print(response.status_code)

