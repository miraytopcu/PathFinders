import requests
import pandas as pd

baseurl = "https://rickandmortyapi.com/api/"
endpoint = "character"

def main_request(baseurl, endpoint, x):
    r = requests.get(baseurl + endpoint + f'?page={x}')
    return r.json()

def get_pages(response):
    pages = response['info']['pages']
    return pages

def parse_json(response):
    charList = []
    for item in response['results']:
        # name = data['results'][item]['name']
        # episodes = data['results'][item]['episode']
        # print(item['name'], len(item['episode']))
        char = {
            "ID" : item['id'],
            "name" : item['name'],
            "num_episode" : len(item['episode'])
        }

        charList.append(char)
    return charList

mainlist = []

data = main_request(baseurl, endpoint, 3)
# print(get_pages(data))
# print(parse_json(data))

for x in range(1, get_pages(data) + 1):
    # print(x)
    mainlist.extend(parse_json(main_request(baseurl, endpoint, x)))

df = pd.DataFrame(mainlist)
df.to_csv('charlist.csv', index=False)

# print(len(mainlist))