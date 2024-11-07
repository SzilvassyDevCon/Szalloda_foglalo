import queries

db = 'szalloda.db'

conn = queries.db_conn(db)

print("1) Mely szállodák rendelkeznek parkolóval?")
parkolo_szalloda = queries.query1(conn)
print(parkolo_szalloda)

print("2) Mely szállodáknak van étterme?")
etterem_szalloda = queries.query2(conn)
print(etterem_szalloda)

print("3) Hány szoba van szállodánként?")
szobak_szama = queries.query3(conn)
print(szobak_szama)

print("4) Hány foglalás történt szállodánként?")
foglalas_szalloda = queries.query4(conn)
print(foglalas_szalloda)

print("5) Hány szálloda van ahol, legalább egy szobát valaha lefoglaltak.")
valid_foglalas = queries.query5(conn)
print(valid_foglalas)

print("6) Mely városokban található olyan szállodák, amelyekhez parkoló is tartozik?")
varos_szalloda_parkolo = queries.query6(conn)
print(varos_szalloda_parkolo)

print("7) Mi az átlagos ágyak száma a szállodák szobáiban?")
avg_agyak = queries.query7(conn)
print(avg_agyak)




