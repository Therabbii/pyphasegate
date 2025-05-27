
 
program = True

while(program):
	message = """
		
	===To-Do List Manager===
	1 -> Add a task
	2 -> View tasks
	3 -> Mark as complete
	4 -> Delete a task
	5  -> Exit
		""" 

	print(message)

	user_input = input("Enter your choice: ") 
		
	match user_input:
		case 1: 
			add_a_task = True
			#while(add_a_task):