import json
import math
from geopy.distance import geodesic
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class Ulasim:
    def __init__(self):
        self.sehirler = []  # Şehir listesini tutmak için boş bir liste oluşturduk

    @staticmethod
    def distance():
        # JSON dosyasından verileri çekme
        with open('cities_of_turkey.json', 'r', encoding='utf-8') as file:
            veri = json.load(file)

        # Kullanıcıdan şehir isimlerini alıp işleme
        input_str = input("İki şehir arasında boşluk bırakarak isimleri girin: ")
        sehirler = input_str.split()

        # Şehir isimlerini büyük harfle başlayıp kalanı küçük olacak şekilde düzenleme
        sehirler = [sehir.capitalize() for sehir in sehirler]
        lats = []   # Girilen inputtaki şehrin enlem bilgisi
        longs = []  # Girilen inputtaki şehrin boylam bilgisi
        for sehir in sehirler:
            if sehir.startswith("I"):
                sehir = sehir.replace("I", "İ")    # izmir - Izmir değil İzmir olsun
            found = False
            for data in veri:
                if data["name"] == sehir:
                    lat = data['latitude']
                    long = data['longitude']
                    lats.append(lat)
                    longs.append(long)
                    found = True
                    break
            if not found:
                print(f"{sehir} adlı şehir veri setinde bulunamadı.")
        
        if len(lats) >= 2 and len(longs) >= 2:        # Listede en az iki şehir olduğunu kontrol etmek için
            coord1 = (lats[0], longs[0])
            coord2 = (lats[1], longs[1])
            return int(geodesic(coord1, coord2).kilometers)    # Geodesic kütüphanesi iki koordinat arası mesafeyi hesaplar
        else:
            return "İki şehir arasında mesafe hesaplanamadı."

    def otobus(self):
        distance = self.distance()
        koltuk_sayisi = 40

        def personel_ucreti():
            sofor = distance * 1.5 * 2     # 2 sofor var, km başı 1.5 tl
            gorevli = distance * 1
            return sofor + gorevli

        def ikram_servis():
            ikram_maliyeti = koltuk_sayisi * 30
            servis_maliyeti = koltuk_sayisi * 40
            return ikram_maliyeti + servis_maliyeti

        def otogar_masrafi():
            durulan_otogar_sayisi = math.floor(distance / 150)     # 150 kmde bir otogarda duruyor ve her durduğu otogarda 450 harcıyor
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

        def yakit_masrafi():       # Mazot fiyatları sürekli güncellendiği için seleniumdan xpath kullanarak veriyi aldık
            chromeOptions = Options()
            chromeOptions.add_argument("--incognito")
            chromeOptions.add_argument("--headless")
            driver = webdriver.Chrome(options=chromeOptions)
            driver.get("https://www.aytemiz.com.tr/akaryakit-fiyatlari/motorin-fiyatlari")
            driver.implicitly_wait(5)     # sitenin açılması için bekleme süresi

            try:
                fiyat_bilgisi = driver.find_element("xpath", '//*[@id="fuel-price-table"]/tbody/tr[6]/td[3]').text
                fiyat = float(fiyat_bilgisi.replace(',', '.'))
                litre = distance * 0.28
                return litre * fiyat
            except Exception as e:
                print(f"Hata oluştu: {e}")
            
            driver.quit()  

        def diger_masraflar():
            mtv = 13500     # motorlu taşıtlar vergisi 
            aylik_kasko = 120000
            yilda_gidilen_km = 330000
            km_basina_kasko = (aylik_kasko * 12 ) / yilda_gidilen_km
            sefer_basina_kasko_mtv = (distance * km_basina_kasko) + ((mtv / yilda_gidilen_km) * distance)
            return sefer_basina_kasko_mtv
        
        toplam_masraf = personel_ucreti() + ikram_servis() + otogar_masrafi() + bakimlar() + yakit_masrafi() + diger_masraflar()
        amortisman = toplam_masraf     # kaarda amortisman içinde
        return (toplam_masraf + amortisman) / koltuk_sayisi
    
    def load_cities_and_regions(self):
        # Load cities and regions from the JSON file
        with open('cities_of_turkey.json', 'r', encoding='utf-8') as file:
            veri = json.load(file)
        
        self.sehirler = [data["name"] for data in veri]
        self.sehir_regionleri = {data["name"]: data["region"] for data in veri}
    
    def ucak(self):
        # JSON dosyasından verileri çekme
        with open('cities_of_turkey.json', 'r', encoding='utf-8') as file:
            veri = json.load(file)

        # Kullanıcının girdiği şehir isimlerini al
        input_str = input("İki şehir arasında boşluk bırakarak isimleri girin: ")
        sehirler = input_str.split()
        sehirler = [sehir.capitalize() for sehir in sehirler]

        # Ensure cities and regions data is loaded
        if not self.sehirler or not self.sehir_regionleri:
            self.load_cities_and_regions()

        # Bölgeler
        regions = {
            "Ege": "İzmir",
            "Akdeniz": "Antalya",
            "Güneydoğu Anadolu": "Gaziantep",
            "İç Anadolu": "Ankara",
            "Doğu Anadolu": "Malatya",
            "Marmara": "İstanbul",
            "Karadeniz": "Samsun"
        }

        havaalani_var = False
        ucak_bileti = 0

        for sehir in sehirler:
            found = False
            for data in veri:
                if data["name"] == sehir:
                    if data["havaalani"] == "+":
                        havaalani_var = True
                        distance = self.distance()  # Mesafeyi hesapla
                        ucak_bileti = math.ceil(distance * 3)  # km başına 3 TL
                    else:
                        print(f"{sehir} adlı şehirde havaalanı bulunmamaktadır!")
                        bolge = self.sehir_regionleri.get(sehir, "Bilinmeyen Bölge")
                        sehir_bolge = regions.get(bolge, "Bilinmeyen Bölge")
                        print(f"Bu şehirden kalkan uçak yok, {sehir_bolge} şehrinden uçağa binebilirsiniz.")
                    found = True
                    break
            if not found:
                print(f"{sehir} adlı şehir veri setinde bulunamadı.")

        if not havaalani_var:
            print("Belirtilen şehirlerde havaalanı bulunmamaktadır.")

        return ucak_bileti  # Return the calculated ucak_bileti value


# Ulasim sınıfından bir örnek oluşturalım
deneme1 = Ulasim()

# distance metodunu çağıralım
bilet_fiyati = deneme1.otobus()
ucak_bileti = deneme1.ucak()
print(f"Bilet fiyatı: {bilet_fiyati}")
print(f"Bilet fiyatı: {ucak_bileti}")

