import function
import sqlite3

database1 = sqlite3.connect("arabalar.db")

komut="CREATE TABLE IF NOT EXISTS arabalar(Marka text, Model text, Renk text, Km int)"
database1.commit()

veriler = "INSERT INTO arabalar  values ('Range Rover', 'Velar', 'Bej', 5000) "
function.veri_ekle()
database1.commit() 

sorgular = "Select * from arabalar"
function.veri_getir()
database1.commit()

msorgular = "select * from arabalar where Model = ?"
function.tek_kayit_getir("Nissan")
database1.commit()


database1.close()
