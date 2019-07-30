import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() #utf8 encoding
mysock.send(cmd)

while True:
    data = mysock.recv(512) # the data we receive is byte
    if (len(data) < 1):
        break
    print(data.decode(),end='')
mysock.close()
