import math
import json
from geopy.distance import geodesic

# JSONdan data çekme
with open('cities_of_turkey.json', 'r', encoding='utf-8') as file:
    veri = json.load(file)

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

def ucak_fiyati(distance):
    # km başına 3 tl
    ucak_bileti = math.ceil(distance * 3)
    return ucak_bileti

def ucus(sehir1, sehir2):
    olasilik1 = veri[sehir1]["havaalani"]
    olasilik2 = veri[sehir2]["havaalani"]
    regions = {"Ege" : "İzmir",
               "Akdeniz" : "Antalya",
               "Güneydoğu Anadolu" : "Gaziantep",
               "İç Anadolu" : "Ankara",
               "Doğu Anadolu" : "Malatya",
               "Marmara" : "İstanbul",
               "Karadeniz" : "Samsun"}
    if (olasilik1 == "+") and (olasilik2 == "+"):
        lat1, lat2 = get_enlem(sehir1, sehir2)
        lon1, lon2 = get_boylam(sehir1, sehir2)
                
        # Calculate distance
        coord1 = (lat1 , lon1)
        coord2 = (lat2 , lon2)
        # print("2 şehir arası km: ", vincenty_distance(coord1, coord2) , "\n")
        print(f"ucak bileti : {ucak_fiyati(vincenty_distance(coord1, coord2))}")
    else:
        if (olasilik1 == "-") and (olasilik2 == "+"):
            bolge1 = veri[sehir1]["region"]
            sehir_bolge = regions.get(bolge1)
            print(f"Bu şehirden kalkan uçak yok, {sehir_bolge} şehrinden uçağa binebilirsiniz.")
            secim = input("Seçimi onaylıyorsanız '1' otobüsü tercih ediyorsanız '2' tuşlayınız: ")
            if secim == "1":
                lat1, lat2 = get_enlem(sehir_bolge, sehir2)
                lon1, lon2 = get_boylam(sehir_bolge, sehir2)
                
                # Calculate distance
                coord1 = (lat1 , lon1)
                coord2 = (lat2 , lon2)
                # print("2 şehir arası km: ", vincenty_distance(coord1, coord2) , "\n")
                print(f"ucak bileti : {ucak_fiyati(vincenty_distance(coord1, coord2))}")
            elif secim == "2": 
                print("otobüs")
        pass
    # print(olasilik1 , olasilik2)

"""
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
print(f"ucak bileti : {ucak_fiyati(vincenty_distance(coord1, coord2))}")

"""

sehir_indexes = input("İki il plakasını arada boşluk bırakarak gir: ")
sehir1 = int(sehir_indexes.split()[0]) - 1
sehir2 = int(sehir_indexes.split()[-1]) - 1
ucus(sehir1 , sehir2)
