def main_menu():
    while True:
        order = get_order
        print("Проверьте заказ:")
        print_order(order)
        confirm = input()


def get_order():
    return {}


def print_order(order):
    print(order)
    return
