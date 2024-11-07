import sqlite3
from pypika import Query, Table


def db_conn(path):
    conn = sqlite3.connect(path)
    return conn

def query1(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT Szalloda.szalloda, szalloda_parkolo.parkoloID FROM Szalloda INNER JOIN szalloda_parkolo ON szalloda_parkolo.szallodaID = szalloda.id")
    return cursor.fetchall()

def query2(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT Szalloda.szalloda, etterem.tipus FROM Szalloda INNER JOIN szalloda_etterem ON szalloda_etterem.szallodaId = Szalloda.ID INNER JOIN etterem ON szalloda_etterem.etteremID = etterem.id")
    return cursor.fetchall()

def query3(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT Szalloda.szalloda, COUNT(szoba.id) FROM Szalloda INNER JOIN szoba on Szalloda.id = szoba.szallodaId GROUP BY Szalloda.szalloda")
    return cursor.fetchall()

def query4(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT Szalloda.szalloda, COUNT(szoba_foglalas.foglalasID) FROM Szalloda INNER JOIN szoba ON Szalloda.id = szoba.szallodaId INNER JOIN szoba_foglalas ON szoba_foglalas.szobaID = szoba.ID GROUP BY Szalloda.szalloda")
    return cursor.fetchall()

def query5(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT Szalloda.szalloda FROM Szalloda INNER JOIN szoba ON Szalloda.id = szoba.szallodaId INNER JOIN szoba_foglalas ON szoba_foglalas.szobaID = szoba.ID GROUP BY Szalloda.szalloda")
    return cursor.fetchall()

def query6(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT Varos.varos from Varos INNER JOIN szalloda ON szalloda.varosID = Varos.id INNER JOIN szalloda_parkolo ON szalloda_parkolo.szallodaID = szalloda.id GROUP BY Varos.varos")
    return cursor.fetchall()

def query7(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT avg(szoba.agy) FROM Szalloda JOIN szoba ON szoba.szallodaId = szalloda.id ORDER BY szalloda.szalloda")
    return cursor.fetchall()


def pyp_query1(conn, varos_neve):
    Szalloda = Table('Szalloda')
    Parkolo = Table('szalloda_parkolo')
    Varos = Table('Varos')

    q = Query.from_(Szalloda).join(Parkolo).on(Szalloda.id == Parkolo.szallodaID)\
        .join(Varos).on(Szalloda.varosID == Varos.id)\
        .select(Szalloda.szalloda, Parkolo.parkoloID)\
        .where(Varos.varos == varos_neve)

    sql_query = str(q)
    cursor = conn.cursor()
    cursor.execute(sql_query)
    return cursor.fetchall()

def pyp_query2(conn, szalloda_neve):
    Szalloda = Table('Szalloda')
    Sz_etterem = Table('szalloda_etterem')
    Etterem = Table('etterem')

    q = Query.from_(Szalloda).join(Sz_etterem).on(Szalloda.id == Sz_etterem.szallodaid)\
        .join(Etterem).on(Sz_etterem.etteremid == Etterem.id)\
        .select(Szalloda.szalloda,Etterem.tipus)\
        .where(Szalloda.szalloda == szalloda_neve)

    sql_query = str(q)
    cursor = conn.cursor()
    cursor.execute(sql_query)
    return cursor.fetchall()

def pyp_query3(conn, szalloda_neve):
    Szalloda = Table('Szalloda')
    Szoba = Table('szoba')

    q = Query.from_(Szalloda).join(Szoba).on(Szalloda.id == Szoba.szallodaid)\
        .select(Szalloda.szalloda.count(Szoba.id))\
        .groupby(Szalloda.szalloda)\
        .where(Szalloda.szalloda == szalloda_neve)

    sql_query = str(q)
    cursor = conn.cursor()
    cursor.execute(sql_query)
    return cursor.fetchall()

def pyp_query4(conn,szalloda_neve):
    Szalloda = Table('Szalloda')
    Szoba = Table('Szoba')
    Sz_foglalas = Table('szoba_foglalas')

    q = Query.from_(Szalloda).join(Szoba).on(Szoba.szallodaid == Szalloda.id)\
        .join(Sz_foglalas).on(Sz_foglalas.szobaid == Szoba.id)\
        .select(Szalloda.szalloda.count(Sz_foglalas.foglalasID))\
        .where(Szalloda.szalloda == szalloda_neve)

    sql_query = str(q)
    cursor = conn.cursor()
    cursor.execute(sql_query)
    return cursor.fetchall()

def pyp_query5(conn,szalloda_neve ):
    Szalloda = Table('Szalloda')
    Szoba = Table('Szoba')
    Sz_foglalas = Table('szoba_foglalas')

    q = Query.from_(Szalloda).join(Szoba).on(Szoba.szallodaid == Szalloda.id) \
        .join(Sz_foglalas).on(Sz_foglalas.szobaid == Szoba.id)\
        .select(Szalloda.szalloda)\
        .where(Szalloda.szalloda == szalloda_neve)

    sql_query = str(q)
    cursor = conn.cursor()
    cursor.execute(sql_query)
    return cursor.fetchall()

def pyp_query6(conn, varos_neve):
    Szalloda = Table('Szalloda')
    Varos = Table('Varos')
    Sz_parkolo = Table('szalloda_parkolo')

    q = Query.from_(Varos).join(Szalloda).on(Szalloda.varosid == Varos.id)\
        .join(Sz_parkolo).on(Szalloda.id == Sz_parkolo.szallodaid)\
        .select(Varos.varos)\
        .where(Varos.varos == varos_neve)

    sql_query = str(q)
    cursor = conn.cursor()
    cursor.execute(sql_query)
    return cursor.fetchall()
def pyp_query7(conn, szalloda_neve):
    Szalloda = Table('Szalloda')
    Szoba = Table('Szoba')

    q = Query.from_(Szalloda).join(Szoba).on(Szoba.szallodaid == Szalloda.id)\
        .select(Szalloda.szalloda.avg(Szoba.agy))\
        .where(Szalloda.szalloda == szalloda_neve)
    sql_query = str(q)
    cursor = conn.cursor()
    cursor.execute(sql_query)
    return cursor.fetchall()