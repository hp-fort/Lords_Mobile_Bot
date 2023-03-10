import os
import sqlite3

class DatabaseHandler():
    def __init__(self, database_name:str):
        self.con = sqlite3.connect(f"{os. path. dirname(os.path. abspath(__file__))}/{database_name}")
        self.con.row_factory = sqlite3.Row

    def add_member(self, member_id:int, success:int):
        cursor = self.con.cursor()
        query = "INSERT INTO FA (member_id, guild_fest_success) VALUES (?, ?);"
        cursor.execute(query, (member_id, success))
        cursor.close()
        self.con.commit()

    def search_member(self):
        cursor = self.con.cursor()
        query = "SELECT member_id FROM FA;"
        cursor.execute(query,)
        result = list(map(dict, cursor.fetchall()))
        cursor.close()
        return result
    
    def take_old_result(self, member_id:int):
        cursor = self.con.cursor()
        query = "SELECT guild_fest_success FROM FA WHERE member_id = ?;"
        cursor.execute(query, (member_id,))
        result = list(map(dict, cursor.fetchall()))
        cursor.close()
        return result
    
    def update_new_gf(self, member_id:int, success:int):
        cursor = self.con.cursor()
        query = "UPDATE FA SET guild_fest_success = ? WHERE member_id = ?;"
        cursor.execute(query, (success, member_id,))
        cursor.close()
        self.con.commit()