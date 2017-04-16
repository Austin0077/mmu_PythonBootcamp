
def startwithAndendwithmethod():
	student ="omambia"
	print('suppose we have this sentence')
	print(student)

	print('my name starts with: o')
	print(student.startswith('o'))

	print('my name ends with: o')
	print(student.endswith('a'))

	print('use of the startwith() and the endwith() methods')
	print('alternative to the == operators \n if you want to check the starting and the end characte ods aa string')
	print('Enjoy python:')
startwithAndendwithmethod()


print('\n')
print('The join() and split() methods')
print('\n')

def join_split():
	student1 = 'omambia'
	student2 = 'joshua'
	student3 = 'omete'
	student4 = 'mokandu'
	student5 = 'felix'
	student = 'he has a good program amongst all'

	print('The jooin() method')
	print('mmu '.join([student1,student2,student3,student4,student5]))

	print("The split() method")

	print(student.split(''))
join_split()

