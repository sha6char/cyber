import os
import socket
from tkinter import filedialog



#create a server side socket using IPV4 (AF_INET) and TCP(SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#how do get ip aaddress dynamically
print(socket.gethostname())#hostname

print (socket.gethostbyname(socket.gethostname()))#ip of the given hostname
#bind the socket to tuple(ip,port)

server_socket.bind((socket.gethostbyname(socket.gethostname()),12345))

#put the socket on listening mode
server_socket.listen()

#Listen forever
os.chdir("C:\\Users\\sha6c\\OneDrive\\מסמכים\\GitHub\\cyber\\server_folder")
while True:
    client_socket, client_address = server_socket.accept()
    print(type(client_socket))
    print(client_socket)
    print(type(client_address))
    print(client_address)

    print(f"Connected to {client_address}!\n ")
    
   
    client_socket.send("You are connected".encode("utf-8")) #send a message to the client
    answer= client_socket.recv(1024).decode()
    print(answer)
    
    def recieve():
        global client_socket
        file_name = client_socket.recv(1024).decode()
        print (file_name)
      #  file_size = client_socket.recv(991024).decode()
      #  print("size "+file_size)
        file = open(file_name, "wb")
        file_bytes = b""
        done = False
        while not done:
            data = client_socket.recv(1024)
            if file_bytes[-5:]==b"<END>":
                done = True
            else:
                file_bytes += data
        file.write(file_bytes)
        file.close()
        server_socket.close()
    def ServerToClient():
        global server_socket
        global client_socket
        server_socket.close()        
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #connect the sockt to a server located at a given Ip and port
        client_socket.connect((socket.gethostbyname(socket.gethostname()),12346))
    def sendD():
        global client_socket
        which_file= client_socket.recv(1024).decode() 
        ServerToClient()               
        print ("which file "+which_file)
        list = os.listdir("C:\\Users\\sha6c\\OneDrive\\מסמכים\\GitHub\\cyber\\server_folder")
        print (list)
        for i in range (len(list)-1):
            if (which_file==list[i]):
                print ("file was found")
                file1 = open(which_file,"rb")
                file1_size =os.path.getsize(which_file)
                file1_size_str = str(file1_size)
                name= which_file
                client_socket.send(name.encode())
                client_socket.send(file1_size_str.encode())
                data1 = file1.read()
                client_socket.sendall(data1)
                client_socket.send(b"<END>")
                file1.close()
                client_socket.close()
            else:
                print("file was not found")
    if(answer=='s'):
        recieve()
    if (answer=='r'):
        sendD()
        


        