import sqlite3 as sql


class db:
    def __init__(self):
        try:
            self.con = sql.connect("counter.db")
            self.cur = self.con.cursor()
            self.cur.execute("DROP TABLE IF EXISTS counter")
            self.cur.execute(
                """
                CREATE TABLE IF NOT EXISTS counter(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    count INTEGER NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            self.cur.execute("INSERT INTO counter(count) VALUES(?)", [0])
            self.con.commit()
            print("connected successfully")

        except ConnectionError as e:
            print("Connection error!!!")
            raise e

    def get_count_value(self):
        res = self.cur.execute("SELECT count FROM counter")
        return res.fetchone()[0]

    def plus_click_db(self):
        self.cur.execute("UPDATE counter SET count = count + 1")
        self.con.commit() # commit the update
        return self.get_count_value()  # Return the updated count

    def minus_click_db(self):
        self.cur.execute("UPDATE counter SET count = count - 1")
        self.con.commit() # commit the update
        return self.get_count_value()  # Return the updated count

DB = db()