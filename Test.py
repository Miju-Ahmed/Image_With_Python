def main():

	print("Hello")
	print("Hi")
	#int x;
	a = 10; b = 5; c = 15.5
	x = a + b + c
	
	
	if(x>10):
		print('x = ' + str(x)) 	#printf("x = %d\n", x)
		print('x = {}'.format(x))
	elif(x==10):
		print('x = ' + str(x)) 	#printf("x = %d\n", x)
		print('x = {}'.format(x))
	
	x = 'Bang' + 'La' + 'Deshi'
	print(x)
	
	x = [a, b, c] # List
	print(x)
	
	x, g, h = f1()
	print(h)
	_,_, h = f1()
	print(h)
	h = f1()
	print(h)
	
def f1():
	x = 10; g=30; h = 60
	
	return x, g, h

if __name__== '__main__':
	main()
