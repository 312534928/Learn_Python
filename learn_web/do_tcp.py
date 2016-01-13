import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET 指定使用IPv4
# AF_INET6 指定使用IPv6
# socket.SOCK_STREAM面向流的TCP协议

# 80端口是Web服务的标准端口,
# SMTP服务是25端口，
# FTP服务是21端口，等等。
# 端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。

s.connect(('www.sina.com.cn', 80))  # 参数是tuple

s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer = []

while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('sina.html', 'wb') as f:
    f.write(html)
