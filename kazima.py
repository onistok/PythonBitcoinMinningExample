
import time
import sys
import os
import platform
from kazicilar import Kazicilar

try:
    sifir_adeti = int(sys.argv[1])
    sira = int(sys.argv[3])
except:
    print ('Degerler yanlis girildi. 1,3 ve 4 sirasindaki argumentler Integer Olmali!')
    sys.exit()

kazima_sekli = sys.argv[2]

if kazima_sekli != "sonsuz":
    try:
        max_sira = int(sys.argv[4])
    except:
        print ('4. siradaki argument girilmedi! max_sira')
        sys.exit()

if platform.system() == "Windows":
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')


blok_numarasi = 5
madenci = 'kjsdkfjsdkljfkjsdkljfklds'
onceki_hash = '0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7'
transferler='''
    Ugur Deneme->Onur Deneme->35,
    Dursun Deneme->Ahmet Deneme->10,
    Mehmet Deneme->Samet Deneme->14
    '''


if __name__=='__main__':
    kazima = Kazicilar()
    ondeki_sifirlar_str = '0'*sifir_adeti
    ilk_zaman = time.time()

    clear()

    print("Kazima basladi")
    print(f"Onceki Blok Numarasi {blok_numarasi}")
    print(f"Onceki Blok Hash {onceki_hash}")
    print(f"Yeni Blok Numarasi {blok_numarasi+1}")

    text = str(blok_numarasi) + transferler + onceki_hash + madenci
    if kazima_sekli == "sonsuz":
        yeni_hash = kazima.sonsuz(sira, ondeki_sifirlar_str, text)
    elif kazima_sekli == "sirali":
        yeni_hash = kazima.sirali(sira, max_sira, ondeki_sifirlar_str, text)
    elif kazima_sekli == "rastgele":
        yeni_hash = kazima.rastgele(sira, max_sira, ondeki_sifirlar_str, text) 
    else:
        print ("Kazima Sekli Dogru Girilmeli")
        sys.exit()

    gecen_zaman = str((time.time() - ilk_zaman))
    if yeni_hash is not None:
        print(f"Yeni hash: {yeni_hash}")
    else:
        print(f"Hash Bulunamadi! Dongu: {max_sira}")

    print(f"Kazima bitti. {gecen_zaman} saniye surdu.")      