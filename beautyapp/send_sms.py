import requests


def send_auth_sms(api_key, phonenumber, text):
    url = 'https://sms.ru/sms/send'
    params = {
        'api_id': api_key,
        'to': phonenumber,
        'msg': text,
    }

    response = requests.post(url, params=params)
    response.raise_for_status()
