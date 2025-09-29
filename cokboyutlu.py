tcdd_yolcu_verisi = []


# tcdd garları
sirkeci_gari = []
ankara_gari = []
alsancak_gari = []


tren1 = {
    "vagon1":{
        "musteri1" : {
            "adi":"Melikşah",
            "yeri":32
        },
        "musteri2" : {
            "adi":"Arda",
            "yeri":30
        }
    }

}
tren2 = {
    "vagon1":{
        "musteri1" : {
            "adi":"Erdinç",
            "yeri":32
        },
        "musteri2" : {
            "adi":"Levent",
            "yeri":30
        }
    }


}

sirkeci_gari.append(tren1)
alsancak_gari.append(tren2)


tcdd_yolcu_verisi.append(sirkeci_gari)
tcdd_yolcu_verisi.append(ankara_gari)
tcdd_yolcu_verisi.append(alsancak_gari)


# print(tcdd_yolcu_verisi)
# print(tcdd_yolcu_verisi[0])
# print(tcdd_yolcu_verisi[0][0]["vagon1"])
# print(tcdd_yolcu_verisi[0][0]["vagon1"]["musteri1"])
print(tcdd_yolcu_verisi[0][0]["vagon1"]["musteri1"]["adi"])
print(tcdd_yolcu_verisi[0][0]["vagon1"]["musteri1"]["yeri"])
