#!/usr/bin/env python
# coding: utf-8


import socket

client = socket.socket()

server_ip = input("Enter server IP : ")
server_port = int(input("Enter a server port : "))

client.connect( (server_ip, server_port) )

print("Connected to Server at ",server_ip)
End_chat = "BYE"
while True:
    request = input("Enter a message to send : ")
    client.send(request.encode())
    if request.upper() == End_chat:
        print("Disconnected........ from client side")
        break
        
    response = client.recv(1024).decode()
    print(f"Resposne : {response}".rjust(50))
    if response.upper() == End_chat:
        print("Disconnected ......... from server side")
        break

client.close()






