import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

with open('cities_of_turkey.json', 'r' , encoding='utf-8') as file:
    veri = json.load(file)

def get_sehir(sehir_index):
    # Check if the index is within range
    if 0 <= sehir_index < len(veri):
        city_name = veri[sehir_index]["name"]
        # Capitalize if all letters are uppercase
        if city_name.isupper():
            return city_name.capitalize()
        else:
            return city_name
    else:
        return "Index out of range"
    
def enlem_fark(sehir1, sehir2):
    enlem1 = float(veri[sehir1]["latitude"])
    enlem2 = float(veri[sehir2]["latitude"])
    result = enlem1 - enlem2
    return abs(result)

def boylam_fark(sehir1, sehir2):
    boylam1 = float(veri[sehir1]["longitude"])
    boylam2 = float(veri[sehir2]["longitude"])
    result = boylam1 - boylam2
    return abs(result)

def uzaklik(enlem, boylam):
    toplam = (enlem ** 2) + (boylam ** 2)
    pisagor = math.sqrt(toplam)
    return pisagor 

# İşlemler
# KM fark için önce bir input al, o inputu " " dan split et, iki değişkene ata, enlemlerini al, birbirinden
# çıkarıp abs value al, aynı işlemler boylam içinde geçerli, sonra yeni def ile pisagor bul

while True: 
    try:
        print("1- Şehir Bulma \n2 - Uzaklık Hesaplama")
        cikis = input("çıkmak istiyorsan 'q' tuşla: ")
        if cikis == "q":
            break
        else:
            tercih = input("Tercihini tuşla: ")
            if tercih == "1":
                sehir_index = int(input("Şehir plakasını giriniz: ")) - 1
                result = get_sehir(sehir_index)
                print("Şehir adı:", result)
            elif tercih == "2":
                sehir_indexes = input("iki il plakasını arada boşluk bırakarak gir: ")
                sehir1 = int(sehir_indexes.split()[0])
                sehir2 = int(sehir_indexes.split()[-1])
                enlem = enlem_fark(sehir1, sehir2)
                boylam = boylam_fark(sehir1, sehir2)
                result = uzaklik(enlem, boylam)
                print("Uzaklık: " , result)
    except ValueError:
        print("Geçersiz giriş. Lütfen bir sayı giriniz.")