# from the socket module import all
from socket import *

domain_name = getfqdn()
ip_address = gethostbyname(getfqdn())
print(f"The domain name is {domain_name}. The hostname is {ip_address}")


# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
sock = socket(AF_INET, SOCK_STREAM)
# if we did not import everything from socket, then we would have to write the previous line as:
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set values for host 'localhost' - meaning this machine and port number 10000
server_address = (ip_address, 10000)
# output to terminal some info on the address details
print('*** Server is starting up on %s port %s ***' % server_address)
# Bind the socket to the host and port
sock.bind(server_address)

# Listen for one incoming connections to the server
sock.listen(1)



# we want the server to run all the time, so set up a forever true while loop
while True:

    # Now the server waits for a connection
    print('*** Waiting for a connection ***')
    # accept() returns an open connection between the server and client, along with the address of the client
    connection, client_address = sock.accept()
    
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
           
            # data received from client 
            amount_received = 0
            amount_expected = int(connection.recv(16).decode())
   
            while amount_received < amount_expected:
                data = connection.recv(16).decode()
                amount_received += len(data)
                print(f"Received: {data}")


            # data sent to client
            message = str(input("Enter your message: "))

            message_length = str(len(message))
            connection.sendall(message_length.encode())

            print(f"Sending: {message}")
            connection.sendall(message.encode())
                
            

    finally:  
        print('no more data from', client_address)  
        connection.close()


# now close the socket

sock.close();
