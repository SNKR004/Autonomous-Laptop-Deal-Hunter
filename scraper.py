from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

def scrape_flipkart(search_query):

    products = []

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        search_url = (
            f"https://www.flipkart.com/search?q={search_query}"
        )

        page.goto(search_url)

        time.sleep(5)

        html = page.content()

        soup = BeautifulSoup(html, "html.parser")

        cards = soup.select("div[data-id]")

        for card in cards[:10]:

            title = card.get_text(" ", strip=True)[:200]

            price_elem = card.select_one("div.Nx9bqj")

            if price_elem:
                price = price_elem.text
            else:
                price = "N/A"

            products.append({
                "title": title,
                "price": price
            })

        browser.close()

    return products