# prints a string
def right_justify(s):
	print(s.rjust(70))


# prints a string
def count_char(s, c):
	print(s.lower().count(c))


# returns a list
def cumulative_sum(modifyList):
	runningTotal = 0
	newList = []
	for x in range(len(modifyList)):
		runningTotal += modifyList[x]
		newList.append(runningTotal)
	return newList


# returns True/False
def check_palindrome(s):
	if(s[::-1] == s):
		return True
	else:
		return False


def main():
	right_justify('Joseph Ismailyan')    # please put your real name

	lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla iaculis tellus id mollis scelerisque. In consequat nec tellus lacinia iaculis. Mauris auctor volutpat aliquam. Nulla dignissim arcu placerat tellus pretium, vel venenatis sem porta. Donec interdum tincidunt mi, et convallis velit aliquet eget. Nam id rutrum felis. Fusce vel fermentum justo. Pellentesque faucibus orci at velit vehicula dignissim. Duis faucibus dapibus malesuada. Pellentesque iaculis tristique vestibulum. Sed egestas nisl non augue imperdiet mattis. Nunc vitae purus lectus. Vestibulum mi turpis, volutpat vel odio quis, hendrerit suscipit ligula. Nunc in massa diam. Suspendisse aliquam quam et ex egestas vestibulum vitae id libero. Cras molestie consectetur condimentum.'
	count_char(lorem, 't')

	result = cumulative_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
	print(result)

	words_list = ['noon', 'madam', 'ams129', 'redivider', 'numpy', 'bob', 'racecar', 'youngjun']
	for word in words_list:
		if(check_palindrome(word)):
			print(word, 'is a palindrome!')

if __name__ == '__main__':	
	main()

'''
# test for right_justify(
print('-----------------right_justify()-----------------')
right_justify('stringInput')

# test for count_char()
print('\n-----------------count_char()-----------------')
stringToCount = 'I want to count how many i used in this string'
letterToCount = 'i'
count_char(stringToCount,letterToCount)

# test for cumulative_sum()
print('\n-----------------cumulative_sum()-----------------')
result = cumulative_sum([1,2,3,4,5,6,7,8,9,10])
print(result)

# test for check_palindrome()
print('\n-----------------check_palindrome()-----------------')
stringCheck = 'noon'
print(stringCheck, check_palindrome(stringCheck))
print('car', check_palindrome('car'))
'''


