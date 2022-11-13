import sqlite3


def get_server_blocks():
    con = sqlite3.connect("app.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM server_blocks")
    res = res.fetchall()

    cur.close()
    con.close()

    return res