import random

def random_generator():
	number1 = random.randrange(1 , 100)
	number2 = random.randrange(1 , 100)

	subtraction = 0

	if number1 > number2:
		subtraction = number1 - number2
		print (number1 , "-" , number2)

	elif number1 < number2:
		numberLow = number1
		subtraction = number2 - numberLow
		print(number2 , "-" , numberLow)
	
	return subtraction

count = 0

for attempt in range(1 ,11):
	print("Question [" , attempt , "]:")
	equationAnswer = random_generator()
	userInput = int(input("What is the answer? "))
	if userInput == equationAnswer:
		count += 1

	elif userInput != equationAnswer:
		print("Second try: ")
		userInput = int(input("What is the answer? "))

print("==== You scored " , count , "/ 10 ====")

