
from hashlib import sha256
import random

class Kazicilar:

    #def ___init__(self, name):
    #    self.name = name

    def SHA256(self,text):
        return sha256(text.encode("ascii")).hexdigest()

    def rastgele(self,sira, max_sira, ondeki_sifirlar_str, text):
        tekrar = 0
        while True:
            i = (random.randint(sira, max_sira))
            text_yeni = text + str(i)
            yeni_hash = self.islem(text_yeni, ondeki_sifirlar_str, tekrar, i)
            if yeni_hash is not None:
                return yeni_hash
            tekrar += 1     

    def sonsuz(self, sira, ondeki_sifirlar_str, text):
        tekrar = 0
        while True:
            text_yeni = text + str(sira)
            yeni_hash = self.islem(text_yeni, ondeki_sifirlar_str, tekrar, sira)
            if yeni_hash is not None:
                return yeni_hash
            sira += 1 
            tekrar += 1   

    def sirali(self, sira, max_sira, ondeki_sifirlar_str, text):
        tekrar = 0
        for i in range(sira, max_sira+1):
            text_yeni = text + str(i)
            yeni_hash = self.islem(text_yeni, ondeki_sifirlar_str, tekrar, i)
            if yeni_hash is not None:
                return yeni_hash
            tekrar += 1

    def islem(self, text, ondeki_sifirlar_str, tekrar, nonce):
        yeni_hash = self.SHA256(text)
        if yeni_hash.startswith(ondeki_sifirlar_str):
            print(f"Dongu {tekrar+1} islem yapti.")
            print(f"nonce {nonce} ile bulundu.")
            return yeni_hash