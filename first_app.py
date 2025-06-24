from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("greeting.html")

@app.route("/hello/<name>")
def greet(name="Stranger"):
    return render_template("greeting.html", name=name)

# Русские названия для кодов
names = {
    "cupcake": "Капкейк",
    "ice-cream": "Мороженое",
    "eclair": "Эклер",
    "croissant": "Круассан",
    "cocktail": "Коктейль",
    "hot-chocolate": "Горячий шоколад",
    "tea": "Чай",
    "coffee": "Кофе"
}

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        product_code = request.form.get('product')  # "tea", "croissant" и т.п.
        product_name = names.get(product_code, "Неизвестно")  # "Чай", "Круассан"
        return render_template("thank_you.html", product=product_name) 
    return render_template("forms.html")

# 🚨 ВАЖНО: запускаем сервер только после всех маршрутов
if __name__ == "__main__":
    app.run(debug=True)