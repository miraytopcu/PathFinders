import requests

def query_journeys(api_key, origin, destination, date):
    endpoint = "https://xx.xx.xx.xx/api/v2/journeys/basic"
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    params = {
        'origin': origin,
        'destination': destination,
        'date': date
    }

    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()

        if response.status_code == 200:
            journeys = response.json().get('journeys', [])

            for journey in journeys:
                print(f"Departure Time: {journey.get('departure_time')}")
                print(f"Arrival Time: {journey.get('arrival_time')}")
                print(f"Price: {journey.get('price')}")
                print("")

        else:
            print(f"Request failed with status code {response.status_code}: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

# Example usage
if __name__ == "__main__":
    api_key = 'YOUR_OBILET_API_KEY'
    origin = 'IST'  # Example: Istanbul
    destination = 'ANK'  # Example: Ankara
    date = '2024-08-04'  # Example: Date of travel

    query_journeys(api_key, origin, destination, date)

