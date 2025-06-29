from flask import Flask, render_template, request

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
    "Powdered sugar": "Сахарная пудра"
}

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        product_code = request.form.get('product')
        product_name = products.get(product_code, "Неизвестно")
        flavor_code = request.form.get('flavor')
        flavor_name = flavors.get(flavor_code, "Неизвестно")
        topping_code = request.form.get('topping')
        topping_name = toppings.get(topping_code, "Неизвестно")
        return render_template("thank_you.html", product=product_name, flavor=flavor_name, topping=topping_name)
    return render_template("forms.html")

# 🚨 ВАЖНО: запускаем сервер только после всех маршрутов
if __name__ == "__main__":
    app.run(debug=True)