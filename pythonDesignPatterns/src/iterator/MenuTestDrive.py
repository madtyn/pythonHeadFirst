from iterator.waitress import Waitress
from menus import *

if __name__ == '__main__':
	pancakeHouseMenu = PancakeHouseMenu()
	dinerMenu = DinerMenu()
	cafeMenu = CafeMenu()

	waitress = Waitress(pancakeHouseMenu, dinerMenu, cafeMenu)

	waitress.printMenu()
	waitress.printVegetarianMenu()

	print "\nCustomer asks, is the Hotdog vegetarian?"
	print "waitress says: "
	if waitress.isItemVegetarian("Hotdog"):
		print "Yes"
	else:
		print "No"

	print "\nCustomer asks, are the Waffles vegetarian?"
	print "waitress says: "
	if waitress.isItemVegetarian("Waffles"):
		print "Yes"
	else:
		print "No"



