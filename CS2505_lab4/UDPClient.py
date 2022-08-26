from socket import *

ip = gethostbyname(getfqdn())
port  = 6789
server_address = (ip, port)

sock = socket(AF_INET, SOCK_DGRAM)
message = input("Enter a message: ").encode()

try:
    # sends message to server
    sock.sendto(message, server_address)


    # receives response and prints it
    response = sock.recv(1024).decode()
    print(response)
finally:
    print("end")