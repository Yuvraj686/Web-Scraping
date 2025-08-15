import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

products = []
for item in soup.select(".product_pod"):
    name = item.h3.a["title"]
    price = item.select_one(".price_color").text
    rating = item.p["class"][1]
    products.append([name, price, rating])

with open("products.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Price", "Rating"])
    writer.writerows(products)
