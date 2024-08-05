import requests
from bs4 import BeautifulSoup

# Function to scrape ticket prices from the website
def scrape_ticket_prices(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find elements containing ticket prices
        ticket_prices = soup.find_all('span', class_='ticket-price')  # Adjust based on actual HTML structure

        # Extract prices into a list
        price_list = []
        for price in ticket_prices:
            price_list.append(price.text.strip())

        return price_list
    else:
        print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    # URL of the ticket sales page
    ticket_sales_url = 'https://www.skyscanner.com.tr/tasima/ucak-bileti/tr/buch/?adultsv2=1&cabinclass=economy&childrenv2=&ref=home&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&oym=2409&iym=2409'  # Replace with actual URL

    # Scrape ticket prices
    prices = scrape_ticket_prices(ticket_sales_url)

    if prices:
        print(f"Scraped {len(prices)} ticket prices:")
        for price in prices:
            print(price)
    else:
        print("No ticket prices scraped.")