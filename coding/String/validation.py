while True:
	print('Please enter your age (it must be a number)')
	age = input()
	print('Please enter your name (it must be a be a characte)')
	name = raw_input()
	if (name.isalpha()):
		print('you are loggeg in as'+ ' '+ name +' ' 'and yor age is :'+str(age))
	else:
		print('next person')
		print(' your credentials did not match. Try again!')
		break
