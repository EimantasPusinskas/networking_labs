from socket import *
import sys

# saves the clients' input from the terminal as variables
server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]
#print(f"{server_host}:{server_port}/{filename}")

# creates a socket connection
sock = socket(AF_INET, SOCK_STREAM)
server_address = (server_host, server_port)
sock.connect(server_address)

try:
    while True:

        # sends get request for the required file
        request = f"GET /{filename} HTTP/1.1\r\n\r\n" 
        sock.sendall(request.encode())

        # receives the file, decodes and then prints
        # its contents in the terminal
        Response = ""
        while True:
            packet = sock.recv(16).decode()
            if len(packet) == 0:
                break
            Response += packet
        print(Response)
finally:
    sock.close()
    print("connection closed")
