'''

f: function which we want the root of 
df: derivative of the function
initial_guess: initial point of x
threshhold: error tolerance

'''
def newtons(f, df, initial_guess, threshhold):
	steps = 0
	guess = initial_guess + 0.0
	dx = []
	dx.append(guess)

	print('  n|', 'x|'.rjust(22), 'dx'.rjust(21))
	print('-------------------------------------------------')
	print((str(steps) + '|').rjust(4), (str(guess) + '|').rjust(22), str(guess).rjust(21))

	guess = guess - f(guess)/df(guess)
	dx.append(guess)
	steps += 1

	while ((abs(dx[steps] - dx[steps-1])) > threshhold):
		print((str(steps) + '|').rjust(4), (str(guess) + '|').rjust(22), (str(abs(dx[steps] - dx[steps-1]))).rjust(21))
		guess = guess - f(guess)/df(guess)
		dx.append(guess)

		steps+=1

	# have to print this out separately because we're no longer in the while loop
	print((str(steps) + '|').rjust(4), (str(dx[-1]) + '|').rjust(22), str(abs(dx[-1] - dx[-2])).rjust(21))

	return None




