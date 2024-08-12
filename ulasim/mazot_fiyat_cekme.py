from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

chromeOptions = Options()
chromeOptions.add_argument("--incognito")
chromeOptions.add_argument("--headless")

driver = webdriver.Chrome(options=chromeOptions)

driver.get("https://www.aytemiz.com.tr/akaryakit-fiyatlari/motorin-fiyatlari")
driver.implicitly_wait(5)


try:
    fiyat_bilgisi = driver.find_element("xpath", '//*[@id="fuel-price-table"]/tbody/tr[6]/td[3]').text
    print(fiyat_bilgisi)
except Exception as e:
    print(f"Hata oluştu: {e}")
    

driver.quit()  # WebDriver'ı kapat
