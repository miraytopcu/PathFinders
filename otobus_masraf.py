"""
1) Yakıt Masrafı: 100 kmde 25 litre mazot
2) Personel Ücreti: 2 şoför ve 1 görevli, bir kaptan şoför kilometre başına 1.5 lira, görevli 1 lira kazanıyor
3) Ikram ve Servis Maliyeti : Yolcu başına ikram maliyeti 25 lira, servis maliyeti ise 40 lira
4) Firma Katılım Ücreti : Bir otobüs sahibinin tek başına sefer düzenlemesi mümkün değil. Kamil Koç gibi, 
Pamukkale gibi firmaların filolarına dahil oluyorlar. Bu filolara dahil olmanın bedeli ise bilet fiyatının 
yaklaşık yüzde 25’i ile 30’unu firma ile paylaşmak anlamına geliyor.
5) Otogar Çıkışları, Paralı Yollar: Tek bir otogara girip çıkmanın maliyeti 200 lira ile 700 lira arasında

6) Bir otobüste yaklaşık 40 satılabilir koltuk var.
7) Dikkat edilmesi gereken bir konu da finansman, kasko sigorta ve bakım onarım giderleri. Bugün yaş ve modele
göre değişmekle birlikte yıllık kasko gideri 400 bin lira civarında. Sigorta 80 bin lira seviyesinde. Tek bir
lastiğin fiyatı ise 15-16 bin liralarda.
8) 

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


