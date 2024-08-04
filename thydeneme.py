"""
HTTP error occurred: 500 Server Error: Internal Server Error for url: 
https://api.turkishairlines.com/availability?departureAirportCode=IST&arrivalAirportCode=LHR&date=2024-08-04

"""
import requests
import csv
import time

def fetch_and_store_flight_availability(api_key, output_file):
    endpoint = "https://api.turkishairlines.com/availability"
    headers = {
        'apikey': api_key,
        'Accept': 'application/json'
    }
    params = {
        'departureAirportCode': 'IST',
        'arrivalAirportCode': 'LHR',
        'date': '2024-08-04'
    }

    max_retries = 3
    retries = 0
    wait_time = 5  # Initial wait time in seconds

    while retries < max_retries:
        try:
            response = requests.get(endpoint, headers=headers, params=params)
            response.raise_for_status()

            if response.status_code == 200:
                flights = response.json().get('availability', [])

                with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
                    fieldnames = ['flight_number', 'departure_time', 'arrival_time', 'fare']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()

                    for flight in flights:
                        writer.writerow({
                            'flight_number': flight.get('flight_number', ''),
                            'departure_time': flight.get('departure_time', ''),
                            'arrival_time': flight.get('arrival_time', ''),
                            'fare': flight.get('fare', '')
                        })

                print(f"Successfully wrote flight availability information to {output_file}")
                return  # Exit function upon successful retrieval

            else:
                print(f"Request failed with status code {response.status_code}: {response.text}")
                retries += 1
                time.sleep(wait_time)
                wait_time *= 2  # Exponential backoff

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            retries += 1
            time.sleep(wait_time)
            wait_time *= 2  # Exponential backoff

        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            retries += 1
            time.sleep(wait_time)
            wait_time *= 2  # Exponential backoff

    print(f"Failed to retrieve flight availability information after {max_retries} retries.")

# Example usage
if __name__ == "__main__":
    api_key = 'YOUR_TURKISH_AIRLINES_API_KEY'
    output_file = 'flight_availability.csv'
    fetch_and_store_flight_availability(api_key, output_file)


