import random

def guess(x):
	random_number = random.randint(1, x)
	guess = 0
	while guess != random_number:
		guess = int(input(f'Tell me your number between 1 and {x}: '))
		if guess < random_number:
			print("Bad, too low")
		elif guess > random_number:
			print("Bad, Too high")
	print(f"Good Job, the number was {random_number}")
guess(10)
