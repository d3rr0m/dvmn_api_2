from urllib.parse import urlparse
from dotenv import dotenv_values
import logging
import requests
import pprint


BITLY_ACCESS_TOKEN = dotenv_values('.env')['BITLY_ACCESS_TOKEN']


def shorten_link(token, url):
    get_bitly_link = 'https://api-ssl.bitly.com/v4/bitlinks'
    
    headers = {
        'Authorization': f'Bearer {BITLY_ACCESS_TOKEN}',
    }
    
    payload = {
        'long_url': f'{url}'
    }
    
    response = requests.post(get_bitly_link, headers=headers, json=payload)
    logging.info(response.status_code)
    response.raise_for_status()
    bitlink = response.json()['link']
    return bitlink


def clicks_count(token, url):
    get_bitly_link = 'https://api-ssl.bitly.com/v4/bitlinks'
        
    headers = {
        'Authorization': f'Bearer {BITLY_ACCESS_TOKEN}',
    }
    
    payload = {
        'long_url': f'{url}'
    }
    
    response = requests.post(get_bitly_link, headers=headers, json=payload)
    response.raise_for_status()
    bitlink = response.json()['link']
    logging.info(response.status_code)
    parsed_bitlink = urlparse(bitlink)
    logging.info(parsed_bitlink)
    bitlink = f'{parsed_bitlink.netloc}{parsed_bitlink.path}'

    get_clicks_count_link = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'.format(bitlink=bitlink)
    response = requests.get(get_clicks_count_link, headers=headers)
    logging.info(get_clicks_count_link)
    pprint.pprint(response)
    response.raise_for_status()
    logging.info(response.status_code)
    
    count = response.json()['total_clicks']
    
    return count


def main():
    logging.basicConfig(level=logging.WARNING)
    get_user_url = 'https://api-ssl.bitly.com/v4/user'
    #long_url = 'http://google.com'
    long_url = input('Введите ссылку для сокращениея: ')
    
    try:
        print('Битлинк', shorten_link(BITLY_ACCESS_TOKEN, long_url))
    except requests.exceptions.HTTPError:
        print('Был введен неверный URL')
    
    try:
        print(clicks_count(BITLY_ACCESS_TOKEN, long_url))
    except requests.exceptions.HTTPError:
        print('Ошибка при получении кол-ва кликов')
    
    
    #logging.info(response)
    #pprint.pprint(response.json())




if __name__ == '__main__':
    main()
