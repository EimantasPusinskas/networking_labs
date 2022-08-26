# from the socket module import all
from socket import *
from datetime import datetime

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

        date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open("log_file.txt", "a") as log_file:
            log_file.write(f"\nMessage Received at: {date_time}. Message: ")


        # Receive the data in small chunks and retransmit it
        while True:
            # decode() function returns string object
            data = connection.recv(16).decode()
            
            if data:
                with open("log_file.txt", "a") as log_file:
                    log_file.write(data)

                print('received "%s"' % data)
                print('sending data back to the client')

                data += f" message received at {date_time}"
                
                # sends length of data to client
                data_length = str(len(data))
                connection.send(data_length.encode())
                data = "................"

                connection.sendall(data.encode()) 
                
            else:
                print('no more data from', client_address)
                break
            
    finally:
        # Clean up the connection
        log_file.close()
        connection.close()


# now close the socket
sock.close();
log_file.close()