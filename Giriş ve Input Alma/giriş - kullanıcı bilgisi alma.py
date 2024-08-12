def pathFinders():
    # Kullanıcıdan bilgileri alma
    ad = input("Adınız: ")
    soyad = input("Soyadınız: ")
    adres = input("Adresiniz: ")
    sehir = input("Yaşadığınız Şehir: ")
    yas = int(input("Yaşınız: "))

    # Kullanıcıyı karşılama mesajı
    print(f"\nMerhaba {ad} {soyad}, PathFinders'a hoş geldiniz!")
    print(f"{sehir} şehrindeki adresinize uygun tatil önerileri sunacağız.\n")

    # İşlem türü seçimi
    print("Lütfen yapmak istediğiniz işlemi seçin:")
    print("1) Tatil yapmak istediğim şehir kesin")
    print("2) Bir kategoriye göre tatil yapmak istiyorum (Kültürel, Lezzet, Deniz, Tur)")
    print("3) Şu kadar bütçem var, nerede tatil yapabilirim?")
    
    islem = input("\nSeçiminizi yapın (1, 2 veya 3): ")
    
    if islem == '1':
        print("\nSeçtiniz: Tatil yapmak istediğim şehir kesin")
        # Bu seçeneğe göre yapılacak işlemleri burada tanımlanacak.
    elif islem == '2':
        print("\nSeçtiniz: Bir kategoriye göre tatil yapmak istiyorum")
        # Bu seçeneğe göre yapılacak işlemleri burada tanımlanacak.
    elif islem == '3':
        print("\nSeçtiniz: Şu kadar bütçem var, nerede tatil yapabilirim?")
        # Bu seçeneğe göre yapılacak işlemleri burada tanımlanacak.
    else:
        print("\nGeçersiz seçim. Lütfen tekrar deneyin.")

# Uygulamayı başlat
pathFinders()
