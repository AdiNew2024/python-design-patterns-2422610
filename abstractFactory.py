class Dog:
	"""One of the objects to be returned"""

	def speak(self):
		return "Woof!"

	def __str__(self):
		return "Dog"

class Cat:

	def speak(self):
		return "Meow!"

	def __str__(self):
		return "Cat"

class DogFactory:
	"""Concrete Factory"""

	def get_pet(self):
		"""Returns dog object"""
		return Dog()
	
	def get_food(self):
		"""Returns dog food object"""
		return "Dog Food!"

class CatFactory:

	def get_pet(self):
		return Cat()

	def get_food(self):
		return "Cat Food!"

class PetStore:
	""" PetStore houses our Abstract Factory """

	def __init__(self, pet_factory=None):
		""" pet_factory is our Abstract Factory """

		self._pet_factory = pet_factory

	def show_pet(self):
		""" Utility method to display the details of the objects retured by the DogFactory """

		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()
		
		print("Our pet is '{}'!".format(pet))
		print("Our pet says hello by '{}'".format(pet.speak()))
		print("Its food is '{}'!".format(pet_food))


#Create a Concrete Factory

factory = CatFactory()

#Create a pet store housing our Abstract Factory

store = PetStore(factory)

#Invoke the utility method to show the details of our pet

store.show_pet()