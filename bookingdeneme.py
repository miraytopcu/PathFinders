import requests
import pandas as pd

# URL of the CSV file (using a different example)
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv"

# Function to download CSV file from URL
def download_csv(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"CSV file downloaded successfully and saved as {save_path}")
    else:
        print("Failed to download CSV file.")

# Function to process and analyze the CSV data
def process_csv(file_path):
    df = pd.read_csv(file_path)
    
    # Example analysis: print the first 5 rows
    print(df.head())

# Main function
def main():
    save_path = "addresses.csv"
    download_csv(url, save_path)
    process_csv(save_path)

if __name__ == "__main__":
    main()
