print("#####################################")
print("############ UDP CLIENT #############")
print("#####################################")

import socket

target_host = "127.0.0.1"
target_port = 8080

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data
client.sendto("AAABBBCCC", (target_host, target_port))

#receieve the data
data, addr = client.recvfrom(4096)

print(data)