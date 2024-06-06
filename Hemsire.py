from Personel import Personel


class Hemsire(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane

    def maas_arttir(self, oran):
        self.maas *= (1 + oran / 100)

    def calisma_saati(self):
        return self.__calisma_saati

    def sertifika(self):
        return self.__sertifika

    def hastane(self):
        return self.__hastane

    def __str__(self):
        return super().__str__() + f", Çalışma Saati: {self.__calisma_saati}, Sertifika: {self.__sertifika}, Hastane: {self.__hastane}"
