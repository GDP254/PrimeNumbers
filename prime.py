#Print prime numbers to given number
def getPrime(num):
	count = 1
	while count <= num:
		if count % 2 > 0:
			print(count)
		count += 2

getPrime(56)
