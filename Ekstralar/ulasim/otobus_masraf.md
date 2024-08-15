"""
import requests
from bs4 import BeautifulSoup
import time

def veri_cek():
    url = 'https://www.petrolofisi.com.tr/akaryakit-fiyatlari'

    try:
        # Web sitesine istek gönderelim
        response = requests.get(url)
        if response.status_code == 200:
            # Sayfa kaynağını BeautifulSoup ile işleyelim
            soup = BeautifulSoup(response.content, 'html.parser')

            # İlgili veriyi bulalım (örneğin, benzin fiyatı)
            benzin_element = soup.find('span', {'class': 'benzin'})
            if benzin_element:
                benzin_fiyati = benzin_element.text.strip()
                return benzin_fiyati
            else:
                print("Benzin fiyatı bulunamadı.")
                return None
        else:
            print("Web sitesine erişim sağlanamadı.")
            return None
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return None

while True:
    # Veriyi çekelim
    benzin_fiyati = veri_cek()
    
    if benzin_fiyati:
        print(f"Güncel benzin fiyatı: {benzin_fiyati}")
    else:
        print("Veri çekilemedi.")

    # 1 saatte bir güncelleme yapmak için 3600 saniye bekleyelim
    time.sleep(3600)

"""