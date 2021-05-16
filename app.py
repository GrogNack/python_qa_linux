import socket
import random

test_socket = socket.socket()
port = random.randint(20000, 30000)

test_socket.bind(('127.0.0.1', port))
print("Started socket on", port)

test_socket.listen(5)

connection, address = test_socket.accept()
print("Connect", connection, address)

data = connection.recv(1024)

connection.send(b'HTTP/1.1 200 OK\r\nConnection: keep-alive\r\nContent-length: 4036\r\n\r\n<H3>Request Headers</H3><p>Host: 127.0.0.1:23925<br />User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0<br />Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8<br />Accept-Language: en-US,en;q=0.5<br />Accept-Encoding: gzip, deflate<br />Connection: keep-alive<br />Upgrade-Insecure-Requests: 1</p>')


