from newsdataapi import NewsDataApiClient

# API key authorization, Initialize the client with your API key

api = NewsDataApiClient(apikey="pub_44563e66ade26d4407f93ef1c1ca09dcf4ddc")

# You can pass empty or with request parameters {ex. (country = "us")}
q=str(input('Enter keyword for search: '))
response = api.news_api(q, country="bd", language='en')
s=1
for i in response['results']:
    print(f'{s}. {i['title']}\n{i['link']}\n')
    s+=1
