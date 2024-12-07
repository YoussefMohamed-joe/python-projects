import socket
host = 'data.pr4e.org'
path = '/intro-short.txt'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, 80))

request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
s.send(request.encode())

response = s.recv(4096)

response_str = response.decode()
headers, body = response_str.split('\r\n\r\n', 1)

print("HTTP Headers:")
print(headers)
print("\nHTTP Body:")
print(body)

