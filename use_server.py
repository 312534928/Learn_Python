import socket
import threading
import time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 监听端口:127.0.0.1绑定到本机地址,客户端必须同时在本机运行才能连接

s.bind(('127.0.0.3', 9999))
s.listen(5)
print('Waiting for connection...')

def tcplink(sock,addr):
	print('Accept new connection from %s:%s...'%addr)
	sock.send(b'Welcome')
	while True:
		data=sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8')=='exit':
			break
		sock.send(('Hello,%s!' %data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('Connection from %s:%s closed' %addr)
def main():
	while True:
		# 接受一个新连接:
		sock, addr = s.accept()
		# 创建新线程来处理TCP连接:
		t=threading.Thread(target=tcplink,args=(sock,addr))
		t.start()

main()

