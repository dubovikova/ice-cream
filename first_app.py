from flask import Flask, render_template, request, send_from_directory
import os
import json
import sqlite3

def save_order(order):
    con = sqlite3.connect("orders.db")
    cur = con.cursor()
    cur.execute(
    "INSERT INTO orders(name,product,flavor,topping) VALUES(?,?,?,?);",
    (order["name"], order["product"], order["flavor"], order["topping"]),
    ) 
    con.commit()
    return

def get_orders():
    con = sqlite3.connect("orders.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM orders;")
    rows = cur.fetchall()
    return rows

def load_orders(filename):
    if os.path.exists(filename):
        f = open(filename, "r")
        with open(filename, "r", encoding="UTF-8") as f:
            orders = json.load(f)
        return orders
    else:
        orders = {}
        return orders

def save_orders(orders, filename):
    with open(filename, "w", encoding="UTF-8") as f:
     f = open(filename, "w", encoding="UTF-8")
    json.dump(orders, f, indent=4)
    f.close()
    return

def read_menu(filename):
    menu_dict = {}
    with open(filename, encoding="UTF-8") as f:
        for line in f:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                menu_dict[key] = value
    return menu_dict

products = read_menu("products.txt")
flavors = read_menu("flavors.txt")
toppings = read_menu("toppings.txt")

orders = load_orders("orders.json")

con = sqlite3.connect("orders.db")
cur = con.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS orders(name, product, flavor, topping);")

app = Flask(__name__, static_folder='static')

@app.route("/")
def index():
    return render_template("greeting.html")

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        name = request.form.get('name')
        product_code = request.form.get('product')
        product_name = products.get(product_code, "Неизвестно")
        flavor_code = request.form.get('flavor')
        flavor_name = flavors.get(flavor_code, "Неизвестно")
        topping_code = request.form.get('topping')
        topping_name = toppings.get(topping_code, "Неизвестно")
        new_order = {
            "name": name,
            "product": product_name,
            "flavor": flavor_name,
            "topping": topping_name
        }
        orders.append(new_order)
        save_orders(orders, "orders.json")
        save_order(new_order)
        return render_template(
            "thank_you.html", new_order=new_order)
    return render_template(
        "forms.html",
        products=products,
        flavors=flavors,
        toppings=toppings)

@app.route("/list", methods=["GET"])
def list_orders():
    orders = get_orders()
    return render_template("list.html", orders=orders)

if __name__ == "__main__":
    app.run(debug=True)