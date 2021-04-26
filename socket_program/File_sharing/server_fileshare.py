#!/usr/bin/env python
# coding: utf-8



import socket
import os
try :
    server = socket.socket()  #By default ipv4 and tcp

    SERVER_IP = input("Enter Server IP : ")
    SERVER_PORT = int(input("Enter server port : "))

    server.bind( (SERVER_IP , SERVER_PORT) )
    #Binding server 
    server.listen() # by default 5 client at a time

    print("\n\n Server is Running .................")

    client , (client_IP ,client_port) = server.accept() 

    print('\n\nConnected to Client at ',client_IP)
    END = 'closed'
    while True:
        file_name = client.recv(2024).decode() # Taking file name from client

        if file_name.lower() == END:
            break
        #Checking file exits or not
        if os.path.exists('Files\\'+file_name) and os.path.isfile('Files\\'+file_name) :
            message = 'FILE FOUND!!'.encode()
            client.send(message)

            with open('Files\\'+file_name, 'rb') as file:
                print('\nTransferring file ......')
                for line in file:
                    client.send(line)
            file.close()
            print('\n\n File Transfered !!!!!')
            client.send(END.encode())


        else:
            message = 'FILE NOT FOUND!!'.encode()
            client.send(message)
    client.close()
    server.close()
    
except Exception as error:
    print("Unable to connect !! Error!!!! ",error)




