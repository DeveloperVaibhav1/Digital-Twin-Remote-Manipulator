import socket
from config import ESP_IP, PORT

sock = None

def connect():
    global sock
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ESP_IP, PORT))
        print("Connected to ESP32")
    except Exception as e:
        sock = None
        print("Connection failed:", e)


def send_data(x, y):
    global sock

    try:
        if sock is None:
            connect()
            return

        message = f"{x},{y}\n"
        sock.send(message.encode())

    except Exception as e:
        print("Connection lost, reconnecting...", e)
        sock = None