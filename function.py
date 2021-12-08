def listele(database1,liste):
    islem = database1.cursor()
    komut = liste
    islem.execute(komut)
    return islem

def veri_ekle(database1, ekleme):
    kayit = database1.cursor()
    veriler= ekleme
    kayit.execute(kayit)
    return kayit

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
