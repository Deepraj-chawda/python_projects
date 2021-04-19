#!/usr/bin/env python
# coding: utf-8



import socket

server = socket.socket()

server_ip = input("Enter Server IP : ")
server_port = 55555

server.bind( (server_ip,server_port))

server.listen()
print("Server is Running ......... ")

client , client_address = server.accept()

print("Connected to client !!... ")
print("Address of client >> ",client_address)

End_chat = "BYE"
while True:
    request = client.recv(1024).decode()
    print(f"Client request :>> {request}".rjust(50))
    if request.upper() == End_chat:
        print("Disconnected........ from client side")
        break
    

    message = input("Enter a message to send : ")
    client.send(message.encode())
    if message.upper() == End_chat:
        print("Disconnected ......... from server side")
        break
    

client.close()
server.close()






