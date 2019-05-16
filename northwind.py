from flask import Flask, render_template, url_for
import sqlite3

app = Flask(__name__)

copyright = "Copyright © 2019 Collin College All rights reserved."

@app.route("/")
def index():
   urls = {"products":url_for("products"),"suppliers":"/suppliers","orders":"/orders"}    
   return render_template("index.html", urls = urls,footer = copyright)

# PRODUCTS

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

   # Pass rows into Jinja2 render_template function to use in products.html.
   return render_template("products.html", urls = {"index":url_for("index")}, products = rows, footer = copyright)

@app.route("/products/<int:id>")
def product_details(id):

   db = sqlite3.connect("northwind2.db")

   cursor = db.cursor() 
 
   cursor.execute(f'''
        SELECT id,product_code,product_name,description,standard_cost,
        list_price,reorder_level, target_level,
        quantity_per_unit,discountinued,minimum_reorder_quantity,category,attachments
        FROM products
        WHERE id = {id}
        ''')

   row = cursor.fetchone() 
    
   db.close()
   
   return render_template("product_detail.html", product = row, footer = copyright)

# SUPPLIERS

@app.route("/suppliers")
def suppliers():
 
   db = sqlite3.connect("northwind2.db")

   cursor = db.cursor() 
 
   cursor.execute('''
         SELECT id,company, first_name, last_name
         FROM suppliers
         ''')

   # Get all rows.
   rows = cursor.fetchall()

   db.close()

   # Pass rows into Jinja2 render_template function to use in suppliers.html.
   return render_template("suppliers.html", urls = {"index":url_for("index")}, suppliers = rows, footer = copyright)

@app.route("/suppliers/<int:id>")
def supplier_details(id):

   db = sqlite3.connect("northwind2.db")

   cursor = db.cursor() 
 
   cursor.execute(f'''
         SELECT id,company, last_name, first_name
         FROM suppliers
         WHERE id = {id}
         ''')

   row = cursor.fetchone() 
    
   db.close()
   
   return render_template("supplier_detail.html", supplier = row, footer = copyright)

# ORDERS

@app.route("/orders")
def orders():
 
   db = sqlite3.connect("northwind2.db")

   cursor = db.cursor() 
 
   cursor.execute('''
         SELECT id,order_date
         FROM orders
         ''')

   # Get all rows.
   rows = cursor.fetchall()

   db.close()

   # Pass rows into Jinja2 render_template function to use in orders.html.
   return render_template("orders.html", urls = {"index":url_for("index")}, orders = rows, footer = copyright)

@app.route("/orders/<int:id>")
def order_details(id):

   db = sqlite3.connect("northwind2.db")

   cursor = db.cursor() 
 
   cursor.execute(f'''
            SELECT id,order_date
            FROM orders
            WHERE id = {id}
            ''')

   row = cursor.fetchone() 
    
   db.close()
   
   return render_template("order_detail.html", order = row, footer = copyright)