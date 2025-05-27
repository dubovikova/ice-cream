import json

orders = []
order = {"name": "Котик", "product": "Коктейль", "flavor": "Клубника", "topping": "Сахарная пудра"}
order1 = {"name": "Полина", "product": "Эклер", "flavor": "Шоколад", "topping": "Крем"}
orders.append(order)
orders.append(order1)
f = open("orders_json.txt", "w", encoding="UTF-8")
json.dump(orders, f, ensure_ascii=False, indent=4)
f.close()
