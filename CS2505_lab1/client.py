# from the socket module import all
from socket import *

domain_name = getfqdn()
ip_address = gethostbyname(getfqdn())
print(f"The domain name is {domain_name}. The hostname is {ip_address}")

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
sock = socket(AF_INET, SOCK_STREAM)

# set values for host 'localhost' - meaning this machine and port number 10000
# the machine address and port number have to be the same as the server is using.
#server_address = (ip_address, 10000)
server_address = ("192.168.43.175", 10000)
# output to terminal some info on the address details
print('connecting to server at %s port %s' % server_address)
# Connect the socket to the host and port
sock.connect(server_address)


try:
    
    # Send data
    #message = 'This is the message.  It will be repeated, over and over again'
    message = str(input("Enter your message: "))
    print('sending "%s"' % message)
    # Data is transmitted to the server with sendall()
    # encode() function returns bytes object
    sock.sendall(message.encode())

    # Look for the response
    amount_received = 0
    amount_expected = int(sock.recv(16).decode())
    #amount_expected = len(message)
    
    while amount_received < amount_expected:
    	# Data is read from the connection with recv()
        # decode() function returns string object
        data = sock.recv(16).decode()
        amount_received += len(data)
        print('received "%s"' % data)

finally:
    print('closing socket')
    sock.close()