def get_menu_list():

	#program = True

	#while(program):
		message = """
		=== To-Do List Manager ===
		1 -> Add a task
		2 -> View tasks
		3 -> Mark as complete
		4 -> Delete a task
		5 -> Exit
		""" 
		print(message)

	user_input = input("Enter your choice: ") 
		
def add_task():
	get_menu_list()
	user_input = input("Enter your choice: ") 
	match user_input:
		case "1":
			String[] tasks = {"Buy groceries" , "take a nap"}
			
		case "2":
			print(1)
		case "3":
			print(1)
		case "4":
			print(1)
		case "5":
			print("Exiting...")
			program = False
		case _:
			print("Invalid input")

