import json
import math
 
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
    
def get_coordinates(sehir_index):
    # Şehrin koordinatlarını döndür
    enlem = float(veri[sehir_index]["latitude"])
    boylam = float(veri[sehir_index]["longitude"])
    return enlem, boylam

def haversine_distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
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
                lat1, lon1 = get_coordinates(sehir1)
                lat2, lon2 = get_coordinates(sehir2)
                
                # Calculate distance
                distance = haversine_distance(lat1, lon1, lat2, lon2)
                print(f"Uzaklık: {distance:.2f} km")
    except ValueError:
        print("Geçersiz giriş. Lütfen bir sayı giriniz.")
