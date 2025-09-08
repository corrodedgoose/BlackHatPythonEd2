import socket


# Code from book was not working with target_host set as a string
# I had to get the IP address by using socket.gethostbyname
# this way IP was returned and passed into client.connect
# target_host = 'www.google.com'

target_host = socket.gethostbyname('localhost')
# target_host = socket.gethostbyname('www.google.com')
target_port = 9998
# target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

# client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
client.send(b'Hello, Server!')

response = client.recv(4096)

print(f'{response.decode()}')

client.close()