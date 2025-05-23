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


def read_menu(filename):
    f = open(filename, encoding="UTF-8")
    temp = f.readlines()
    menu_list = []
    for item in temp:
        new_item = item.strip()
        menu_list.append(new_item)
    return menu_list


products = read_menu("products.txt")
flavors = read_menu("flavors.txt")
toppings = read_menu("toppings.txt")
product = menu(products, "🐱Еда и напитки🐱", "🐱Введите номер еды/напитка: ")
flavor = menu(flavors, "🐱Вкусы🐱", "🐱Введите номер вкуса: ")
topping = menu(toppings, "🐱Добавки и топпинги🐱", "🐱Введите номер топпинга: ")
print("_______________________________")
print("🐱Ваш заказ,", name, ":")
print("🐱Еда/напиток: ", product)
print("🐱Вкус: ", flavor)
print("🐱Топпинг: ", topping)
print("🐱Спасибо за заказ!🐱")
