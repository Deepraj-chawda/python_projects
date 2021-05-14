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

request = client.recv(1024).decode()

print("Client request :>> ",request)

message = input("Enter a message to send : ").encode()

client.send(message)

client.close()
server.close()







