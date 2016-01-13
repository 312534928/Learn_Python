import time
import threading

balance = 0
look = threading.Lock()


def change_it(n):
	global balance  # ¹²Ïí±äÁ¿balance
	balance = balance + n
	balance = balance - n


def run_thread(n):
	for i in range(100000):
		look.acquire()
		try:
			change_it(n)
		finally:
			look.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
