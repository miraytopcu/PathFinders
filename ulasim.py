import json
import math
from geopy.distance import geodesic
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

def otobus_masraf(distance):
    koltuk_sayisi = 40
    
    def personel_ucreti():
        sofor = distance * 1.5 * 2
        gorevli = distance * 1
        return sofor + gorevli
    
    def ikram_servis():
        ikram_maliyeti = koltuk_sayisi * 30
        servis_maliyeti = koltuk_sayisi * 40
        return ikram_maliyeti + servis_maliyeti
    
    def otogar_masrafi():
        durulan_otogar_sayisi = math.floor(distance / 150)
        return durulan_otogar_sayisi * 450
    
    def bakimlar():
        yillik_kasko = 400000
        sigorta = 80000
        tek_lastik = 15000
        lastikler = tek_lastik * 6
        yilda_gidilen_km = 330000
        km_basina_bakim_masraflari = (yillik_kasko + sigorta + lastikler) / yilda_gidilen_km
        sefer_basi_bakim_masrafi = km_basina_bakim_masraflari * distance
        return sefer_basi_bakim_masrafi
    
    def yakit_masrafi():
        chromeOptions = Options()
        chromeOptions.add_argument("--incognito")
        chromeOptions.add_argument("--headless")
        driver = webdriver.Chrome(options=chromeOptions)
        driver.get("https://www.aytemiz.com.tr/akaryakit-fiyatlari/motorin-fiyatlari")
        driver.implicitly_wait(5)

        try:
            fiyat_bilgisi = driver.find_element("xpath", '//*[@id="fuel-price-table"]/tbody/tr[6]/td[3]').text
            fiyat = float(fiyat_bilgisi.replace(',', '.'))
            litre = distance * 0.28
            return litre * fiyat
        except Exception as e:
            print(f"Hata oluştu: {e}")
            
        driver.quit()  
    
    def diger_masraflar():
        mtv = 13500
        aylik_kasko = 120000
        yilda_gidilen_km = 330000
        km_basina_kasko = (aylik_kasko * 12 ) / yilda_gidilen_km
        sefer_basina_kasko_mtv = (distance * km_basina_kasko) + ((mtv / yilda_gidilen_km) * distance)
        return sefer_basina_kasko_mtv
    
    
    toplam_masraf = personel_ucreti() + ikram_servis() + otogar_masrafi() + bakimlar() + yakit_masrafi() + diger_masraflar()
    amortisman = toplam_masraf
    return (toplam_masraf + amortisman) / koltuk_sayisi

# JSONdan data çekme
with open('cities_of_turkey.json', 'r', encoding='utf-8') as file:
    veri = json.load(file)

def get_sehir(sehir_index):
    # Girilen index list uzunluğuna uygun mu
    if 0 <= sehir_index < len(veri):
        city_name = veri[sehir_index]["name"]
        return city_name
    else:
        return "Index out of range"
    
def get_enlem(sehir1, sehir2):
    enlem1 = float(veri[sehir1]["latitude"])
    enlem2 = float(veri[sehir2]["latitude"])
    return (enlem1, enlem2)

def get_boylam(sehir1, sehir2):
    boylam1 = float(veri[sehir1]["longitude"])
    boylam2 = float(veri[sehir2]["longitude"])
    return (boylam1, boylam2)

def vincenty_distance(coord1, coord2):
    return geodesic(coord1, coord2).kilometers

while True: 
    try:
        print("1- Şehir Bulma \n2 - Uzaklık Hesaplama \n3- Bilet Fiyatı \n4- Çıkış(q)")
        tercih = input("Tercihini tuşla: ")
        
        if tercih == "q":
            break
        elif tercih == "1":
            sehir_index = int(input("Şehir plakasını giriniz: ")) - 1
            result = get_sehir(sehir_index)
            print("Şehir adı:", result , "\n")
        elif tercih == "2":
            sehir_indexes = input("İki il plakasını arada boşluk bırakarak gir: ")
            sehir1 = int(sehir_indexes.split()[0]) - 1
            sehir2 = int(sehir_indexes.split()[-1]) - 1
                
            # Get latitude and longitude
            lat1, lat2 = get_enlem(sehir1, sehir2)
            lon1, lon2 = get_boylam(sehir1, sehir2)
                
            # Calculate distance
            coord1 = (lat1 , lon1)
            coord2 = (lat2 , lon2)
            print("2 şehir arası km: ", vincenty_distance(coord1, coord2) , "\n")
        elif tercih == "3":
            sehir_indexes = input("İki il plakasını arada boşluk bırakarak gir: ")
            sehir1 = int(sehir_indexes.split()[0]) - 1
            sehir2 = int(sehir_indexes.split()[-1]) - 1
                
            # Get latitude and longitude
            lat1, lat2 = get_enlem(sehir1, sehir2)
            lon1, lon2 = get_boylam(sehir1, sehir2)
                
            # Calculate distance
            coord1 = (lat1 , lon1)
            coord2 = (lat2 , lon2)
            print(f"bilet ücreti: {otobus_masraf(vincenty_distance(coord1, coord2))} \n")
            
                
    except ValueError:
        print("Geçersiz giriş. Lütfen bir sayı giriniz.\n")