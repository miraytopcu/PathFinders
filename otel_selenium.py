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

# Open the website
driver.get("https://www.trivago.com.tr/tr/lm/otel-i%CC%87stanbul-t%C3%BCrkiye?search=200-15288;dr-20240813-20240814-s;rc-1-1")

# Set up WebDriverWait
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds for elements to be present

try:
    # Wait for the hotel name to be present
    ist_otel1_adi_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/main/div[3]/section/div/div/ol/li[1]/div/article/div[2]/div[1]/section/h2/button/span')))
    ist_otel1_adi = ist_otel1_adi_element.text  # Extract the text of the element

    # Wait for the hotel price to be present
    ist_otel1_fiyati_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/main/div[3]/section/div/div/ol/li[1]/div/article/div[2]/div[2]/div[1]/div[2]/div/div/div/span')))
    ist_otel1_fiyati = ist_otel1_fiyati_element.text  # Extract the text of the element

    # Wait for the hotel name to be present
    ist_otel2_adi_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/main/div[3]/section/div/div/ol/li[4]/div/article/div[2]/div[1]/section/h2/button/span')))
    ist_otel2_adi = ist_otel2_adi_element.text  # Extract the text of the element

    # Wait for the hotel price to be present
    ist_otel2_fiyati_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/main/div[3]/section/div/div/ol/li[4]/div/article/div[2]/div[2]/div[1]/div[2]/div/div/div/span')))
    ist_otel2_fiyati = ist_otel2_fiyati_element.text  # Extract the text of the element

    # Wait for the hotel name to be present
    ist_otel3_adi_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/main/div[3]/section/div/div/ol/li[5]/div/article/div[2]/div[1]/section/h2/button/span')))
    ist_otel3_adi = ist_otel3_adi_element.text  # Extract the text of the element

    # Wait for the hotel price to be present
    ist_otel3_fiyati_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/main/div[3]/section/div/div/ol/li[5]/div/article/div[2]/div[2]/div[1]/div[2]/div/div/div/span')))
    ist_otel3_fiyati = ist_otel3_fiyati_element.text  # Extract the text of the element

    ist_hotels = {ist_otel1_adi : ist_otel1_fiyati ,
                  ist_otel2_adi : ist_otel2_fiyati , 
                  ist_otel3_adi : ist_otel3_fiyati}

    # Print the extracted values
    print("Hotel Name:", ist_otel1_adi)
    print("Hotel Price:", ist_otel1_fiyati)
    print(ist_hotels)

finally:
    # Close the driver
    driver.quit()
