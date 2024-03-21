import requests

r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2024-02-20&to=2024-2-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')
content = r.json()
print(content['articles'][0]['description'])