import requests

def fetchandSave(url, path):
    r = requests.get(url)
    with open(path, 'w', encoding="utf-8") as f:
        f.write(r.text)

moneycontrol_url = "https://www.moneycontrol.com/news/"
livemint_url = "https://www.livemint.com/market"
economictimes_url = "https://economictimes.indiatimes.com/markets"
reuters_url = "https://www.reuters.com/markets/"
cnbc_url = "https://www.cnbc.com/markets/"

fetchandSave(moneycontrol_url, "data/moneycontrol.html")
fetchandSave(livemint_url, "data/livemint.html")
fetchandSave(economictimes_url, "data/economictimes.html")
fetchandSave(reuters_url, "data/reuters.html")
fetchandSave(cnbc_url, "data/cnbc.html")
print("data fetched")


