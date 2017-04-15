# consider the following dictionariy
	# =======================================================
			# DICTIONARY
			# a dictionary is a list_like python data type
import pprint
import os
import sys

def struc_dict():
	student = {'omambia':'BSE', 'Hamilton':'BSC','joshua':'ENG', 'Mokandu':'SCE'}

	# Dictionary finctions :....keys(), items(), and values() methods.............:

	print(student.keys())

	print(student.values())

	print(student.items()) #this returns a tuples of the dictionary key and value

struc_dict()
	# ....using the dictionaries with the for loop to iterate throught a dictionary...#

print( '\n'*2) 
print("check a key and return either True or False:")
print( '\n'*2)

def usingfor():
	student = {'omambia':'BSE', 'Hamilton':'BSC','joshua':'ENG', 'Mokandu':'SCE'}

	for i in student.keys():
		print(i)	

	for y in student.values():
		print(y)

	for x in student.items():
		print(x)

usingfor()


# having a true list, just pass the dict_keys, dict_values, and dict_items inside 
#  a list() method

print( '\n'*2) 
print(": Getting a true list out of a dictionary, out of the keys(), items() & values() methods")
print( '\n'*2)

def true_list():
	student = {'omambia':'BSE', 'Hamilton':'BSC','joshua':'ENG', 'Mokandu':'SCE'}

	print(student.keys())

	print(student.items())

	print(student.values())

	# look at the out put is really a true list consider all the property of a list
true_list()

		# ckecking whether a key, value exists in a dictionary

print( '\n'*5)

def checking_key_if_exists():
	student = {'omambia':'BSE', 'Hamilton':'BSC','joshua':'ENG', 'Mokandu':'SCE'}

	print('omambia' in student.keys())
	print('jose' in student.keys())

	print('welcome' in student.values())
checking_key_if_exists()


		# using the get() method  dictionaries have a method that it uses to check 
		# a key exists: 
			 #it takes two arguements, 
			 		# 1. First the key to of the value to retrieve
			 		# 2. Second a fallback value to return if that key does not exists.

print( '\n'*2) 
print("checking if a value exists using the get() method: The get() takes two arguments")
print( '\n'*2)

def getMethod():
	student = {'omambia':73, 'Hamilton':34,'joshua':34, 'Mokandu':56}

	print('omambia' + ' '+ str(student.get('omambia',45)) + ' '+ 'marks in programming')

	print('Joseph' + ' '+str(student.get('jose',40)) + ' '+ 'marks in programming')
getMethod()

print( '\n'*2) 
print("setting a default value if not given : using the setdefault() method")
print( '\n'*2)

def setdefaultmethod():
	student = {'omambia':73, 'Hamilton':34,'joshua':34, 'Mokandu':56}
	print( 'Joshua'+ ' '+ str(student.setdefault('jose',35)) + ' as his marks in programming')
setdefaultmethod()

print( '\n'*2) 
print("counting characters in a sentence")
print( '\n'*2)

def character_count():
	message ='''omambia is a third year student in a mmu taking BSE. 
				He is good in programming'''
	count = {}
	for i in message:
		count.setdefault(i, 0)
		count[i] = count[i]+1
	print(count)
character_count()


# word count using python dictionary and a list
print( '\n'*2) 
print("counting words in a sentence")
print( '\n'*2)

def word_count():
	sentence ="omambia is a third year student in a mmu taking BSE. He is good in programming"
	count = {}

	sent = sentence.split()
	print(sent)
	for word in sent:
		count.setdefault(word, 0)
		count[word] = count[word]+1
	print(count)
word_count()

print( '\n'*2) 
print("Pretty Printing: ")
print( '\n')

print( '\n'*2) 
print("1. counting words in a sentence using pprint")
print( '\n'*2)

def word_count():
	sentence ="omambia is a third year student in a mmu taking BSE. He is good in programming"
	count = {}

	sent = sentence.split()
	print(sent)
	print('\n'*2)
	for word in sent:
		count.setdefault(word, 0)
		count[word] = count[word]+1
	pprint.pprint(count)
	pprint.pformat(count)
word_count()

print( '\n'*2) 
print("2. counting characters in a sentence using pprint")
print( '\n'*2)


def character_count():
	message ='''omambia is a third year student in a mmu taking BSE. 
				He is good in programming'''
	count = {}
	for i in message:
		count.setdefault(i, 0)
		count[i] = count[i]+1
	pprint.pprint(count)
	pprint.pformat(count) # pretifies the display, that is it aligns it 
character_count()