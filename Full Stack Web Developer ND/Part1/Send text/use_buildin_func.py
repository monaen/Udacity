# def a function
def check_even(a):
	if a % 2 == 1:
		return False
	elif a % 2 == 0:
		return True


# def a vector
a = [1,2,3,4,5,6,7,8,9,0]

# print the even number in vector a
print(filter(check_even, a))