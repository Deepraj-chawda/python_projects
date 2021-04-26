import socket
from threading import Thread

class Client() :
    def __init__(self):
        self.client = socket.socket()

        self.server_ip = input("Enter Server IP : ")
        self.server_port = int(input("Enter Server port : "))
        self.END = "BYE"
        self.Flag = False
    
    def receive(self,client):
        
        while True:
         
            if self.Flag:
                break
            else:
                response = client.recv(1024).decode()
                print('server:',response.rjust(50))
            if response.upper() == self.END:
                    self.Flag = True
                    
                    break
        
            
           

    def send(self,client):
       
        while True:
           
            if self.Flag:
                break
            else:
                message = input('client: ')
                client.send(message.encode())
            if message.upper() == self.END :
                self.Flag = True
                
                break  
        
    def run(self):
      
        self.client.connect( (self.server_ip,self.server_port))

        print("Connected to Server at ",self.server_ip)
        
        
        send = Thread(target = self.send, args = (self.client,) )
        receive = Thread(target = self.receive, args = (self.client,))
        
        send.start()
        receive.start()

        send.join()
        receive.join()


        self.client.close()
        
client1 = Client()
client1.run()