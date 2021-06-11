import numpy as np
import sqlite3

conn = sqlite3.connect("coasts.db")
cursor = conn.cursor()

N = 1000
years_list = ["2022", "2021", "2020", "2019"]
execute = "INSERT INTO coast VALUES "

for i in range(N):
    day = np.random.randint(1, 32)
    month = np.random.randint(1, 13)
    year = years_list[np.random.randint(-1, 3)]
    shop_id = np.random.randint(1, 13)
    sum_coast = np.random.randint(200, 3000)

    execute = execute + f"({shop_id}, {sum_coast}, '{year}-{month}-{day}'), "

execute = execute[:-2] + ";"
print(execute)
