print("~~~~~~~~~~~||`````````````||~~~~~~~~~~~~")
print("ENUM! How intelligent are you? Let's see!")
print("~~~~~~~~~~~||`````````````||~~~~~~~~~~~~")

program = True
count = 0
attempt = 0

while program:

	userChoice = int(input("Pick a question numbered from [1-10] and 0 to exit"))

	match (userChoice):

		case 1:
			print("  Q1. Who was the first to get to the moon?")
			print("A. Herbert Macaulay")
			print("B. James D. Collins")
			print("C. Spinf Heizer")
			print("D. Neil Armstrong")

			q1_answer = input()

			if q1_answer == "D" or q1_answer == "d":
				print("Correct!")
				count +=count 
		
			else:
				print("Wrong answer. 1 more try: ")
				q1_answer = input()
			#break
			attempt += attempt
		case 2:
			print("  Q2. How many months are in two and a half years?")
			print("A. 20")
			print("B. 14")
			print("C. 29")
			print("D. 30")

			q2_answer  = input()

			if q2_answer  == "D" or  q2_answer  == "d":
				print("Correct!")
				count +=count 
			else:
				print("Wrong answer. 1 more try: ")
				q2_answer  = input()
			
			#break
			attempt += attempt
		case 3:
			print("  Q3. 200 +1324 = ?")
			print("A. 1524")
			print("B. 1440")
			print("C. 2930")
			print("D. 3014")

			q3_answer = input()

			if q3_answer == "A" or  q3_answer == "a":
				print("Correct!")
				count +=count 
			else:
				print("Wrong answer. 1 more try: ")
				q3_answer = input()
			
			#break
			attempt += attempt

		case 4:
			print("  Q4. Who betrayed Jesus?")
			print("A. Thomas")
			print("B. Zacheus")
			print("C. Judas")
			print("D. Barnabas")
		
			q4_answer = input()

			if q4_answer == "C" or q4_answer == "c":
				print("Correct!")
				count +=count 
			else:
				print("Wrong answer. 1 more try: ")
				q4_answer = input()
			
			#break
			attempt += attempt


		case 5:
			print("  Q5. Which of the following is not a fruit?")
			print("A. Cucumber")
			print("B. Carrot")
			print("C. Cashew")
			print("D. Coconut")

			q5_answer = input()

			if q5_answer == "B" or q5_answer == "b":
				print("Correct!")
				count +=count 
			else:
				print("Wrong answer. 1 more try: ")
				q5_answer = input()
			
			#break
			attempt += attempt


		case 6:
			print("  Q6. How long does it take for the earth to revolve round the sun ?")
			print("A. 365 days")
			print("B. 72hours")
			print("C. 24hours")
			print("D. 50 days")

			q6_answer = input()

			if q6_answer == "C" or q6_answer == "c":
				print("Correct!")
				count +=count 
			else:
				print("Wrong answer. 1 more try: ")
				q6_answer = input()
			
			#break
			attempt += attempt


		case 7:
			print("  Q7. What is 24 in roman numerals?")
			print("A. XIV")
			print("B. IVX")
			print("C. XXIV")
			print("D. VIXX")	

			q7_answer = input()

			if q7_answer == "C" or q7_answer == "c":
				print("Correct!")
				count +=count 
			else:
				print("Wrong answer. 1 more try: ")
				q7_answer = input()
				
			#break	
			attempt += attempt

		case 8:
			print("  Q3. 200 +1324 = ?")
			print("A. 1524")
			print("B. 1440")
			print("C. 2930")
			print("D. 3014")
			
			q8_answer = input()

			if q8_answer == "A" or q8_answer == "a":
				print("Correct!")
				count +=count 
			else:
				print("Wrong answer. 1 more try: ")
				q8_answer = input()
			
			#break
			attempt += attempt

		case 9:
			print("  Q9. How many trimester does a preganant woman go through?")
			print("A. 5")
			print("B. 3")
			print("C. 2")
			print("D. 9")
		
			q9_answer = input()

			if q9_answer == "B" or q9_answer == "b":
				print("Correct!")
				count +=count 
			else:
				print("Wrong answer. 1 more try: ")
				q9_answer = input()
		
			#break
			attempt += attempt


		case 10:
			print("  Q10. In what year did Nigeria gain her independence?")
			print("A. 1950")
			print("B. 1930")
			print("C. 1960")
			print("D. 1984")

			q10_answer = input()
			if q10_answer == "C" or q10_answer == "c":
				print("Correct!")
				count +=count 
			else:
				print("Wrong answer. 1 more try: ")
				q10_answer = input()
			
			#break
			attempt += attempt

		case 0:
			program = False
			print("Exiting... Thank you!")	

			#break

		case _:
			print("Invalid input. Enter number 1-10")

print(f"You scored {count} / {attempt}.")
	
	