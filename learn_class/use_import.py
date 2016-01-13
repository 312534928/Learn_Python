import sys,os
print("+++++")
print(sys.path)
print(os.getcwd())


from use_call import Next

b=Next(2,7)
print(b(2))