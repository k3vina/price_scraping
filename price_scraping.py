import requests
from requests.exceptions import HTTPError, Timeout
from bs4 import BeautifulSoup
import pandas as pd

try:

   
    url = "https://www.jumia.co.ke/"

    headers = {
        "User-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
    }   

    book_response = requests.get(url, headers= headers, timeout=30)

    book_response.raise_for_status()

    #print(book_response.status_code)
    #print(book_response.content)


    soup = BeautifulSoup(book_response.content, "html.parser")
    #print(soup)

    books = soup.select(".product_pod")
    #print(cards[0].select_one("h3 a").text)
    #print(cards[0].select_one(".price_color").text)


    items = soup.select(".itm.col")
    #print(items)


except Timeout:
    print("The server took long to respond") # prints 429 code
except HTTPError as err:
    print(f"HTTP error occured: {err}") # prints 400/500 code
except Exception as err:
    print(f"Something went wrong {err}")

 