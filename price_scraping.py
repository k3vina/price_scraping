import requests
from requests.exceptions import HTTPError, Timeout
from bs4 import BeautifulSoup

try:
    api_url = "https://v6.exchangerate-api.com/v6/a5a0f70d5a3e8a3acc871a24/latest/KES"

    api_response = requests.get(api_url)

    api_response.raise_for_status()
    #print(api_response.status_code)
    #print(api_response.text[:200])  # just the first 200 chars, not the whole HTML page

    data = api_response.json()
    #print(data.keys())
 
    usd_rate = data["conversion_rates"]["USD"]
    print(f"KES to USD rate: {usd_rate}")


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

    all_scraped_items = []                  

    for item in items[:10]:                      # limit to first 10
        title = item.select_one(".itm col").text
        price_text = item.select_one(".prc").text   # e.g. "KSh 1,080"

        price_kes = float(price_text.replace("KSh", "").replace(",", "").split("-")[0].strip())
        price_usd = price_kes / usd_rate

        item_dict = {
            "product_title": title,
            "price_kes": price_kes,
            "price_gbp": round(price_gbp, 2),
        }

        all_scraped_items.append(item_dict)

    #print(all_scraped_items)

    df = pd.DataFrame(all_scraped_items)
    #print(df)
    df.to_csv("extracted_items.csv")

except Timeout:
    print("The server took long to respond") # prints 429 code
except HTTPError as err:
    print(f"HTTP error occured: {err}") # prints 400/500 code
except Exception as err:
    print(f"Something went wrong {err}")

 