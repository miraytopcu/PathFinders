import json
import math
from geopy.distance import geodesic
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class Ulasim:
    def __init__(self, from_city, to_city):
        self.sehirler = []  # Şehir listesini tutmak için boş bir liste oluşturduk
        self.from_city = from_city
        self.to_city = to_city

    # @staticmethod
    def distance(self):
        # JSON dosyasından verileri çekme
        with open('cities_of_turkey.json', 'r', encoding='utf-8') as file:
            veri = json.load(file)

        # Şehir isimlerini büyük harfle başlayıp kalanı küçük olacak şekilde düzenleme
        sehirler = [self.from_city.capitalize() , self.to_city.capitalize()]
        lats = []   # Girilen inputtaki şehrin enlem bilgisi
        longs = []  # Girilen inputtaki şehrin boylam bilgisi
        for sehir in sehirler:
            # güncelle İğdır
            if sehir == "Istanbul":
                sehir = sehir.replace("I", "İ")
            elif sehir == "Izmir":
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
        return int((toplam_masraf + amortisman) / koltuk_sayisi)
    
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
        sehirler = [self.to_city.capitalize() , self.from_city.capitalize()]
        if sehirler[0] == "Istanbul":
            sehirler[0] = sehirler[0].replace("I", "İ")
        elif sehirler[1] == "Istanbul":
            sehirler[1] = sehirler[1].replace("I", "İ")
        elif sehirler[0] == "Izmir":
            sehirler[0] = sehirler[0].replace("I", "İ")
        elif sehirler[1] == "Izmir":
            sehirler[1] = sehirler[1].replace("I", "İ")

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

        # ucak_bileti = 0

        for data in veri:
            if data["name"] == sehirler[0]:
                hava1 = data["havaalani"]
            if data["name"] == sehirler[1]:
                hava2 = data["havaalani"]

        if hava1 == "+" and hava2 == "+":
            distance = self.distance()  # Mesafeyi hesapla
            ucak_bileti = math.ceil(distance * 3)  # km başına 3 TL
            return ucak_bileti
        
        elif hava1 == "-" and hava2 == "+":
            bolge = self.sehir_regionleri.get(sehirler[0], "Bilinmeyen Bölge")
            sehir_bolge = regions.get(bolge, "Bilinmeyen Bölge")
            print(f"{sehirler[0]} adlı şehirde havaalanı bulunmamaktadır! {sehir_bolge} şehrinden uçağa binebilirsiniz.")
            secim = input(f"Aktarmalı gitmek isterseniz 'e', yolculuğu otobüsle yapmak isterseniz 'h' tuşlayınız: ")
            if secim == "h":
                otobus_fiyat = self.otobus()
                return otobus_fiyat
            elif secim == "e":
                self.from_city = sehirler[0]
                self.to_city = sehir_bolge
                otobus_fiyat = self.otobus()
                self.from_city = sehir_bolge
                self.to_city = sehirler[1]
                distance = self.distance()
                ucak_fiyat = math.ceil(distance * 3)
                return otobus_fiyat + ucak_fiyat
            else:
                return f"Tercihini gözden geçir!"
            
        elif hava1 == "+" and hava2 == "-":
            bolge = self.sehir_regionleri.get(sehirler[1], "Bilinmeyen Bölge")
            sehir_bolge = regions.get(bolge, "Bilinmeyen Bölge")
            print(f"{sehirler[1]} adlı şehirde havaalanı bulunmamaktadır! {sehir_bolge} şehrinden uçağa binebilirsiniz.")
            secim = input(f"Aktarmalı gitmek isterseniz 'e', yolculuğu otobüsle yapmak isterseniz 'h' tuşlayınız: ")
            if secim == "h":
                otobus_fiyat = self.otobus()
                return otobus_fiyat
            elif secim == "e":
                self.from_city = sehirler[0]
                self.to_city = sehir_bolge
                distance = self.distance()
                ucak_fiyat = math.ceil(distance * 3)
                self.from_city = sehir_bolge
                self.to_city = sehirler[1]
                otobus_fiyat = self.otobus()
                return otobus_fiyat + ucak_fiyat
            else:
                return f"Tercihini gözden geçir!"
            
        elif hava1 == "-" and hava2 == "-":
            bolge1 = self.sehir_regionleri.get(sehirler[0], "Bilinmeyen Bölge")
            sehir_bolge1 = regions.get(bolge1, "Bilinmeyen Bölge")
            bolge2 = self.sehir_regionleri.get(sehirler[1], "Bilinmeyen Bölge")
            sehir_bolge2 = regions.get(bolge2, "Bilinmeyen Bölge")
            print(f"{sehirler[0]} adlı şehirde havaalanı bulunmamaktadır! {sehir_bolge1} şehrinden uçağa binebilirsiniz.")
            print(f"{sehirler[1]} adlı şehirde havaalanı bulunmamaktadır! {sehir_bolge2} şehrinden uçağa binebilirsiniz.")
            secim = input(f"Aktarmalı gitmek isterseniz 'e', yolculuğu otobüsle yapmak isterseniz 'h' tuşlayınız: ")
            if secim == "h":
                otobus_fiyat = self.otobus()
                return otobus_fiyat
            elif secim == "e":
                self.from_city = sehirler[0]
                self.to_city = sehir_bolge1
                otobus_fiyat1 = self.otobus()
                self.from_city = sehir_bolge1
                self.to_city = sehir_bolge2
                distance = self.distance()
                ucak_fiyat = math.ceil(distance * 3)
                self.from_city = sehir_bolge
                self.to_city = sehirler[1]
                otobus_fiyat2 = self.otobus()
                return otobus_fiyat1 + ucak_fiyat + otobus_fiyat2
            else:
                return f"Tercihini gözden geçir!"
            
        else:
            return f"Tercihini gözden geçir!!!"
        

tofrom = input("Sırasıyla çıkmak ve gitmek istediğiniz illeri arada boşluk karakteri kullanarak giriniz: ")
tofromx = tofrom.split()
to_city = tofromx[0]
from_city = tofromx[1]
# Ulasim sınıfından bir örnek oluşturalım
deneme1 = Ulasim(from_city, to_city)

ulasim_tercih = input("Otobüsle yolculuk yapmak istiyorsanız 'o' uçakla yolculuk yapmak istiyorsanız 'u' tuşlayınız: ")
if ulasim_tercih == "o":
    # invoke otobus
    bilet_fiyati = deneme1.otobus()
    print(f"Bilet fiyatı: {bilet_fiyati}")
elif ulasim_tercih == "u":
    # invoke ucak
    ucak_bileti = deneme1.ucak()
    print(ucak_bileti)
