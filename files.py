f = open("products.txt", encoding="UTF-8")
temp = f.readlines()
products = []
for item in temp:
    new_item = item.strip()
    products.append(new_item)
print(products)
