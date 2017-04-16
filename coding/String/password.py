import sys
import os

def passwordcheck():
	print('please choose a password for your account.')
	password = raw_input()

	while True:
		if password.isalnum():
			print('Thank you for registering,you are  logined your password being:'+password)
			print('Try again. byb providing an alphanumric password')
			break
passwordcheck()


print(' startwith() and endwith() methods')
print('\n')


