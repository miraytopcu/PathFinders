tofrom = input("Sırasıyla çıkmak ve gitmek istediğiniz illeri arada boşluk karakteri kullanarak giriniz: ")
tofromx = tofrom.split()
to_city = tofromx[0]
from_city = tofromx[1]

num_person = int(input("Katılacak kişi sayısını giriniz: "))
num_day = int(input("Kalınacak gece sayısını giriniz: "))
rehber = input("Rehber hizmeti istiyorsanız 'e' istemiyorsanız 'h' tuşlayınız: ")

if rehber == "e":
    rehber_tercih = True
ulasim_tercih = input("Otobüsle yolculuk yapmak istiyorsanız 'o' uçakla yolculuk yapmak istiyorsanız 'u' tuşlayınız: ")
if ulasim_tercih == "o":
    # invoke otobus
    pass
elif ulasim_tercih == "u":
    # invoke ucak
    pass

butce = 1000
max_butce = float(input("Tatil için ayırabileceğiniz max bütçe miktarını giriniz: "))

if butce > max_butce:
    print(f"Aştın!", butce - max_butce , "lira emin misin?")