#importing socket module
import socket
#importing json module
import json
#importing Thread from threading
from threading import Thread
import sys
class Client:
    '''
    TCP Client socket according to Secure communication Protocols
    '''
    def __init__(self,IP,Port= 8082):
        '''
        initializing server IP and Port

        :param IP: server IP Address
        :param Port: Server Port
        '''

        self.server_IP = IP
        self.server_Port = Port
        self.user_ID = None
        self.port = 8088
        self.connect_to_server()

    def connect_to_server(self):
        '''
        Creating a client socket and
        connecting to server using server IP and Port
        '''

        # Creating a client socket
        # creating a TCP type and  IPV4 faimly Socket
        self.client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        #Connecting to Server
        self.client.connect((self.server_IP,self.server_Port))
        print(f"Connected to server at {self.server_IP}")



    def processing_requests(self):
        '''
        processing different client requests according to predefine protocols
        '''

        #sending authentication request to server
        authentication_response = self.authentication_phase()

        #checking Status of authentication response
        if authentication_response['status'] == 'GRANTED' :
            choose = input('Do you want to connect with other user (Y or N): ')
            #closing client socket
            self.client.close()
            if choose.upper() == 'Y':
                #creating new client socket to connect with server
                self.connect_to_server()
                # Taking Lookup ID
                lookup_id = input('Enter Lookup ID : ')
                #Sending lookup request to server
                lookup_response = self.lookup_phase(lookup_id)
                # Checking Status of Lookup response
                if lookup_response['status'] == 'SUCCESS':
                    #closing client socket
                    self.client.close()
                    #Request for connection phase
                    self.connection_phase(lookup_response)
                else:
                    print('Lookup status NOTFOUND')
            else:
                #Receiving connection request
                self.connection_receive()
        else :
            print('Authentication status REFUSED')


    def authentication_phase(self):
        '''
        sending authentication request to server according to predefine protocols
        :return: response from server
        '''

        #Taking User Id and Passcode
        self.user_ID = input('Enter User ID : ')
        Passcode = input('Enter passcode : ')

        #authentication request
        request = {
            "msgtype": "AUTHREQ",
            "userid": self.user_ID,
            "passcode": Passcode
        }

        #sending authentication request to server
        self.client.send(json.dumps(request).encode('utf-8'))

        #Receiving server Response
        response = json.loads(self.client.recv(2048).decode())

        return response

    def lookup_phase(self,lookup_id):
        '''
        #Sending lookup request to server according to predefine protocols
        :param lookup_id: lookup id of user
        :return: response from the server
        '''

        #Lookup request
        request = {
            "msgtype": "LOOKUPREQ",
            "userid": self.user_ID,
            "lookup": lookup_id
        }

        #sending Lookup request to server
        self.client.send(json.dumps(request).encode('utf-8'))

        #Receiving lookup response
        response = json.loads(self.client.recv(2048).decode('utf-8'))

        return response

    def connection_phase(self,lookup):
        '''
        Sending connection request to other client
        :param lookup: lookup response from server
        '''

        #for creating local client socket
        local_client = self.create_local_client(lookup)

        #Connection request
        request = {
            "msgtype": "CONNECTREQ",
            "initiator": self.user_ID
        }

        #sending Connection request to local server
        local_client.send(json.dumps(request).encode('utf-8'))
        #closing local client socket
        local_client.close()

        #for creating local server socket
        local_client,local_server = self.create_local_server()

        #Receiving connection response from local client
        response = json.loads(local_client.recv(2048).decode('utf-8'))
        if response['status'] == 'ACCEPTED':
            #chatting phase
            self.chat(local_client)
        else:
            print('Connection REFUSED')

    def create_local_client(self,lookup):
        '''
        creating a local client socket
        :param lookup: lookup response from server
        :return: local_client socket
        '''

        #creating a TCP type and  IPV4 faimly Socket
        self.local_client = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

        local_server_IP = lookup['address']
        self.port += 1
        #Connecting to  local Server
        self.local_client.connect((local_server_IP,self.port))

        return self.local_client

    def connection_receive(self):
        '''
        Receiving connection request from other client
        '''

        #reply of connection request
        reply = {
                "msgtype": "CONNECTREPLY",
                "status": "REFUSED"
        }

        #creating local server
        client_local,local_server = self.create_local_server()

        #Receiving  connection request from local client
        request = json.loads(client_local.recv(2048).decode('utf-8'))

        #closing local server and client
        client_local.close()
        local_server.close()

        #checking connection request
        if request['msgtype'] == 'CONNECTREQ' :
            #connect to main server
            self.connect_to_server()
            #lookup into server
            response = self.lookup_phase(request['initiator'])
            #closing connection from main server
            self.client.close()

            if response['status'] == 'SUCCESS':
                reply['status'] = 'ACCEPTED'

            else:
                print('Lookup status NOTFOUND')

            #creating local client
            client_local = self.create_local_client(response)

            #Replying connection response to local server
            client_local.send(json.dumps(reply).encode('utf-8'))
            #chatting phase
            self.chat(client_local)

    def create_local_server(self):
        '''
        creating local server socket
        :return: client_local ,local_server
        '''

        # creating a TCP type and  IPV4 faimly Socket
        self.local_server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.port += 1
        #Binding local server
        self.local_server.bind( ('',self.port) )

        #local server is ready to listen or accept clients request
        self.local_server.listen()

        # accepting client request
        client_local, (client_local_IP,client_local_Port)  = self.local_server.accept()
        print(client_local_IP, client_local_Port)
        return client_local,self.local_server


    def send(self,client):
        '''
        sending message to client
        :param client: client socket
        '''

        while True:
            try:
                message = input('Enter Message : ')
                client.send(message.encode('utf-8'))
            except Exception:
                print("EXSE")
                client.close()
                break
    def receive(self,client):
        '''
        receiving message from client
        :param client: client socket
        '''
        while True:
            try :
                print("RR")
                message = client.recv(1024).decode('utf-8')
                print("receive :",message)
            except Exception:
                print('EXREC')
                client.close()
                break

    def chat(self, client):
        '''
        chatting or communication between clients
        :param client: client socket
        '''

        #creating thread of send function
        send_msg = Thread(target=self.send, args=(client,))

        # creating thread of receive function
        receive_msg = Thread(target=self.receive, args=(client,))

        try:
            #starting both the thread
            send_msg.start()
            receive_msg.start()

            send_msg.join()
            receive_msg.join()
        except Exception as e:
            print('exception')

    def __del__(self):
        self.local_client.close()
        self.local_server.close()
        del self
        print('dele')

if __name__ == '__main__':
    try :

        client = Client(input("Enter server IP : "))
        client.processing_requests()

    except KeyboardInterrupt:
        del client
        print('Closing client .....')
