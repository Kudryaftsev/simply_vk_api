import requests
import csv

def take_posts():
    token = '6041c7a96041c7a96041c7a9b0602dff5d660416041c7a93d0e341326c7f6573664d06a'
    version = 5.101
    domain = 'pikabu'
    count = 100
    offset = 0
    all_posts = []
    
    while offset < 500:
        response = requests.get('https://api.vk.com/method/wall.get',
            params = {
            'access_token': token,
            'v': version,
            'domain': domain,
            'count': count,
            'offset': offset
            })
        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
        
    return all_posts

all_posts = take_posts()