# PathFinders
Path Finders, YetGen Core Python programının bitirme projesi olup 2 haftada geliştirilmiştir.

### Geliştiriciler: 
- Miray Topcu
- İrem Kasar
- Ahmet Demirbaş
- Ömer Oral

Path Finders, kullanıcısı için tatile giderken ulaşım ve otel masraflarını hesaplayarak bütçe dostu ve pratik bir tatil planlama süreci oluşturur.

Program 2 ana seçenek üzerinden ilerliyor.

1) Kullanıcı gitmek istediği lokasyondan emindir.
   - Programa input olarak kişi sayısı, kaç gece konaklama olunacağı, rehber hizmeti istenip istenmediği, tatile ayırılabilecek maksimum bütçe miktarı ve yaşanılan şehir girilir.
   - Daha sonra kullanıcın tatil lokasyonu kesin olduğu için kendisine gitmek istenilen şehir sorulur.
   - Ardından ulaşım için otobüs mü yoksa uçak mı tercih edildiği sorulur.
   - Otobüs tercih edilirse iki konum arasındaki uzaklık enlem ve boylam bilgileri üzerinden hesaplanıp kilometre cinsine çevrilir, sonrasında otobüs biletini etkileyen diğer parametreler çalışır ve kullanıcıya bilet fiyatı sunulur. (Not: Bu kısımda mazot fiyatları sürekli güncellendiği için selenium kullandık, bundan dolayı veri internetten çekildiği için çok az bir yavaşlama söz konusu.)
   - Uçak tercih edilirse her iki şehirde de havaalanlarının varlığı kontrol edilir. Eğer varsa uçak fiyatı hesaplanır. Bir tanesinde bile olmama durumunda kullanıcıya kullanabileceği en yakın havaalanının olduğu şehir belirtilir, aktarmalı mı gitmek ister yoksa tercihini otobüsle mi değiştirmek istediği sorulur. Tercihini aktarmalı olarak düzeltirse hem havaalanı olan şehirler arasındaki uçak fiyatı hem de havaalanı olan ve olmayan şehir arasındaki otobüs fiyatı hesaplanır ve toplanır.
   - Daha sonrasında sıra otel tercihlerine gelir, gitmek istenilen şehirdeki ucuz, orta, pahalı fiyatlı birer otel ve bir kamp alanı kullanıcıya ad, adres, telefon ve fiyat bilgileriyle sunulur ve bu dört seçenek arasından tercih yapılması istenir. Otel fiyatı da kişi ve gece sayısıyla çarpılarak toplam bütçeye eklenir.
   - kampanya ödeme maxbutce
2) Kullanıcı gitmek istediği lokasyondan emin değildir, kategoriler üzerinden tercih yapıp programın ona öneride bulunmasını istiyordur.
