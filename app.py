import random
import socket

test_socket = socket.socket()
port = random.randint(20000, 30000)
result_str = ''

test_socket.bind(('127.0.0.1', port))
print("Started socket on", port)

test_socket.listen(5)

connection, address = test_socket.accept()
print("Connect", connection, address)

data = connection.recv(1024)
headers = data.decode("utf-8").split("\r\n")
for header in headers:
    result_str = result_str + header + "<br />"
result_str = "HTTP/1.1\r\nHost: 127.0.0.1:25528\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\n<h3>Request Headers</h3><p>" + result_str + "</p>"
print(result_str)

connection.send(result_str.encode("utf-8"))
