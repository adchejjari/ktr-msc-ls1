from debugpy import connect
from Database import *
import os
#os.system('cls||clear')


connectionMenu = """Welcome to the application
                    
To login, please type 1
To create a new account please type 2
To quit the application please type 0\n"""

loginMenu = """Welcome to the login Menu, please type your username and password bellow : """

profileMenu ="""To see business cards please type 1
To add a new business card please type 2
To log out please type 3
"""

class App():
    def __init__(self):
        self.database = DataBase("database")
        self.user = None
        self.database.openDataBase()
        self.database.createTables()
        
    

    def connect(self):
        os.system('cls||clear')
        print(connectionMenu)
        userInput = input("Your entry : ")
        while userInput != "1" and userInput != "2" and userInput != "0":
            print(connectionMenu)
            userInput = input("Your entry : ")
        if userInput == "1":
            self.login()
        elif userInput == "2":
            self.createProfile()
        else:
            print("Bye bye .. :) ")
            quit
        


        

    def login(self):
        os.system('cls||clear')
        print(loginMenu+'\n \n')
        username = input("Please type your username :")
        password = input("Please type your password :")
        while not self.database.isUserRegistered(username, password):
            print("Invalid username or password, please try again! \n \n")
            username = input("Please type your username :")
            password = input("Please type your password :")
        self.user = username
        self.displayProfile()

    def logout(self):
        os.system('cls||clear')
        self.user = ""
        self.connect()

    def createProfile(self):
        os.system('cls||clear')
        print("To create a new profile, please enter the following Data :\n\n")
        name = input("Please enter the name :")
        while name == "":
            name = input("Invalid name, please enter your name :")
        password = input("Please enter the password :")
        while password == "":
            password = input("Invalid password, please enter a new password :")
        company = input("Please enter the company name :")
        email = input("Please enter your email :")
        phone = input("Please enter your phone number :")
        user = User(name,password,company,email,phone)
        self.database.addUser(user)
        self.login()


    def displayProfile(self):
        os.system('cls||clear')
        print("Welcome to your Profile " + self.user + '\n')
        print(profileMenu)
        userInput = input("Please type your choice :")
        while userInput != "1" and userInput != "2" and userInput != "3":
            os.system('cls||clear')
            print("Invalid Choice, please try again : ")
            print(profileMenu)
            userInput = input("Please type your choice : ")
        if userInput == "1":
            self.displayCards()
        elif userInput == "2":
            self.addNewCard()
        elif userInput == "3":
            self.logout()
    
    def addNewCard(self):
        os.system('cls||clear')
        print("Please enter the following data to add a new card" )
        name = input("Please enter the name :")
        company = input("Please enter the company name :")
        email = input("Please enter the email adress :")
        while email == "":
            print("This email is not correct, please try again" )
            email = input("Please enter the email adress :")

        phone = input("Please enter the phoneNumber :")
        card = Card(name, company, email, phone)
        self.database.addCard(card)
        print("Card Added successfully ! ")
        self.displayProfile()

    def displayCards(self):
        os.system('cls||clear')
        allCards = self.database.getCards()
        print("Please find bellow all the buisness cards \n \n")
        for line in allCards:
            for data in line:
                print(data, end=' ')
            print()
        print('\n')
        choice = input("Please type 1 go to the main Menu, or 2 to log out :")
        while choice!= "1" and choice != "2":
            choice = input("Invalid entry,  please type 1 go to the main Menu, or 2 to log out :")
        if choice == "1":
            self.displayProfile()
        elif choice == "2":
            self.logout()


        
        
if __name__ == "__main__":
    myApp = App()
    myApp.connect()
