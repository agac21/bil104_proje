class Personel:
    def __init__(self, personel_no, ad, soyad, departman, maas):
        self.__personel_no = personel_no
        self.__ad = ad
        self.__soyad = soyad
        self.__departman = departman
        self.__maas = maas

    # Get ve Set metotları
    @property
    def maas(self):
        return self.__maas

    @maas.setter
    def maas(self, yeni_maas):
        self.__maas = yeni_maas

    def personel_no(self):
        return self.__personel_no

    def ad(self):
        return self.__ad

    def soyad(self):
        return self.__soyad

    def departman(self):
        return self.__departman

    def maas(self):
        return self.__maas

    # __str__ metodu
    def __str__(self):
        return f"Personel No: {self.__personel_no}, Adı: {self.__ad}, Soyadı: {self.__soyad}, Departman: {self.__departman}, Maaş: {self.__maas} TL"
