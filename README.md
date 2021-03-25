# PythonBitcoinMinningExample
Python ile bitcoin madenciliği yapmak hakkında basit ve kısa bir örnek.
<br>
1-<br>
  Aşağıdaki şekilde çalıştırın. Buradaki 4 rakamı zorluk seviyesidir. Hash kodunun ilk 4 hanesi 0 olacak demektir.<br>
  0 ve 39000 ise 0 dan başla 39000 e kadar hashı bulmayı dene işlevi görür.<br>
  python3.7 kazima.py 4 sirali 0 39000<br>
  uyuglanadığında ekran çıktısı şu şekilde olacaktır.<br><br>

  Kazima basladi<br>
  Onceki Blok Numarasi 5<br>
  Onceki Blok Hash 0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7<br>
  Yeni Blok Numarasi 6<br>
  Dongu 35153 islem yapti.<br>
  nonce 35152 ile bulundu.<br>
  Yeni hash: 0000ee46935727afd9e6936ee41a053a4fb94a0802613b66980ec7c7f41b54cb<br>
  Kazima bitti. 0.1368389129638672 saniye surdu.<br><br>

  Yukarıda Yeni hash i görüyorsanız minning başarılı demektir.<br>
  
2-<br>
  python3.7 kazima.py 4 sonsuz 0<br>
  yada<br>
  python3.7 kazima.py 4 sonsuz 1250<br><br>
  
  bu kod ise o dan yada 1250 den başlayarak sonsuza kadar doğru hashi arayacak demektir.<br>
  
3-<br>
  python3.7 kazima.py 4 rastgele 15000 100000000000<br>
  buda 15000 ile 100000000000 arasında sürekli random bir sayı üreterek hash i bulmaya çalışacaktır.<br>
  
  
  
  
Zorluk Seviyesi: 4 olarak girildi ve gördüğünüz gibi 0.13 saniyede buldu. Şuanda bitcoin ağında istenen zorluk seviyesi 19 sıfırlıdır. 4 rakamını 6 ya çıkarırsak ne olur.<br>

Ekran Çıktısı:<br>

Kazima basladi<br>
Onceki Blok Numarasi 5<br>
Onceki Blok Hash 0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7<br>
Yeni Blok Numarasi 6<br>
Dongu 10911673 islem yapti.<br>
nonce 10911672 ile bulundu.<br>
Yeni hash: 000000cad2626734d99376019ccefeef975ee26bf6473d8a5c855c2de05a4783<br>
Kazima bitti. 37.380290031433105 saniye surdu.<br>


Görüldüğü üzere 37.3 saniye sürdü. 2021 yılı itibariyle zorkuk seviyesi 19 sıfırlıdır. Yani günümüz ev bilgisayarlarında bu doğru hashi bulmak yıllar süredbilir.
Ve sizin bu madeni çıkarmak için sadece 10 dakikanız var. Çünkü 10 dakikada bir yeni block üretilir ve madenciler bunu yüksek işlem gücü olan cihazlrında üretip erkenden ağa sunarlar.<br>
bu durumda diğer madenciler 1 dakika içinde yeni hash i üretirse sizin taramayı durdurmanız gerekir.<br><br>


Not:<br>

  Yukarıdak 3 parametre test edebilmeniz için oluşturulmuştur. Çünkü doğru hash ı bulmak yıllar sürecek olsada rastgele deneme ile birkaç dakikada bulunaiblir.
  Kodların içinde göreceğiniz kazima.py içindeki Satır 30 ile 36 arasındaki el ile verdiğim Değişkenleri işleyerek bu hash i bulmaya çalışacaktır.
  Eğerki gerçek bir bitcoin ağında madencilik yapıyor olsanız oradaki değerler birkaç satır değil çok daha fazla olacaktır.
  Satır 30 ile 36 içindeki değerlere gelecek olursak.<br><br>
  Madencinin Bitcoin adresi, bir önceki block hash i ve o süreçte gerçekleşmiş dünyadaki tüm transfler yer alacaktır.<br>


Önemli:<br>

Buradaki işlemler tamamen madencilik çalışma mantığı hakkında bilgi vermek içindir.<br>
Gerçek ağda yukarıdaki belirttiğim işlemlerin sayısı çok daha fazladır.
Aynı zamanda tüm değşikenleri ayarlamış ve doğru sıra ile hash üretmiş olsaydık bile, bitcoin madenciliği yapmak için bitcoin-core indirierek full node denilen bugune kadarki tüm işlemleri çekmiş ve doğrulamış olmanız gerekmektedir. Buda yaklaşık 400 GB ve birkaç hafta alacaktır. Tüm bu data olmadan değişkenler içinde Zorunlu İstenen verilere sahip olamazdınız. Aynı zamanda yeni hash i ürettiğinizde ve bunu ağdaki diğer madenciler ile doğru şekilde paylaştığınızda ve onlardan biri dahi bunu doğruladığında bitcoin üretmiş sayılacaksınız.
