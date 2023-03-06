import os
import sqlite3

class DatabaseHandler():
    def __init__(self, database_name:str):
        self.con = sqlite3.connect(f"'{os. path. dirname(os.path. abspath(__file__))}/{database_name}")
        self.con.row_factory = sqlite3.Row

        def add_member(member_id:int, success:int):
            cursor = self.con.cursor()
            query = "INSERT INTO F-A (member_id, guild_fest_success) VALUES (?, ?);"
            cursor.execute(query, (member_id, success))
            cursor.close()
            self.con.commit()