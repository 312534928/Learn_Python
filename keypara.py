def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)

person('Mike',30)
person('Mike',30,city='Beijing')
person('Mike',30,gender='M',city='Beijing')

extra={'city':'Beijing','job':'Engineer'}
person('Jack',24,city=extra['city'],job=extra['job'])
person('Jack',24,**extra)
