#!/usr/bin/env python
# coding: utf-8

# In[5]:


from getpass import getpass
import os
database = [
            [1001, 'Sachin', 'redhat', 50000 ],
            [1002, 'ram', 'Asimov', 45000],
            [1003, 'nikhil', 'lihkin', 60000]
           ]
user = None
def clear() : # to clear screen
    if os.name == 'nt' :  #for Windows
        os.system('cls')
    else :               #for Linux
        os.system('clear')
    
def main_menu() :
    main = '''
                                      " WELCOME TO BANK SERVICE "
                                             
                             1. Login                           
                             2. Signup                          
                             3. Exit            
           '''
    print(main)
    choice = int(input("Enter your choice (1-3) : "))
    if choice == 1:
        login()
    elif choice == 2:
        signup()
    elif choice == 3:
        exit()
    else :
        print("\tINVALID CHOICE !!! please Enter a valid choice(1-3)")
        main_menu()


def is_verified(account_no,password):
    global user
    index = account_no - 1001
    if len(database) >= index+1 and account_no == database[index][0] and password == database[index][2]:
            user = index
            return True
    else :
        return False
def login():
    clear()
    account_no = int(input("Enter a ACCOUNT NO. : "))
    password = getpass("Enter PASSWORD : ")
    
    if is_verified(account_no,password):
        sub_menu()
    else :
        print("\tINVAILD Cerdentials !!! TRY Again")
        main_menu()

def is_valid_name(username): 
    for data in database:
        if username == data[1]:
            return False
    else:
        return True
        
def signup():
    clear()
    username = input("Enter a USERNAME : ")
    password = getpass("Enter PASSWORD : ")
    balance = int(input("Enter BALANCE : "))   
    if len(database) > 0:
        last_acc_no = database[-1][0]
    else :
        last_acc_no = 1000
    if is_valid_name(username):
        database.append([last_acc_no+1,username,password,balance])
        print("\tAccount keep safe use for login...")
        main_menu()
    else :
        print("\tINVALID USERNAME !!! TRY AGAIN ")
        signup()
def exit():
    clear()
    print("\tThanks !! For using Bank Services")

def sub_menu():
    
    menu = '''
                    1. Debit
                    2. Credit
                    3. Balance Enquiry
                    4. Update Record
                    5. Logout
    
           '''
    print(menu)
    choice = int(input('Enter your choice (1-5) : '))
    clear()
    if choice == 1:
        debit()
    elif choice == 2:
        credit()
    elif choice == 3:
        balance_Enquiry()
    elif choice == 4:
        update_record()
    elif choice == 5:
        main_menu()
    else:
        print("\tINVALID CHOICE !!! please Enter a valid choice(1-5)")
        sub_menu()
def debit():
    amount = int(input("Enter Amount to Debit : "))
    if amount <= database[user][-1]:
        database[user][-1] -= amount
    else:
        print("\tInsufficient Balance !!!!")
    sub_menu()
def credit():
    amount = int(input("Enter Amount to Debit : "))
    database[user][-1] += amount
    sub_menu()
def balance_Enquiry():
    print('Account Balance : ',database[user][-1])
    sub_menu()
def update_record():
    database[user][1] = input("Enter a USERNAME : ")
    database[user][2] = getpass("Enter PASSWORD : ")
    sub_menu()
    
    
main_menu()


# In[ ]:





# In[ ]:




