import sqlite3
from Profile import *


class DataBase():
    def __init__(self, _path):
        self.path = _path
        self.connection = None

    def openDataBase(self):
        try:
            self.connection = sqlite3.connect(self.path)
        except Error as e:
            print(e)


    def createTables(self):
        cursor = self.connection.cursor()
        sql_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        password text NOT NULL,
                                        company text,
                                        email text,
                                        phone text
                                    ); """
        sql_library_table = """ CREATE TABLE IF NOT EXISTS library (
                                        id integer PRIMARY KEY,
                                        name text,
                                        company text,
                                        email text NOT NULL,
                                        phone text
                                    ); """
        
        cursor.execute(sql_users_table)
        cursor.execute(sql_library_table)
        cursor.close()
    

    def addUser(self, user):
        cursor = self.connection.cursor()
        data = (user.name, user.password, user.companyName, user.email, user.telephoneNumber)
        sql_insert = ''' INSERT INTO users(name,password,company,email, phone)
              VALUES(?,?,?,?,?) '''
        cursor.execute(sql_insert, data)
        self.connection.commit()
        cursor.close()

    def addCard(self, card):
        cursor = self.connection.cursor()
        data = (card.name, card.companyName, card.email, card.telephoneNumber)
        sql_insert = ''' INSERT INTO library(name,company,email, phone)
              VALUES(?,?,?,?) '''
        cursor.execute(sql_insert, data)
        self.connection.commit()
        cursor.close()

    def isUserRegistered(self, username, password):
        cursor = self.connection.cursor()
        request = "SELECT * FROM users WHERE name ='" + username + "'"
        cursor.execute(request)
        result = cursor.fetchall()
        cursor.close()
        for element in result:
            if element[1] == username and element[2]==password:
                return True
        return False


    def getCards(self):
        cursor = self.connection.cursor()
        request = "SELECT * FROM library"
        cursor.execute(request)
        result = cursor.fetchall()
        cursor.close()
        return result


