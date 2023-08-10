from dotenv import dotenv_values
import logging
import requests
import pprint
import json

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
    response.raise_for_status()
    return response.json()['link']


def main():
    get_user_url = 'https://api-ssl.bitly.com/v4/user'
    long_url = 'http://google.com'
    
    print(shorten_link(BITLY_ACCESS_TOKEN, long_url))
    #logging.info(response)
    #pprint.pprint(response.json())




if __name__ == '__main__':
    main()
