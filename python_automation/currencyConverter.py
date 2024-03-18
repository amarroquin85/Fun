from bs4 import BeautifulSoup
import requests
def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    content = requests.get(url, headers= headers).text
    soup = BeautifulSoup(content,'html.parser')
    currency = soup.find('span', class_ ="ccOutputRslt").get_text()
    currency = float(currency[:-4])
    return currency
print(get_currency('USD','JPY'))