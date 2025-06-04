
program = True

print("Welcome to Semicolon Employee Payroll!")

employee_name = []
hours_worked_list = []
pay_rate_list = []
federal_rate = []
state_rate = []

while(program):

	print("\n========================================")
	print("	1. Add employee Payroll")
	print("	2. View employee Payroll")
	print("	3. Update employee Payroll")
	print("	4. Exit")
	print("========================================")

	print()

	userInput = int(input("Enter 1-4: "))

	match (userInput):
		case 1: 
			name = input("Enter Employee Name: ")
			employee_name.append(name)

			hours_worked = int(input("Enter number of hours worked in a week: "))
			if hours_worked  <= 40 and hours_worked  > 1:
				hours_worked_list.append(hours_worked)
			else:
				while(hours_worked  > 40 and hours_worked  < 1):
					print("Hours worked cannot be above 40hrs or below 1hr: ")
					#hoursWorked = timmy.nextInt()
			
			pay_rate = float(input("Enter hourly pay rate: "))
			pay_rate_list.append(pay_rate)

			federal_tax_rate = float(input("Enter the federal tax withholding rate: "))
			federal_rate.append(federal_tax_rate)

			state_tax_rate = float(input("Enter the state tax withholding rate: "))
			state_rate.append(state_tax_rate)

			print()
			print("\nEmployee payroll added ============>")

			

		case 2:
			
			if(employee_name.len == 0):
				print("No employees addedd.")
			 

			else:

				print("Employee name: ")

				print(employee_name(0))
	
				print(f"Hours worked {hours_worked_list(0)}")
							
				print(f"Pay Rate:${pay_rate_list(0)}")
			

				gross_pay = hours_worked_list(0) * pay_rate_list(0)
				print(f"Gross Pay: ${gross_pay}")

				test_federal = federal_rate(0)
				test_state = state_rate(0)
		
				federal_tax_reduction = test_federal / 100 * gross_pay
				state_tax_reduction = test_state / 100 * gross_pay



				print("Deductions: ")
				print(f"   Federal withholding: ${federal_tax_reduction}")
				print(f"   State withholding: ${state_tax_reduction}")
	
				total_deduction = federal_tax_reduction + state_tax_reduction

				print(f"   Total Deduction: ${total_deduction}")

				print()
		
				net_pay = gross_pay - total_deduction;

				System.out.printf("Net Pay: ${netPay}")
		

		case 3:
			print("Update employee payroll.")
		
		case 4:
			print("Exiting... Thank you!")
			program = False
		
		case _:
			print("Invalid input.")
		
	
	