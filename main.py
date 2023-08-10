from dotenv import dotenv_values
import logging
import requests
import pprint
import json

BITLY_ACCESS_TOKEN = dotenv_values('.env')['BITLY_ACCESS_TOKEN']


def main():
    logging.basicConfig(level=logging.INFO)
    get_user_url = 'https://api-ssl.bitly.com/v4/user'
    get_bitly_link = 'https://api-ssl.bitly.com/v4/bitlinks'
    headers = {
        'Authorization': f'Bearer {BITLY_ACCESS_TOKEN}',
    }

    payload = {
        'long_url': 'http://google.com'
    }

    
    response = requests.post(get_bitly_link, headers=headers, json=payload)
    response.raise_for_status()
    #logging.info(response.url)
    short_link = response.json()['link']
    print(short_link)
    #logging.info(response)
    #pprint.pprint(response.json())




if __name__ == '__main__':
    main()
