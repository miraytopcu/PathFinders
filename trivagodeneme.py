"""
Request error: 403 Client Error: Forbidden for url: https://api.trivago.com/v1/hotels

"""

import requests
import csv

def fetch_and_store_hotels(api_key, output_file):
    endpoint = "https://api.trivago.com/v1/hotels"
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()

        if response.status_code == 200:
            hotels = response.json().get('hotels', [])

            with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['hotel_id', 'name', 'address', 'city', 'country', 'rating']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                for hotel in hotels:
                    writer.writerow({
                        'hotel_id': hotel.get('hotel_id', ''),
                        'name': hotel.get('name', ''),
                        'address': hotel.get('address', ''),
                        'city': hotel.get('city', ''),
                        'country': hotel.get('country', ''),
                        'rating': hotel.get('rating', '')
                    })

            print(f"Successfully wrote hotel information to {output_file}")
        else:
            print(f"Request failed with status code {response.status_code}: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

# Example usage
if __name__ == "__main__":
    api_key = 'YOUR_TRIVAGO_API_KEY'
    output_file = 'hotels_info.csv'
    fetch_and_store_hotels(api_key, output_file)
