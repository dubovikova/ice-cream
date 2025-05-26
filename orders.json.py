import json

order = {"name": "Полина", "product": "Капкейк", "flavor": "Шоколад", "topping": "Взбитые сливки"}
f = open("orders_json.txt", "w", encoding="UTF-8")
json.dump(order, f, ensure_ascii=False)
f.close()
