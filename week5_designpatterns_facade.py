class OrderPreparation: 
	'''Facade'''

	def __init__(self): 
		self.prepareFood = PrepareFood() 
		self.cookFood = CookFood() 
		self.packageFood = PackageFood() 

	def prepareOrder(self): 
		self.prepareFood.gatherIngredients() 
		self.cookFood.cook() 
		self.packageFood.package() 

class PrepareFood: 
	'''Preparing the ingredients before cooking'''

	def gatherIngredients(self): 
		print("Gathering Ingredients!") 

class CookFood: 
	'''Cook ingredients before packaging'''

	def cook(self): 
		print("Cooking!") 

class PackageFood: 
	'''Take cooked food and package for delivery'''

	def package(self): 
		print("Packaging food for delivery!") 


order = OrderPreparation() 
order.prepareOrder() 