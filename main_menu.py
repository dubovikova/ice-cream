def main_menu():
    while True:
        print("___________________________________________")
        print("🐱Добро пожаловать в кафе Meow-Meow!🍨🍦🍧")
        order = get_order()
        print("Проверьте заказ:")
        print_order(order)
        confirm = input("Все верно? Чтобы подтвердить заказ, введите 'да' чтобы отклонить заказ, введите 'нет': ")
        if confirm == "да" or confirm == "ДА" or confirm == "Да" or confirm == "дА":
            save_order(order)
        else:
            continue


def read_menu(filename):
    f = open(filename, encoding="UTF-8")
    temp = f.readlines()
    menu_list = []
    for item in temp:
        new_item = item.strip()
        menu_list.append(new_item)
    return menu_list


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


def get_order():
    order = {}
    order["name"] = input("Напишите ваше имя: ")
    products = read_menu("products.txt")
    flavors = read_menu("flavors.txt")
    toppings = read_menu("toppings.txt")
    order["product"] = menu(products, "Еда/напитки", "Введите номер еды/напитка: ")
    order["flavor"] = menu(flavors, "Вкусы", "Введите номер вкуса: ")
    order["topping"] = menu(toppings, "Добавки и топпинги", "Введите номер топпинга: ")
    return order


def print_order(order):
    print("Имя: ", order["name"])
    print("Еда/напиток: ", order["product"])
    print("Вкус: ", order["flavor"])
    print("Топпинг: ", order["topping"])
    return


def save_order(order):
    print("Заказ сохраняется...")
    return


main_menu()
