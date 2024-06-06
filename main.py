from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta
import pandas as pd


def main():
    personel1 = Personel(1, "Ayşe", "Yılmaz", "İdari", 5000)
    personel2 = Personel(2, "Ali", "Demir", "Destek", 4500)

    doktor1 = Doktor(3, "Canan", "Kara", "Kardiyoloji", 15000, "Kardiyolog", 10, "Şehir Hastanesi")
    doktor2 = Doktor(4, "Murat", "Çelik", "Nöroloji", 13500, "Nörolog", 8, "Devlet Hastanesi")
    doktor3 = Doktor(5, "Selin", "Taş", "Genel Cerrah", 16000, "Cerrah", 12, "Özel Hastane")

    hemsire1 = Hemsire(6, "Elif", "Gün", "Acil", 7000, 40, "Acil Tıp", "Devlet Hastanesi")
    hemsire2 = Hemsire(7, "Cem", "Arslan", "Yoğun Bakım", 7500, 45, "Yoğun Bakım", "Şehir Hastanesi")
    hemsire3 = Hemsire(8, "Zeynep", "Bulut", "Pediatri", 7200, 38, "Çocuk Sağlığı", "Özel Hastane")

    hasta1 = Hasta(101, "Burak", "Özdemir", "1992-05-14", "Astım", "İnhaler Tedavisi")
    hasta2 = Hasta(102, "Seda", "Akın", "1987-11-23", "Diyabet", "İnsülin Tedavisi")
    hasta3 = Hasta(103, "Kemal", "Sönmez", "2001-03-12", "Bronşit", "Antibiyotik Tedavisi")

    print(personel1)
    print(personel2)
    print(doktor1)
    print(doktor2)
    print(doktor3)
    print(hemsire1)
    print(hemsire2)
    print(hemsire3)
    print(hasta1)
    print(hasta2)
    print(hasta3)

    personeller = [personel1, personel2, doktor1, doktor2, doktor3, hemsire1, hemsire2, hemsire3, hasta1, hasta2,
                   hasta3]

    personel_dict = {
        "ID": [p.personel_no() if hasattr(p, 'personel_no') else p.hasta_no() for p in personeller],
        "Ad": [p.ad() if isinstance(p, Personel) else p.hasta_ad() for p in personeller],
        "Soyad": [p.soyad() if isinstance(p, Personel) else p.hasta_soyad() for p in personeller],
        "Departman": [p.departman() if hasattr(p, 'departman') else None for p in personeller],
        "Maas": [p.maas() if hasattr(p, 'maas') else None for p in personeller],
        "Uzmanlik": [p.uzmanlik() if hasattr(p, 'uzmanlik') else None for p in personeller],
        "Deneyim Yili": [p.deneyim_yili() if hasattr(p, 'deneyim_yili') else None for p in personeller],
        "Hastane": [p.hastane() if hasattr(p, 'hastane') else None for p in personeller],
        "Çalisma Saati": [p.calisma_saati() if hasattr(p, 'calisma_saati') else None for p in personeller],
        "Sertifika": [p.sertifika() if hasattr(p, 'sertifika') else None for p in personeller],
        "Hasta No": [p.hasta_no() if hasattr(p, 'hasta_no') else None for p in personeller],
        "Dogum Tarihi": [p.dogum_tarihi() if hasattr(p, 'dogum_tarihi') else None for p in personeller],
        "Hastalik": [p.hastalik() if hasattr(p, 'hastalik') else None for p in personeller],
        "Tedavi": [p.tedavi() if hasattr(p, 'tedavi') else None for p in personeller],
    }

    df = pd.DataFrame(personel_dict)

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    while True:
        try:
            print("Lütfen gerçekleştirmek istediğiniz işlem numarasını giriniz:")
            print("1. Boş olan değişken değerleri için 0 atayınız.")
            print("2. Doktorları uzmanlık alanlarına göre gruplandırarak toplam sayısını hesaplayınız ve yazdırınız.")
            print("3. 5 yıldan fazla deneyime sahip doktorların toplam sayısını bulunuz.")
            print("4. Hasta adına göre DataFrame’i alfabetik olarak sıralayınız ve yazdırınız.")
            print("5. Maaşı 7000 TL üzerinde olan personelleri bulunuz ve yazdırınız.")
            print("6. Doğum tarihi 1990 ve sonrası olan hastaları gösteriniz ve yazdırınız.")
            print("7. Var olan DataFrame’den ad, soyad, departman, maaş, uzmanlık, deneyim yılı,"
                  " hastalık, tedavi bilgilerini içeren yeni bir DataFrame elde ediniz ve yazdırınız.")
            print("0. Çıkış")
            secim = int(input("İşlem numarası (Çıkmak için 0): "))
            if secim == 0:
                break
            if secim == 1:
                df.fillna(0, inplace=True)
                print(df)
            elif secim == 2:
                uzmanlik_gruplari = df.groupby('Uzmanlik').size()
                print(uzmanlik_gruplari)
            elif secim == 3:
                deneyimli_doktorlar = df[(df['Deneyim Yili'] > 5) & (df['Uzmanlik'].notna())]
                print(len(deneyimli_doktorlar))
            elif secim == 4:
                hastalar_sirali = df[df['Hasta No'].notna()].sort_values('Ad')
                print(hastalar_sirali)
            elif secim == 5:
                yuksek_maasli_personeller = df[df['Maas'] > 7000]
                print(yuksek_maasli_personeller)
            elif secim == 6:
                yeni_hastalar = df[(df['Dogum Tarihi'] >= '1990-01-01') & (df['Hasta No'].notna())]
                print(yeni_hastalar)
            elif secim == 7:
                yeni_df = df[['Ad', 'Soyad', 'Departman', 'Maas', 'Uzmanlik', 'Deneyim Yili', 'Hastalik', 'Tedavi']]
                print(yeni_df)
            else:
                print("Geçersiz işlem numarası girdiniz.")

        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")


if __name__ == '__main__':
    main()
