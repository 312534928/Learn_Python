import os
print(os.getcwd())
# 'r'    open for reading (default)
# 'w'    open for writing, truncating the file first
# 'x'    open for exclusive creation, failing if the file already exists
# 'a'    open for writing, appending to the end of the file if it exists
# 'b'    binary mode
# 't'    text mode (default)
# '+'    open a disk file for updating (reading and writing)
# 'U'    universal newlines mode (deprecated)
with open('hello.txt') as f:
	print(f.read())

with open('hello.txt','w') as f:
	f.write('Hello world!\n')

with open('hello.txt','a') as f:
	f.write('Hello Leon!')
