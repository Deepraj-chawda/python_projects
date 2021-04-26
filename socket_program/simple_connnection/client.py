#!/usr/bin/env python
# coding: utf-8


import socket

client = socket.socket()

server_ip = input("Enter server IP : ")
server_port = int(input("Enter a server port : "))

client.connect( (server_ip, server_port) )

print("Connected to Server at ",server_ip)

request = input("Enter a message to send : ").encode()

client.send(request)

response = client.recv(1024).decode()
print("Resposne : ",response)

client.close()







