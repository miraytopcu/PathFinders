from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import pandas as pd
import time

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
# options.add_argument("--headless")  # Comment out headless mode for debugging

# Initialize the Chrome driver
driver = webdriver.Chrome(options=options)

# burada genel link aynı mantık üzerine kurulu, sadece link üzerinde 2 alan şehire göre değişiyor, bende linki 
# her seferinde ayrı ayrı verip kod kalabalığı yapmak istemediğim için farklı yerleri belirleyip listeye atadım, 
# artık o şehire sıra gelince sadece link üzerindeki belirli alanları düzenliyor
codes = {
    "istanbul": ["i%CC%87stanbul", "288"],
    "ankara": ["ankara", "245"],
    "adana": ["adana", "236"]
}

hotels_info = []

def fetch_hotel_data(driver, wait, ad_xpath, fiyat_xpath, city_name):
    try:
        otel_adi = wait.until(EC.presence_of_element_located((By.XPATH, ad_xpath))).text
        otel_fiyati = wait.until(EC.presence_of_element_located((By.XPATH, fiyat_xpath))).text
        return [city_name, otel_adi, otel_fiyati]
    except (NoSuchElementException, TimeoutException) as e:
        print(f"Error fetching hotel data: {e}")
        return [city_name, "N/A", "N/A"]

for sehir, bilgiler in codes.items():
    kod = bilgiler[0]
    sayi = bilgiler[1]
    url = f"https://www.trivago.com.tr/tr/srl/otel-{kod}-t%C3%BCrkiye?search=200-15{sayi};dr-20240928-20240929-s;rc-1-1;so-3"
    driver.get(url)
    wait = WebDriverWait(driver, 20)
    
    # Define XPaths for the hotel elements
    otel_xpath_ad = [
        '//*[@id="__next"]/div[1]/main/div[3]/section/div/div/ol/li[3]/div/article/div[2]/div[1]/section/h2/button/span',
        '//*[@id="__next"]/div[1]/main/div[3]/section/div/div/ol/li[27]/div/article/div[2]/div[1]/section/h2/button/span',
        '//*[@id="__next"]/div[1]/main/div[3]/section/div/div/ol/li[35]/div/article/div[2]/div[1]/section/h2/button/span'
    ]
    
    otel_xpath_fiyat = [
        '//*[@id="__next"]/div[1]/main/div[3]/section/div/div/ol/li[3]/div/article/div[2]/div[2]/div[1]/div[2]/div/div/div/span',
        '//*[@id="__next"]/div[1]/main/div[3]/section/div/div/ol/li[27]/div/article/div[2]/div[2]/div[1]/div[2]/div/div/div/span',
        '//*[@id="__next"]/div[1]/main/div[3]/section/div/div/ol/li[35]/div/article/div[2]/div[2]/div[1]/div[2]/div/div/div/span'
    ]
    
    for ad_xpath, fiyat_xpath in zip(otel_xpath_ad, otel_xpath_fiyat):
        otel_data = fetch_hotel_data(driver, wait, ad_xpath, fiyat_xpath, sehir)
        hotels_info.append(otel_data)

# Close the driver
driver.quit()

# Convert the list to a DataFrame
df = pd.DataFrame(hotels_info, columns=['City', 'Hotel Name', 'Price'])
print(df)
