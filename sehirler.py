import json
import math

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
    
def enlem_fark(sehir1, sehir2):
    enlem1 = float(veri[sehir1]["latitude"])
    enlem2 = float(veri[sehir2]["latitude"])
    return (enlem1, enlem2)

def boylam_fark(sehir1, sehir2):
    boylam1 = float(veri[sehir1]["longitude"])
    boylam2 = float(veri[sehir2]["longitude"])
    return (boylam1, boylam2)

def haversine_distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)*2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)*2
    c = 2 * math.asin(math.sqrt(a))
    
    # Radius of Earth in kilometers
    r = 6371.0
    
    # Calculate the distance
    distance = r * c
    return distance

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
                lat1, lat2 = enlem_fark(sehir1, sehir2)
                lon1, lon2 = boylam_fark(sehir1, sehir2)
                
                # Calculate distance
                distance = haversine_distance(lat1, lon1, lat2, lon2)
                print(f"Uzaklık: {distance:.2f} km")
    except ValueError:
        print("Geçersiz giriş. Lütfen bir sayı giriniz.")