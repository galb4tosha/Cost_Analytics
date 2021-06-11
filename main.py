from data_base import *

if __name__ == "__main__":
    print("""Введите 1 для вывода общей таблицы
        2 для вывода статистики по магазинам
        3 для вывода списка магазинов
        4 для добавления нового магазина
        5 для добавления новой покупки""")
    menu = input()

    if menu == 1:
        print(get_all_table())

    elif menu == 2:
        print(get_shop_stat())

    elif menu == 3:
        print(get_shop_list())

    elif menu == 4:
        print("Введите название магазина и его тип через запятую")
        shop_name = input()
        shop_type = input()
        print(add_shop(shop_name, shop_type))
    
    elif menu == 5:
        print("Введите id магазина, сумму и дату покупки")
        shop_id = input()
        sum_coast = input()
        date = input()
        print(add_coast(shop_id, sum_coast, date))
