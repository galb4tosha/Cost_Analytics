import sqlite3

def get_execute(execute_str):
    conn = sqlite3.connect("coasts.db")
    cursor = conn.cursor()
    cursor.execute(execute_str)
    return cursor.fetchall()


def get_coast():
    execute_str = """select * from coast"""
    return get_execute(execute_str)


def get_all_table():
    execute_str = """select sum as "Сумма", date as "Дата", type as "Тип", name as "Название"
                    from coast
                    left join shops
                    on coast.shop_id = shops.rowid"""
    return get_execute(execute_str)


def get_shop_stat():
    execute_str = """select count(*) as "Количество покупок", sum(sum) as "Сумма покупок", name as "Название"
                    from coast 
                    left join shops
                    on coast.shop_id = shops.rowid
                    group by shop_id
                    order by sum(sum) desc"""
    return get_execute(execute_str)


def get_shop_list():
    execute_str = """select * from shops"""
    return get_execute(execute_str)


def add_coast(sum_coast, date, shop_id):
    execute_str = f"""INSERT INTO coast VALUES ({shop_id}, {sum_coast}, '{date}')"""
    return get_execute(execute_str)


def add_shop(name_shop, type_shop):
    execute_str = f"""INSERT INTO shops VALUES ({type_shop}, {name_shop}"""
    return get_execute(execute_str)
