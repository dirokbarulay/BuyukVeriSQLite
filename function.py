def listele(database1,liste):
    islem = database1.cursor()
    komut = liste
    islem.execute(komut)
    return islem

def veri_ekle(database1, ekleme):
    kayit = database1.cursor()
    veriler= ekleme
    kayit.execute(veriler)
    return kayit

def veri_silme(database1, silme):
    kayit2 = database1.cursor()
    veriler2= silme
    kayit2.execute(veriler2)
    return kayit2

def veri_guncelle(database1, guncelle):
    kayit3 = database1.cursor()
    veriler3= guncelle
    kayit3.execute(veriler3)
    return kayit3

def veri_getir(database1,sorgu):
    islem2 =database1.cursor()
    sorgular = sorgu
    islem2.execute(sorgular)
    return islem2

def tek_kayit_getir(Model, msorgu):
    islem3 = Model.cursor()
    msorgular = msorgu
    islem3.execute(islem3,(msorgular))
    return islem3
