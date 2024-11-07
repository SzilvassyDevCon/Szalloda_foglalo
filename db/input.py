import queries

db = 'szalloda.db'

conn = queries.db_conn(db)

print("1) Szállodák parkolóval egy adott városban:")

varos_neve = input("Adja meg a várost: ")

parkolo_szalloda = queries.pyp_query1(conn, varos_neve)
print(parkolo_szalloda)

print("2) Étteremre szűrés szállodánként:")

szalloda_neve = input("Adja meg a szálloda nevét: ")

etterem_szalloda = queries.pyp_query2(conn, szalloda_neve)
print(etterem_szalloda)

print("3) Szobák száma egy adott szállodában:")

szalloda_neve2 = input("Adja meg a szállodát: ")

szoba_szalloda = queries.pyp_query3(conn, szalloda_neve2)
print(szoba_szalloda)

print("4) Foglalások listázása adott szállodában:")

szalloda_neve3 = input("Adja meg a szállodát: ")

foglalas_szalloda = queries.pyp_query4(conn, szalloda_neve3)
print(foglalas_szalloda)

print("5) Szállodák amelyekben már valaha történt foglalas:")

szalloda_neve4 = input("Adja meg a szállodát: ")

foglalas_szalloda2 = queries.pyp_query5(conn, szalloda_neve4)
print(foglalas_szalloda2)

print("6) Szállodák parkolóval egy adott városban:")

varos_neve2 = input("Adja meg a várost: ")

parkolo_varos = queries.pyp_query6(conn, varos_neve2)
print(parkolo_varos)

print("7) Átlagos ágyak egy adott szállodában")

szalloda_neve5 = input("Adja meg a szállodát: ")

agy_szalloda = queries.pyp_query7(conn, szalloda_neve5)
print(agy_szalloda)