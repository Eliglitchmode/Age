driving = input('Have you ever driven a car?')
if driving != 'Yes' and driving != 'No':
	print('You should only answer yes or no')
	raise SystemExit
age = input('How old are you?')
age = int(age)
if driving == 'Yes':
	if age >= 18:
		print('You passed the test! :D')
	else:
		print('That is weird!')
elif driving == 'No':
	if age >= 18:
		print('You are eligible to get your license!')
	else:
		print('Wait for a couple years!')
else:
	print('You should only answer yes or no')