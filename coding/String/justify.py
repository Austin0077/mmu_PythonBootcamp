print('\n')
print('String jusitification, using the ljust(), rjust() and center()')
print('\n')

def  jusitification():
	number ='.'
	header ="welcome to mmu bootcamp"
	body = ''' The mmu bootcamp start at 8:00am  and end at 4:30pm today. The bootcamp's events will ne as followed;'''

	footer = ['copyright:', 'mmu_cit_club','@mmucitclub_python']

	events = ['introduction','basics', 'data types','functions','object oriented in pyhthon']

	print(header.center(50,'*'))
	print('\n')

	for x in events:
		print(number+' '+x.ljust(20,'-'))
		

	for w in footer:
		print(w.rjust(30))

jusitification()
