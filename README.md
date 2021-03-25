# PythonBitcoinMinningExample
Python ile bitcoin madenciliği yapmak hakkında basit ve kısa bir örnek.

1-
  Aşağıdaki şekilde çalıştırın. Buradaki 4 rakamı zorluk seviyesidir. Hash kodunun ilk 4 hanesi 0 olacak demektir.
  0 ve 39000 ise 0 dan başla 39000 e kadar hashı bulmayı dene işlevi görür.
  python3.7 kazima.py 4 sirali 0 39000
  uyuglanadığında ekran çıktısı şu şekilde olacaktır.

  Kazima basladi
  Onceki Blok Numarasi 5
  Onceki Blok Hash 0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7
  Yeni Blok Numarasi 6
  Dongu 35153 islem yapti.
  nonce 35152 ile bulundu.
  Yeni hash: 0000ee46935727afd9e6936ee41a053a4fb94a0802613b66980ec7c7f41b54cb
  Kazima bitti. 0.1368389129638672 saniye surdu.

  Yukarıda Yeni hash i görüyorsanız minning başarılı demektir.
  
2-
  python3.7 kazima.py 4 sonsuz 0
  yada
  python3.7 kazima.py 4 sonsuz 1250
  
  bu kod ise o dan yada 1250 den başlayarak sonsuza kadar doğru hashi arayacak demektir.
  
3-
  python3.7 kazima.py 4 rastgele 15000 100000000000
  buda 15000 ile 100000000000 arasında sürekli random bir sayı üreterek hash i bulmaya çalışacaktır.
  
  
  
  
Zorluk Seviyesi: 4 olarak girildi ve gördüğünüz gibi 0.13 saniyede buldu. Şuanda bitcoin ağında istenen zorluk seviyesi 19 sıfırlıdır. 4 rakamını 6 ya çıkarırsak ne olur.

Ekran Çıktısı:

Kazima basladi
Onceki Blok Numarasi 5
Onceki Blok Hash 0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7
Yeni Blok Numarasi 6
Dongu 10911673 islem yapti.
nonce 10911672 ile bulundu.
Yeni hash: 000000cad2626734d99376019ccefeef975ee26bf6473d8a5c855c2de05a4783
Kazima bitti. 37.380290031433105 saniye surdu.


Görüldüğü üzere 37.3 saniye sürdü. 2021 yılı itibariyle zorkuk seviyesi 19 sıfırlıdır. Yani günümüz ev bilgisayarlarında bu doğru hashi bulmak yıllar süredbilir.
Ve sizin bu madeni çıkarmak için sadece 10 dakikanız var. Çünkü 10 dakikada bir yeni block üretilir ve madenciler bunu yüksek işlem gücü olan cihazlrında üretip erkenden ağa sunarlar.
bu durumda diğer madenciler 1 dakika içinde yeni hash i üretirse sizin taramayı durdurmanız gerekir.


Not:

  Yukarıdak 3 parametre test edebilmeniz için oluşturulmuştur. Çünkü doğru hash ı bulmak yıllar sürecek olsada rastgele deneme ile birkaç dakikada bulunaiblir.
  Kodların içinde göreceğiniz kazima.py içindeki Satır 30 ile 36 arasındaki el ile verdiğim Değişkenleri işleyerek bu hash i bulmaya çalışacaktır.
  Eğerki gerçek bir bitcoin ağında madencilik yapıyor olsanız oradaki değerler birkaç satır değil çok daha fazla olacaktır.
  Satır 30 ile 36 içindeki değerlere gelecek olursak.
  Madencinin Bitcoin adresi, bir önceki block hash i ve o süreçte gerçekleşmiş dünyadaki tüm transfler yer alacaktır.
