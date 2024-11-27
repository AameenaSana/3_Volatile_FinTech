import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["STOCKNEWS"]
collection = db["articles"]

def extract_data_from_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, "html.parser")

    #todo: Extracting the title, link, and summary from different tags/classes for the 3 websites

    extracted_data = []

    # MoneyControl
    for item in soup.find_all("h3", class_="related_des"):
        link = item.find("a")["href"]
        title = item.find("a")["title"]
        summary = item.get_text(strip=True)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        extracted_data.append({"title": title, "link": link, "summary": summary, "timestamp": timestamp})

    # LiveMint
    for item in soup.find_all("h2"):
        a_tag = item.find("a")
        if a_tag and a_tag.get("href"):
            link = a_tag["href"]
            title = a_tag.get_text(strip=True)
            summary = title  
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            extracted_data.append({"title": title, "link": link, "summary": summary, "timestamp": timestamp})

    #economictimes
    for item in soup.find_all("a", class_="font_faus wrapLines l1"):
        link = item["href"]
        title = item.get("title", "")
        summary = item.get_text(strip=True)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        extracted_data.append({"title": title, "link": link, "summary": summary, "timestamp": timestamp})

    return extracted_data

files = ["data/livemint.html", "data/economictimes.html", "data/moneycontrol.html", "data/cnbc.html"]

for file in files:
    data = extract_data_from_html(file)
    print(f"Extracted data from {file}:")
    collection.insert_many(data)
print("data updated on mongoDB")


