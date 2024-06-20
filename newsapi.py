import requests


def everything(search, date):
    url = (
        "https://newsapi.org/v2/everything?"
        f"q={search}&"
        f"from=2024-{date}&"
        "sortBy=popularity&"
        "apiKey=7e72878adb5b4566bc74aa9bbf1311ab"
    )
    s=1
    response = requests.get(url).json()
    for articles in response["articles"]:
        print(f'{s}. Title: {articles['title']}\nLink: {articles['url']}\n')
        s+=1
def country(country):
    url = ('https://newsapi.org/v2/top-headlines?'
       f'country={country}&'
       'apiKey=7e72878adb5b4566bc74aa9bbf1311ab')
    s=1
    response = requests.get(url).json()
    for articles in response["articles"]:
        print(f'{s}. Title: {articles['title']}\nLink: {articles['url']}\n')
        s+=1

everything('crypto','5-19')
