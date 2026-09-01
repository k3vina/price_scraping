# price_scraping + currency_converter

A Python script that scrapes product prices from [Jumia Kenya](https://www.jumia.co.ke/) and converts them from KES to USD using a live exchange rate API.


## Description

- Scrapes product titles and prices from jumia.co.ke using `requests` and `BeautifulSoup`
- Cleans price text (strips "KSh" and commas, handles price ranges) and converts to numeric values
- Skips non-product elements on the page that don't contain a title or price
- Adds both the original price (KES) and the converted price (USD)
- Fetches a live KES -> USD exchange rate from exchangerate-api.com
- Displays results as a list of dicts and stores them in a `pandas` DataFrame
- Saves the final dataset to `extracted_items.csv`
- Handles connection errors, timeouts, and HTTP errors gracefully


## Prerequisites

- Python 3.x
- Packages listed in `requirements.txt`:
    - `requests`
    - `beautifulsoup4`
    - `pandas`


## Installation and Usage

1. Clone this repository:
```bash
    git clone https://github.com/k3vina/price_scraping
    cd price_scraper
```

2. Create and activate a virtual environment:
```bash
    python -m venv .venv
    .venv\Scripts\activate     # Windows
    source .venv/bin/activate  # macOS/Linux
```

3. Install dependencies:
```bash
    pip install -r requirements.txt
```

4. Replace the API key in `price_scraping.py` with your own from [exchangerate-api.com](https://www.exchangerate-api.com/):
```python
    api_url = "https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/KES"
```

5. Run the script:
```bash
    python price_scraping.py
```

The script will:
1. Fetch the current KES -> USD exchange rate
2. Scrape up to 10 product titles and prices from jumia.co.ke
3. Print the scraped results to the terminal
4. Save the data to `extracted_items.csv`


## Output

`extracted_items.csv` contains the following columns:

| Column          | Description                               |
| --------------- | ----------------------------------------- |
| `product_title` | Name of the scraped product                |
| `price_kes`      | Original price in Kenyan Shillings (KES)  |
| `price_usd`      | Converted price in US Dollars (USD)       |


## Error Handling

The script catches and reports:
- Connection timeouts
- HTTP errors (e.g. site unavailable)
- Missing product data (skips items without a name or price instead of crashing)
- General/unexpected errors


## Known Limitations

- Not every `.itm.col` element on Jumia's homepage is a product card (some are banners/ad slots), so these are filtered out before scraping
- Products with a price range (e.g. "KSh 897 - KSh 1,199") are recorded using the lower bound
- Jumia's page structure and anti-bot behavior may change over time, which can break the selectors without any code changes on your end


## Optional Extensions

- [ ] User-selected currencies: Allow the user to input source/target currencies at runtime
- [ ] Timestamp: Add a `conversion_date` column to track when the conversion was performed
- [ ] Visualization: Plot a bar chart comparing original vs. converted prices using matplotlib
- [ ] Pagination / more categories: Scrape multiple Jumia category pages to collect more than 10 products
- [ ] Environment Variables: Store the API key in a `.env` file instead of hardcoding it
