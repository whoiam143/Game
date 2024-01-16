import sqlite3 as sql


def create_bd():  # Функция для создания база данных
    with sql.connect("results.db") as con:
        cur = con.cursor()

        cur.execute(""" CREATE TABLE IF NOT EXISTS score(
            time  TEXT,
            level INTEGER,
            score INTEGER,
            accuracy TEXT);
            """)

        con.commit()


def add_result(time, level, score, acc):  # Функция для добовления результатов
    with sql.connect("results.db") as bd:
        cr = bd.cursor()

    cr.execute("""INSERT INTO score VALUES (?, ?, ?, ?)""",
               (time, level, score, acc))

    bd.commit()


def results():  # Функция для получения списка результатов
    with sql.connect("results.db") as bd:
        cr = bd.cursor()

        res = cr.execute("""SELECT wpm FROM score""")
        lst_of_res = [list(i)[0] for i in res if type(list(i)[0]) is int]
        if len(lst_of_res) == 0:
            lst_of_res.append(0)

    return lst_of_res



