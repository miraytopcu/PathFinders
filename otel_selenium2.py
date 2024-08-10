from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
# options.add_argument("--headless")  # Comment out headless mode for debugging

# Initialize the Chrome driver
driver = webdriver.Chrome(options=options)

codes = {"İstanbul" : ["i%CC%87stanbul" , "288"],
         "Ankara" : ["ankara" , "245"],
         "Adana" : ["adana" , "236"]}

hotels_info = []

for sehir, bilgiler in codes.items():
    kod = bilgiler[0]
    sayi = bilgiler[1]
    driver.get(f"https://www.trivago.com.tr/tr/srl/otel-{kod}-t%C3%BCrkiye?search=200-15{sayi};dr-20240926-20240927-s;rc-1-1;so-4")
    wait = WebDriverWait(driver, 10)

    
    if sehir == "İstanbul" :
        otel_adi_1 = wait.until(EC.presence_of_element_located((By.XPATH, ''))).text
        otel_fiyati_1 = wait.until(EC.presence_of_element_located((By.XPATH, ''))).text

        otel_adi_2 = wait.until(EC.presence_of_element_located((By.XPATH, ''))).text
        otel_fiyati_2 = wait.until(EC.presence_of_element_located((By.XPATH, ''))).text

        otel_adi_3 = wait.until(EC.presence_of_element_located((By.XPATH, ''))).text
        otel_fiyati_3 = wait.until(EC.presence_of_element_located((By.XPATH, ''))).text

        otel_1 = [otel_adi_1 , otel_fiyati_1]
        otel_2 = [otel_adi_2 , otel_fiyati_2]
        otel_3 = [otel_adi_3 , otel_fiyati_3]

    elif sehir == "Ankara" :
        otel_adi_1 = wait.until(EC.presence_of_element_located((By.XPATH, ''))).text
        otel_fiyati_1 = wait.until(EC.presence_of_element_located((By.XPATH, ''))).text

        otel_adi_2 = wait.until(EC.presence_of_element_located((By.XPATH, ''))).text
        otel_fiyati_2 = wait.until(EC.presence_of_element_located((By.XPATH, ''))).text

        otel_adi_3 = wait.until(EC.presence_of_element_located((By.XPATH, ''))).text
        otel_fiyati_3 = wait.until(EC.presence_of_element_located((By.XPATH, ''))).text

        otel_1 = [otel_adi_1 , otel_fiyati_1]
        otel_2 = [otel_adi_2 , otel_fiyati_2]
        otel_3 = [otel_adi_3 , otel_fiyati_3]

    hotels_info.append(otel_1)
    hotels_info.append(otel_2)
    hotels_info.append(otel_3)


# Close the driver
driver.quit()

print(hotels_info)
