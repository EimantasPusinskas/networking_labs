from socket import *
import time
import statistics
import sys

num_pings = int(sys.argv[1])
ip = sys.argv[2]
port = 12000
server_address = (ip, port)

sock = socket(AF_INET, SOCK_DGRAM)

# sets the timeout value to 1 second
sock.settimeout(1)

try:
    packets_received = 0
    packets_lost = 0
    rtts = []

    print(f"PING {ip} ({ip}): {num_pings} data bytes")

    for i in range(num_pings):
        # records the time every ping is sent
        start_time = time.time()
        # sends ping to server
        sock.sendto(str(i).encode(), server_address)

        # if the packet is not lost, then 
        try:
            # the response is decoded, its time received is recorded
            response = sock.recv(4096).decode()
            rtt = time.time() - start_time
            # its rtt is calculated and added to the rtts list
            rtts.append(rtt)
            print(f"{len(str(i))} byte(s) from {ip}: udp_seq={i} time={round(rtt, 5)}ms")
            packets_received += 1 
        except:
            # otherwise if there is an exception, there is a timeout
            packets_lost += 1
            print("Request timed out")
            

    # statistics are printed to the terminal
    print(f"\n--- {ip} ping statistics ---")    
    print(f"{num_pings} packets transmitted, {packets_received} packets received, {((num_pings - packets_received) / num_pings) * 100}% packet loss")
    # two data points are required to calculate the standard deviation
    # and so if less than two packets are received from the server, the program crashes
    # thus if this scenario arises, the standard deviation is set to None since it cannot be calculated
    if len(rtts) > 1:
        std = round(statistics.stdev(rtts), 2)
    else:
        std = None
    print(f"round-trip min/avg/max/stddev = {round(min(rtts), 5)}/{round(sum(rtts)/packets_received, 5)}/{round(max(rtts), 5)}/{std} ms")
finally:
    sock.close()
    print("socket closed")