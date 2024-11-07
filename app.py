from flask import Flask, render_template, request
from db.queries import  db_conn, query1, query2, query3, query4, query5, query6, query7, pyp_query1, pyp_query2, pyp_query3, pyp_query4, pyp_query5, pyp_query6, pyp_query7 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/query1')
def query1_route():
    conn = db_conn('szalloda.db')
    eredmeny = query1(conn)
    oszlopok = ["Szálloda", "Parkoló ID"]
    conn.close()
    return render_template('template.html', eredmeny=eredmeny, oszlopok=oszlopok)

@app.route('/query2', methods=['POST'])
def query2_route():
    eredmeny = []
    oszlopok = ["Szálloda", "Étterem Típus"]
    
    if request.method == 'POST':
        szallodanev = request.form.get('szallodanev')
        conn = db_conn('szalloda.db')
        eredmeny = pyp_query2(conn, szallodanev)
        conn.close()
    print(szallodanev)
    return render_template('template.html', eredmeny=eredmeny, oszlopok=oszlopok)

@app.route('/query3')
def query3_route():
    conn = db_conn('szalloda.db')
    eredmeny = query3(conn)
    oszlopok = ["Szálloda", "Szobák Száma"]
    conn.close()
    return render_template('template.html', eredmeny=eredmeny, oszlopok=oszlopok)

@app.route('/query4')
def query4_route():
    conn = db_conn('szalloda.db')
    eredmeny = query4(conn)
    oszlopok = ["Szálloda", "Foglalás"]
    conn.close()
    return render_template('template.html', eredmeny=eredmeny, oszlopok=oszlopok)

@app.route('/query5')
def query5_route():
    conn = db_conn('szalloda.db')
    eredmeny = query5(conn)
    oszlopok = ["Szálloda"]
    conn.close()
    return render_template('template.html', eredmeny=eredmeny, oszlopok=oszlopok)

@app.route('/query6')
def query6_route():
    conn = db_conn('szalloda.db')
    eredmeny = query6(conn)
    oszlopok = ["Város"]
    conn.close()
    return render_template('template.html', eredmeny=eredmeny, oszlopok=oszlopok)

@app.route('/query7')
def query7_route():
    conn = db_conn('szalloda.db')
    eredmeny = query7(conn)
    oszlopok = ["Szálloda Átlag Ágyszáma"]
    conn.close()
    return render_template('template.html', eredmeny=eredmeny, oszlopok=oszlopok)