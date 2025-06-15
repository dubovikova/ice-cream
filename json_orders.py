import os
import json

order1 = {"name": "Кот Кот Кот Кот Котульки", "product": "Горячий шоколад", "flavor": "Карамель", "topping": "Зефирки"}
order2 = {"name": "Котокусь", "product": "Мороженое", "flavor": "Ваниль", "topping": "Шоколадка"}
order3 = {"name": "Котокекс", "product": "Капкейк", "flavor": "Шоколад", "topping": "Взбитые сливки"}
orders = []
orders.append(order1)
orders.append(order2)
orders.append(order3)
f = open("orders.json", "w", encoding="UTF-8")
json.dump(orders, f, ensure_ascii=False, indent=4)
f.close()
f = open("orders.json", "r", encoding="UTF-8")
saved_orders = json.load(f)
for s in saved_orders:
    print(s)

def load_orders(filename):
    if os.path.exists(filename):
        f = open(filename, "r")
        orders = json.load(f)
        return orders
    