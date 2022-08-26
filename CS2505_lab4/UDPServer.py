from socket import *
from datetime import datetime

ip = gethostbyname(getfqdn())
port  = 6789

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((ip, port))

try:
    while True:
        # receives nmessage from client, decodes it and then changes all the letters to upper case
        message, client_address = serverSocket.recvfrom(1024)
        message = message.decode().upper()
        print("received: " + message)

        # writes the message and the time it was received to the log file
        date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open("log_file.txt", "a") as log_file:
            log_file.write(f"\nmessage received at: {date_time}. message: {message}")

        # sends response back to client
        message = f"server received '{message}' at {date_time}"
        serverSocket.sendto(message.encode(), client_address)
finally:
    print("end")
