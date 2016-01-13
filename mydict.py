class Dict(dict):

	def __init__(self, **kw):#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
		super().__init__(**kw)

	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r'''Dict' object has no attribute '%s'''%key)

	def __setattr__(self,key,value):
		self[key]=value
		
		