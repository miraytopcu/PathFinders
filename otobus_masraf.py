import math

def otobus_masraf(distance):
    koltuk_sayisi = 40
    
    def personel_ucreti():
        sofor = distance * 2 * 2
        gorevli = distance * 1.5
        return sofor + gorevli
    
    def ikram_servis():
        ikram_maliyeti = koltuk_sayisi * 30
        servis_maliyeti = koltuk_sayisi * 40
        return ikram_maliyeti + servis_maliyeti
    
    def otogar_masrafi():
        durulan_otogar_sayisi = math.floor(distance / 100)
        return durulan_otogar_sayisi * 550
    
    def bakimlar():
        yillik_kasko = 400000
        sigorta = 80000
        tek_lastik = 15000
        lastikler = tek_lastik * 6
        yilda_gidilen_km = 330000
        km_basina_bakim_masraflari = (yillik_kasko + sigorta + lastikler) / yilda_gidilen_km
        sefer_basi_bakim_masrafi = km_basina_bakim_masraflari * distance
        return sefer_basi_bakim_masrafi
    
    def yakit_masrafi():
        mazot_fiyati = 43.74
        litre = distance * 0.28
        return litre * mazot_fiyati
    
    toplam_masraf = personel_ucreti() + ikram_servis() + otogar_masrafi() + bakimlar() + yakit_masrafi()
    return toplam_masraf / koltuk_sayisi

print(otobus_masraf(329.84464001975505))


"""
1) Yakıt Masrafı: 100 kmde 25 litre mazot, km başı 0,25 (28)
+2) Personel Ücreti: 2 şoför ve 1 görevli, bir kaptan şoför kilometre başına 1.5 lira, görevli 1 lira kazanıyor
+3) Ikram ve Servis Maliyeti : Yolcu başına ikram maliyeti 25 lira, servis maliyeti ise 40 lira
4) Firma Katılım Ücreti : Bir otobüs sahibinin tek başına sefer düzenlemesi mümkün değil. Kamil Koç gibi, 
Pamukkale gibi firmaların filolarına dahil oluyorlar. Bu filolara dahil olmanın bedeli ise bilet fiyatının 
yaklaşık yüzde 25’i ile 30’unu firma ile paylaşmak anlamına geliyor.
+5) Otogar Çıkışları, Paralı Yollar: Tek bir otogara girip çıkmanın maliyeti 200 lira ile 700 lira arasında

+6) Bir otobüste yaklaşık 40 satılabilir koltuk var.
+7) Dikkat edilmesi gereken bir konu da finansman, kasko sigorta ve bakım onarım giderleri. Bugün yaş ve modele
göre değişmekle birlikte yıllık kasko gideri 400 bin lira civarında. Sigorta 80 bin lira seviyesinde. Tek bir
lastiğin fiyatı ise 15-16 bin liralarda.
8) 

"""








