#!/usr/bin/env python
# coding: utf-8




import socket
import os

try :
    client = socket.socket()  #By default ipv4 and tcp

    SERVER_IP = input("Enter Server IP : ")
    SERVER_PORT = int(input("Enter server port : "))

    client.connect( (SERVER_IP,SERVER_PORT) ) # connecting to server
    print('\n\nConnected to Server at ',SERVER_IP)

    if not os.path.isdir('Downloads') :
        os.mkdir('Downloads') #make Downloads folder

    END = 'closed'

    while True:
        file_name = input("Enter file name to download : ")

        client.send(file_name.encode()) #sending file name

        response = client.recv(2024).decode() #Receiving response from server 

        if response == 'FILE FOUND!!':
            print(f"\n\n {response} !!!!!")
            print('\nDownloading...')
            with open('Downloads\\'+file_name,'wb') as file:
                while True:
                    line = client.recv(2024)
                    if line == END.encode() :
                        file.close()
                        print('\n\nDownloaded ....')
                        break
                    else:
                        file.write(line)
        else :
            print(f'\n\n {response} !!!!!')

        if input("Do you want to continue downloading more files (y or n)").lower() == 'n':
            client.send(END.encode())
            break
    client.close()
    
except Exception as error:
    print("Unable to connect !! Error!!!! ",error)

