import random
#
# def guess(x):
# 	random_number = random.randint(1, x)
# 	guess = 0
# 	while guess != random_number:
# 		guess = int(input(f'Tell me your number between 1 and {x}: '))
# 		if guess < random_number:
# 			print("Bad, too low")
# 		elif guess > random_number:
# 			print("Bad, Too high")
# 	print(f"Good Job, the number was {random_number}")
# guess(50)

def computer_guess(x):
	low = 1
	high = x
	feedback = ''
	while feedback != 'c':
		if low != high:
			guess = random.randint(low, high)
		else:
			guess = low # could also be high b/c low = high
		feedback = input(f'Is {guess} to high (H), too low (L), or correct (C)?? '.lower)
		if feedback == 'h':
			high = guess - 1
		elif feedback == 'l':
			low = guess + 1
	print(f'Congratulations! Computer guessed your number, {guess}, correctly!')

computer_guess(10)