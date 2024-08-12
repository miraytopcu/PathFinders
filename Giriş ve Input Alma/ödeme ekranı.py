def odemeEkrani():
    # Kullanıcıya ödeme seçeneklerini sunma
    print("Lütfen ödeme yöntemini seçin:")
    print("1) Kredi Kartı (%2 komisyonlu)")
    print("2) Banka Kartı")
    print("3) Nakit Ödeme")
    print("4) Havale ile Ödeme (%5 indirimli)")

    # Ödeme türü seçimi
    odeme = input("\nSeçiminizi yapın (1, 2, 3 veya 4): ")

    # Toplam tutar tatil planları kodu yazıldıktan sonra oradan çekilebilir.
    toplam_tutar = float(input("Toplam tutar (TL): "))

    if odeme == '1':
        komisyon_orani = 0.02
        komisyonlu_tutar = toplam_tutar * (1 + komisyon_orani)
        print(f"\nSeçtiniz: Kredi Kartı ile Ödeme")
        print(f"Ödenecek Tutar (komisyonlu): {komisyonlu_tutar:.2f} TL")
        
    elif odeme == '2':
        print(f"\nSeçtiniz: Banka Kartı ile Ödeme")
        print(f"Ödenecek Tutar: {toplam_tutar:.2f} TL")
        
    elif odeme == '3':
        print(f"\nSeçtiniz: Nakit Ödeme")
        print(f"Ödenecek Tutar: {toplam_tutar:.2f} TL")
        
    elif odeme == '4':
        indirimli_tutar = toplam_tutar * 0.95
        print(f"\nSeçtiniz: Havale ile Ödeme")
        print(f"Ödenecek Tutar (indirimli): {indirimli_tutar:.2f} TL")
        
    else:
        print("\nGeçersiz seçim. Lütfen tekrar deneyin.")

# Ödeme ekranını başlat
odemeEkrani()
