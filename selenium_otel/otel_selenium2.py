from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
# options.add_argument("--headless")  # Comment out headless mode for debugging

# Initialize the Chrome driver
driver = webdriver.Chrome(options=options)

codes = {"istanbul" : ["i%CC%87stanbul" , "288"],
         "ankara" : ["ankara" , "245"],
         "adana" : ["adana" , "236"]}

hotels_info = []

for sehir, bilgiler in codes.items():
    kod = bilgiler[0]
    sayi = bilgiler[1]
    # https://www.trivago.com.tr/tr/srl/otel-ankara-t%C3%BCrkiye?search=200-15245;dr-20240928-20240929-s;rc-1-1;so-3
    driver.get(f"https://www.trivago.com.tr/tr/srl/otel-{kod}-t%C3%BCrkiye?search=200-15{sayi};dr-20240928-20240929-s;rc-1-1;so-3")
    wait = WebDriverWait(driver, 10)
    
    otel_adi_1 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/main/div[3]/section/div/div/ol/li[3]/div/article/div[2]/div[1]/section/h2/button/span'))).text
    otel_fiyati_1 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/main/div[3]/section/div/div/ol/li[3]/div/article/div[2]/div[2]/div[1]/div[2]/div/div/div/span'))).text

    otel_adi_2 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/main/div[3]/section/div/div/ol/li[27]/div/article/div[2]/div[1]/section/h2/button/span'))).text
    otel_fiyati_2 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/main/div[3]/section/div/div/ol/li[27]/div/article/div[2]/div[2]/div[1]/div[2]/div/div/div/span'))).text

    otel_adi_3 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/main/div[3]/section/div/div/ol/li[35]/div/article/div[2]/div[1]/section/h2/button/span'))).text
    otel_fiyati_3 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/main/div[3]/section/div/div/ol/li[35]/div/article/div[2]/div[2]/div[1]/div[2]/div/div/div/span'))).text

    otel_1 = [otel_adi_1 , otel_fiyati_1]
    otel_2 = [otel_adi_2 , otel_fiyati_2]
    otel_3 = [otel_adi_3 , otel_fiyati_3]

    hotels_info.append(otel_1)
    hotels_info.append(otel_2)
    hotels_info.append(otel_3)


# Close the driver
driver.quit()

print(hotels_info)

df = pd.DataFrame(hotels_info, columns=['Hotel Name', 'Price'])
print(df)