import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect_ex(("bancocn.com", 80))
client.send(b"h w!")

ans_return = client.recv(1024)
print(ans_return)

