print("🐱Добро пожаловать в кафе Meow-Meow!🍨🍦🍧")
name = input("🐱Напишите ваше имя: ")
def menu(choices, title, promt):
    print("__________________________")
    print(title)
    print("__________________________")
    i = 1
    for c in choices:
        print(i, c)
        i += 1
    choice = input(promt)
    answer = choices[int(choice) - 1]
    return answer
products = ["Капкейк", "Мороженое", "Эклер", "Коктейль", "Горячий шоколад"]
flavors = ["Клубника", "Мята", "Шоколад", "Ваниль", "Малина", "Карамель", "Банан", "Сгущёнка"]
toppings = ["Вишенка", "Карамельная поливка", "Мармеладки", "Взбитые сливки", "Кусочки шоколада", "Зефирки"]
product = menu(products, "🐱Еда/напитки🐱", "🐱Введите номер еды/напитка: ")
flavor = menu(flavors, "🐱Вкусы🐱", "🐱Введите номер вкуса: ")
topping = menu(toppings, "🐱Добавки и топпинги🐱", "🐱Введите номер топпинга:")
print("🐱Ваш заказ,", name, ":")
print("🐱Еда/напиток: ", product)
print("🐱Вкус: ", flavor)
print("🐱Топпинг: ", topping)
print("🐱Спасибо за заказ!🐱")
