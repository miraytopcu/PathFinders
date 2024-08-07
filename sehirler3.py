import json
import math
from geopy.distance import geodesic

# km çevirmede hata var (sayısal)

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
        print("1- Şehir Bulma \n2 - Uzaklık Hesaplama")
        cikis = input("Çıkmak istiyorsan 'q' tuşla: ")
        if cikis == "q":
            break
        else:
            tercih = input("Tercihini tuşla: ")
            if tercih == "1":
                sehir_index = int(input("Şehir plakasını giriniz: ")) - 1
                result = get_sehir(sehir_index)
                print("Şehir adı:", result)
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
                print("2 şehir arası km: ", vincenty_distance(coord1, coord2))
                
    except ValueError:
        print("Geçersiz giriş. Lütfen bir sayı giriniz.")