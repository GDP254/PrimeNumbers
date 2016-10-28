#Print prime numbers to given number
def getPrime(num):
	#Start from one since 0 is not a prime number
	count = 1
	while count <= num:
		# is the modulus is beyond zero it is prime
		if count % 2 > 0:
			print(count)
		# increment by two to skip directly to the next prime number
		count += 2

getPrime(56)
