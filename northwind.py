from flask import Flask, render_template, url_for
import sqlite3

app = Flask(__name__)

copyright = "Copyright © 2019 Collin College All rights reserved."

@app.route("/")
def index():
   urls = {"products":url_for("products")}    
   return render_template("index.html", urls = urls,footer = copyright)

@app.route("/products")
def products():
 
   db = sqlite3.connect("northwind2.db")

   cursor = db.cursor() 
 
   cursor.execute('''
        SELECT id,product_code,product_name,description
        FROM products
        ''')

   # Get all rows.
   rows = cursor.fetchall()

   db.close()

   # Pass rows into Jinja2 render_template() function to use in products.html.
   return render_template("products.html", urls = {"index":url_for("index")}, products = rows, footer = copyright)

@app.route("/products/<int:id>")
def product_details(id):

# place code here
   
   return render_template("product_detail.html", product = row, footer = copyright)
