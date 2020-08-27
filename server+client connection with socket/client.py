import socket

#Almost the same setting that we applied for the server except the SERVER variable, that needs to be the server IP address where we're trying to connect

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "<INSERT SERVER IP HERE>"
ADDR = (SERVER, PORT)

#We define the same parameters that we did before and now we're using a subfield under the client variable to connect to the server based on the given
#SERVER and PORT
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

#Again the same parameters, the exception here is that we need to encode the message

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER -len(send_length))
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


#Testing the client with a disconnect message in the end
send("Hello World")
input()
send("Hello Baba")
input()

send(DISCONNECT_MESSAGE)
