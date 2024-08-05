import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to scrape
url = 'https://www.skyscanner.com.tr/tasima/kalkis-yeri/tr/?adultsv2=1&cabinclass=economy&childrenv2=&ref=home&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&oym=2409&iym=2409 '

# Send a GET request to the URL
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find elements containing ticket prices
ticket_prices = soup.find_all('span', class_='ticket-price')  # Adjust based on actual HTML structure

# Extract prices into a list
price_list = []
for price in ticket_prices:
    price_list.append(price.text.strip())

# Create a DataFrame using pandas
df = pd.DataFrame({'Ticket Prices (TL)': price_list})

# Export DataFrame to Excel
df.to_excel('obilet_ticket_prices.xlsx', index=False)

print(f"Scraped {len(price_list)} ticket prices. Data saved to 'obilet_ticket_prices.xlsx'.")