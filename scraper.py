import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

print("🚀 E-commerce Scraper Starting...")

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

titles = []
prices = []
ratings = []
links = []

try:

    for page in range(1, 6):

        print(f"Scraping Page {page}")

        url = base_url.format(page)
        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("article", class_="product_pod")

        for book in books:

            title = book.h3.a["title"]

            # Clean price using regex (more stable ⭐)
            price_text = book.find("p", class_="price_color").text
            price = float(re.sub(r"[^\d.]", "", price_text))

            rating = book.p["class"][1]

            link = "https://books.toscrape.com/catalogue/" + book.h3.a["href"]

            titles.append(title)
            prices.append(price)
            ratings.append(rating)
            links.append(link)

    df = pd.DataFrame({
        "Title": titles,
        "Price": prices,
        "Rating": ratings,
        "Link": links
    })

    df.to_csv("products.csv", index=False)

    print("✅ Scraping Completed Successfully")

except Exception as e:
    print("❌ Error:", e)