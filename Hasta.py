class Hasta:
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi):
        self.__hasta_no = hasta_no
        self.__ad = ad
        self.__soyad = soyad
        self.__dogum_tarihi = dogum_tarihi
        self.__hastalik = hastalik
        self.__tedavi = tedavi

    def hasta_no(self):
        return self.__hasta_no

    def hasta_ad(self):
        return self.__ad

    def hasta_soyad(self):
        return self.__soyad

    def dogum_tarihi(self):
        return self.__dogum_tarihi

    def hastalik(self):
        return self.__hastalik

    def tedavi(self):
        return self.__tedavi

    def tedavi_suresi_hesapla(self):
        # Tedavi süresi hesaplaması için örnek bir yöntem
        return "14 gün"  # Gerçek hesaplama burada yapılmalıdır

    def __str__(self):
        return f"Hasta No: {self.__hasta_no}, Adı: {self.__ad}, Soyadı: {self.__soyad}, Doğum Tarihi: {self.__dogum_tarihi}, Hastalık: {self.__hastalik}, Tedavi: {self.__tedavi}"
