import os
import json


def main_menu(orders):
    while True:
        print("___________________________________________")
        print("🐱Добро пожаловать в кафе Meow-Meow!🍨🍦🍧")
        order = get_order()
        if order == {}:
            print("🐱Завершение работы...")
            return
        else:
            print("🐱Проверьте заказ:")
            print_order(order)
            confirm = input(
                "Все верно? Чтобы подтвердить заказ, введите 'да' чтобы отклонить заказ, введите 'нет': "
            )
            if confirm == "да" or confirm == "ДА" or confirm == "Да" or confirm == "дА":
                orders.append(order)
                print("🐱Спасибо за заказ!🐱")
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
            print("🐱Введите число от 1 до", len(choices), "!")
            answer = ""
    return answer


def get_order():
    order = {}
    name = input("🐱Напишите ваше имя, для выхода нажмите Enter: ")
    if name == "":
        return {}
    else:
        order["name"] = name
        products = read_menu("products.txt")
        flavors = read_menu("flavors.txt")
        toppings = read_menu("toppings.txt")
        order["product"] = menu(
            products, "🐱Еда/напитки🐱", "🐱Введите номер еды/напитка: "
        )
        order["flavor"] = menu(flavors, "🐱Вкусы🐱", "🐱Введите номер вкуса: ")
        order["topping"] = menu(
            toppings, "🐱Добавки и топпинги🐱", "🐱Введите номер топпинга: "
        )
        return order


def print_order(order):
    print("🐱Имя: ", order["name"])
    print("🐱Еда/напиток: ", order["product"])
    print("🐱Вкус: ", order["flavor"])
    print("🐱Топпинг: ", order["topping"])
    return


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
main_menu(orders)
save_orders(orders, "orders.json")
