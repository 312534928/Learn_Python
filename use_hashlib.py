# coding: utf-8
__author__ = 'Leon.Nie'

# 返回用户输入的密码的
import hashlib

# 用于存储用户名密码
db = {}


def get_md5(str):
	md5 = hashlib.md5()
	md5.update(str.encode('utf-8'))
	return md5.hexdigest()


def register(user, pw):
	if(user in db)==False:
		db[user] = get_md5(pw + user + 'the_Salt')
		print('User %s has been registered successfully' % user)
	else:
		print('User %s has already been registered ' % user)


def login(user, pw):
	if (user in db):
		if get_md5(pw + user + 'the_Salt') == db[user]:
			print('User %s login successfully' % user)
		else:
			print('Password incorrect!')
	else:
		print('User %s doesn\'t exist' % user)



if __name__ == '__main__':
	while True:
		n = input('Choose your action, 1 or 2:\n1. Login\n2. Register\n')
		if n == '1':
			username = input('Please enter your username: ')
			password = input('Please enter your password: ')
			login(username, password)
		elif n == '2':
			username = input('Please enter your username: ')
			password = input('Please enter your password: ')
			register(username, password)
		else:
			pass