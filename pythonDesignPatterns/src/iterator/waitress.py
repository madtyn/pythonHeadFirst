
class Waitress():
	def __init__(self, pancakeHouseMenu, dinerMenu, cafeMenu):
		self.pancakeHouseMenu = pancakeHouseMenu
		self.dinerMenu = dinerMenu
		self.cafeMenu = cafeMenu


	def printMenu(self):
		pancakeIterator = self.pancakeHouseMenu.createIterator()
		dinerIterator = self.dinerMenu.createIterator()
		cafeIterator = self.cafeMenu.createIterator()

		print "MENU\n----\nBREAKFAST"
		self.__printMenu(pancakeIterator)
		print "\nLUNCH"
		self.__printMenu(dinerIterator)
		print "\nDINNER"
		self.__printMenu(cafeIterator)


	def __printMenu(self, iterator):
		while iterator.hasNext():
			menuItem = iterator.next()
			print menuItem.getName() + ", "
			print menuItem.getPrice() + " -- "
			print menuItem.getDescription()



	def printVegetarianMenu(self):
		print "\nVEGETARIAN MENU\n---------------"
		self.__printVegetarianMenu(self.pancakeHouseMenu.createIterator())
		self.__printVegetarianMenu(self.dinerMenu.createIterator())
		self.__printVegetarianMenu(self.cafeMenu.createIterator())


	def isItemVegetarian(self, name):
		pancakeIterator = self.pancakeHouseMenu.createIterator()
		if self.__isVegetarian(name, pancakeIterator):
			return True

		dinerIterator = self.dinerMenu.createIterator()
		if self.__isVegetarian(name, dinerIterator):
			return True

		cafeIterator = self.cafeMenu.createIterator()
		if self.__isVegetarian(name, cafeIterator):
			return True

		return False



	def __printVegetarianMenu(self, iterator):
		while iterator.hasNext():
			menuItem = iterator.next()
			if menuItem.isVegetarian():
				menuItem.getName() + ", "
				menuItem.getPrice() + " -- "
				menuItem.getDescription()




	def __isVegetarian(self, name, iterator):
		while iterator.hasNext():
			menuItem = iterator.next()
			if menuItem.getName().equals(name):
				if menuItem.isVegetarian():
					return True

		return False


# ^^ WaitressCafeMain
# ^^ WaitressCafe
