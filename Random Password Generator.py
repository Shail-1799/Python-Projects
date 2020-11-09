#----------------------------RANDOM PASSWORD GENERATOR--------------------------#

import random


def gen_password(length=10): # Default length = 10

	l=['!','@','#','$','%','*','^']

	lower1 = chr(random.randint(97,122))   # a to z
	sp1 = random.choice(l)
	upper = chr(random.randint(65,90))     # A to Z
	sp2 = random.choice(l)
	digits1 = random.randint(100,999)
	lower2 = chr(random.randint(97,122))   # a to z
	digits2 = random.randint(10,99)

	password = lower1+sp1+upper+sp2+str(digits1)+lower2+str(digits2)

	l1 = random.sample(password,length)   # pass length parameter upto 10 char
	password = ("").join(l1)

	return password

print(gen_password())