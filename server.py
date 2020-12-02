import socket
from threading import Thread

DISCONNECT_MESSAGE = "DISCONNECT !"
PORT = 8080
SERVER = "localhost"
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)


def client(conn, addr):
    print("[NEW CONNECTION] {} {} Connected".format(conn, addr))
    connected = True
    while connected:
        message = "Hi"
        message = message.encode(FORMAT)
        conn.send(message)
        msg = conn.recv(1024).decode("utf-8")
        if msg == DISCONNECT_MESSAGE:
            connected = False
        print(msg)
    conn.close()


def start_server():
    server.listen(1)
    print("[LISTENING TO SERVER] {}".format(SERVER))

    while True:
        conn, addr = server.accept()
        thread1 = Thread(target=client, args=(conn, addr))
        thread1.start()


print("SERVER IS STARTING...")
start_server()
