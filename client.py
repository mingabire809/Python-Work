from server import ADDR
import socket
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "10.5.0.107"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(message)
    send_lenght = str(msg_lenght).encode(FORMAT)
    padded_send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += b' '* (HEADER - len(send_lenght))
    client.send(send_lenght)
    client.send(message)
send("Hello Word!")
send(DISCONNECT_MESSAGE)