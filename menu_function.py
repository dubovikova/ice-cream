def menu(choices, title, promt):
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
choice = menu(products, "Еда/напитки", "Введите номер еды/напитка: ")
print(choice)
