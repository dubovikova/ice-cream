print("🐱Добро пожаловать в кафе Meow-Meow!🍨🍦🍧")
name = input("🐱Напишите ваше имя: ")


def menu(choices, title="Меню", promt="Введите номер: "):
    print((len(title) + 2) * "_")
    print(title)
    print((len(title) + 2) * "_")
    i = 1
    for c in choices:
        print(i, c)
        i += 1
    while True:
        print("🐱Чтобы пропустить этот раздел меню, введите 0")
        choice = input(promt)
        allowed_answers = []
        for a in range(1, len(choices) + 1):
            allowed_answers.append(str(a))
        allowed_answers.append("0")
        if choice in allowed_answers:
            if choice == "0":
                answer = "-"
                break
            else:
                answer = choices[int(choice) - 1]
                break
        else:
            print("Введите число от 1 до", len(choices), "!")
            answer = ""
    return answer


products = ["Капкейк", "Мороженое", "Эклер", "Коктейль", "Горячий шоколад"]
flavors = [
    "Клубника",
    "Мята",
    "Шоколад",
    "Ваниль",
    "Малина",
    "Карамель",
    "Банан",
    "Сгущёнка",
]
toppings = [
    "Вишенка",
    "Карамельная поливка",
    "Мармеладки",
    "Взбитые сливки",
    "Кусочки шоколада",
    "Зефирки",
]
product = menu(products, "🐱Еда и напитки🐱", "🐱Введите номер еды/напитка: ")
flavor = menu(flavors, "🐱Вкусы🐱", "🐱Введите номер вкуса: ")
topping = menu(toppings, "🐱Добавки и топпинги🐱", "🐱Введите номер топпинга: ")
print("_______________________________")
print("🐱Ваш заказ,", name, ":")
print("🐱Еда/напиток: ", product)
print("🐱Вкус: ", flavor)
print("🐱Топпинг: ", topping)
print("🐱Спасибо за заказ!🐱")
