from flask import Flask, render_template, request
import sqlite3
import json

def conexion():
    return sqlite3.connect("base.db")

app = Flask(__name__)

@app.route("/pepito", methods=["GET"])
def index():
    db = conexion()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM ingreso")
    base = cursor.fetchall()
    print(base)
    cursor.close()
    db.close()
    return render_template("index.html", base=base)

@app.route("/cargar", methods=["POST"])
def cargar():
    datos = json.loads(request.data)
    db = conexion()
    cursor = db.cursor()
    cursor.execute("INSERT INTO ingreso VALUES (?, ?)", (None, "27-9-9887"))
    cursor.close()
    db.close()
    return "hola"


app.run(debug=True)