print('_'*65)
print('Narrative Bot')
name = input('What is your name?')
grade = input('What is your grade?')
grade = int(grade)
if grade >= 65:
	print (name + ', your final grade in AP Computer Science is ' + str(grade) + '%. You have excelled in all components of the class!' 
		'I wish you continued success in the next semester of AP Computer Science!')
else:
	print (name + ', your  final grade in AP Computer Science is ' + str(grade) + '%. This is largely a result of missing projects and homework assignments.'
		' Unfortunately, because this grade is less than a 65, you will have to complete an MBA assignment next semester.')
