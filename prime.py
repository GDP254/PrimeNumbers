#Print prime numbers to given number
def getPrime(num):
	#Start from one since 0 is not a prime number
	count = 1
	while count <= num:
		if count % 2 > 0:
			print(count)
		count += 2

getPrime(56)
