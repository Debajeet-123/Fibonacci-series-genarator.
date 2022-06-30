def  fibonacci(n):

	if n == 1  or n == 0:

		return n;

	else:

		return fibonacci(n-2) + fibonacci(n - 1)


numero = int(input("print a possitive number: "))

if numero < 0:
	print("Numer is not valid:")

i = 0

print("fibonacci series is: ")

for i in range(0, numero):
	print(fibonacci(i))
