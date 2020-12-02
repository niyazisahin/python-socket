import socket


DISCONNECT_MESSAGE = "DISCONNECT !"
PORT = 8080
SERVER = "localhost"
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)


def send_message(message):
    msg = message.encode(FORMAT)
    msg_receive = client.recv(1024).decode(FORMAT)
    print(msg_receive)
    client.send(msg)


send_message("Hello Host. How Are You Today ? ")
send_message(DISCONNECT_MESSAGE)
