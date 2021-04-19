import socket
from threading import Thread

class Server() :
    def __init__(self):
        self.server = socket.socket()

        self.server_ip = input("Enter Server IP : ")
        self.server_port = int(input("Enter Server port : "))
        self.END = "BYE"
        self.Flag = False
    
    
    def receive(self,client):
        
        while True:
            
            if self.Flag:
                break
            else:
                request = client.recv(1024).decode()
                print('client:',request.rjust(50))

            if request.upper() == self.END:
                self.Flag = True
            
                break
    
    def send(self,client):
        
        while True: 
            
            if self.Flag:
                break
            else:    
                message = input('server: ')
                client.send(message.encode())
            if message.upper() == self.END :
                self.Flag = True
            
                break
         

    def run(self):
        self.server.bind( (self.server_ip,self.server_port))

        self.server.listen()
        print("Server is Running ......... ")

        client , client_address = self.server.accept()

        print("Connected to client !!... ")
        print("Address of client >> ",client_address)

        send = Thread(target = self.send, args = (client,) )
        receive = Thread(target = self.receive, args = (client,))
        
        send.start()
        receive.start()

        send.join()
        receive.join()
        
    
        client.close()
        self.server.close()

server1 = Server()
server1.run()
