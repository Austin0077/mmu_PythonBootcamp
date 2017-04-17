import sys
import os
import random

class Person:

	Title = ['Dr','Mr','sir','Mrs','Ms']

	def __init__(self, title, name, surname):

		if title not in self.Title:
			raise valueError("%s is not a valid title." %title)

		self.title = title
		self.name = name
		self.surname = surname

	def getdetails(self):
		details = self.title + self.name +self.surname

		return details

	def setdetails():
		self.title = raw_input()
		self.name = raw_input()
		self.surname = raw_input()

# print(Person())
p = Person('mr', 'Omambia' 'Mogaka')
print(p.setdetails())
print(p.getdetails())
