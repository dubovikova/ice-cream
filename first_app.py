from flask import Flask, render_template, request
import os
import json

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
        json.dump(orders, f, ensure_ascii=False, indent=4)
    return

orders = load_orders("orders.json")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("greeting.html")

@app.route("/hello/<name>")
def greet(name="Stranger"):
    return render_template("greeting.html", name=name)

# Русские названия для кодов
products = {
    "cupcake": "Капкейк",
    "ice-cream": "Мороженое",
    "eclair": "Эклер",
    "croissant": "Круассан",
    "cocktail": "Коктейль",
    "hot-chocolate": "Горячий шоколад",
    "tea": "Чай",
    "coffee": "Кофе"
}

flavors = {
    "vanilla": "Ваниль",
    "chocolate": "Шоколад",
    "strawberry": "Клубника",
    "mint": "Мята",
    "caramel": "Карамель"
}

toppings = {
    "cherry": "Вишенка",
    "sprinkles": "Посыпка",
    "chocolate-sause": "Шоколадный соус",
    "marshmallows": "Зефирки",
    "pieces-of-chocolate": "Кусочки шоколада",
    "caramel-sause": "Карамельный соус",
    "powdered-sugar": "Сахарная пудра"
}

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
        return render_template(
            "thank_you.html", new_order=new_order)
    return render_template("forms.html")

# 🚨 ВАЖНО: запускаем сервер только после всех маршрутов
if __name__ == "__main__":
    app.run(debug=True)