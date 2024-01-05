#TCP client side 
import os
import socket
from tkinter import filedialog

#create a client side socket using IPV4 (AF_INET) and TCP(SOCK_STREAM)
global client_socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the sockt to a server located at a given Ip and port
client_socket.connect((socket.gethostbyname(socket.gethostname()),12345))
print ("hi")

# recieve a message from the server..... you mast specify the max number of bytes to recieve
message = client_socket.recv(1024)
print (message.decode("utf-8"))
answer = str(input("what do you want to do niger s/r"))
client_socket.send(answer.encode())
def sendD():
    global fpath
    fpath=filedialog.askopenfile()
    fpath=fpath.name

    file = open(fpath,"rb")
    file_size =os.path.getsize(fpath)
    name =os.path.basename(fpath)
    file_size_str = str(file_size)
    client_socket.send(name.encode())
    client_socket.send(file_size_str.encode())

    data = file.read()
    client_socket.sendall(data)
    client_socket.send(b"<END>")
    file.close()
    client_socket.close()
def ClientToServer():
    global client_socket
    client_socket.close()
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((socket.gethostbyname(socket.gethostname()),12346))
    server_socket.listen()
    
def recieve():
    global client_socket
    which_file= str(input("enter the name of the file...niger!!!"))
    client_socket.send(which_file.encode())
    ClientToServer() 
   # file1_name = client_socket.recv(1024).decode()
    os.chdir("C:\\Users\\sha6c\\OneDrive\\מסמכים\\GitHub\\cyber\\resive")  
    while True:
        client_socket, client_address = server_socket.accept()
        print(type(client_socket))
        print(client_socket)
        print(type(client_address))
        print(client_address)
        print(f"Connected to {client_address}!\n ")
        file_name = client_socket.recv(1024).decode()
        #file1_size_str = client_socket.recv(102400).decode() 
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
if (answer=='s'):
    sendD()


if (answer =='r'):
    recieve()
  
    