def get_balance(balance):
	balance = int(input())

def withdrawal_amount(balance , amount_to_withdraw):
	
	if amount_to_withdraw < balance:	
		balance = balance - amount_to_withdraw - 100
		return balance


print("Welcome to TimChoco Microfinance Bank!")
balance = float(input("Enter your account balance(#100 and above): "))
while balance < 100:
	balance = float(input("Enter an amount above #100: "))
print(f"Your current balance is #{balance}.")

print("<><><><><><><><><><><><><><>")

sum_withdrawal = []

program = True
while(program):

	display_1 = """
		What do you want to do?
	1. Make withdrawal
	2. Check transaction history
	3. Exit
	"""
	print(display_1)
	user_selection = int(input("Make a selection: "))

	match (user_selection):
		case 1: 
			amount_to_withdraw = float(input("Enter amount to withdraw(Fixed charge of #100): "))

			while(amount_to_withdraw > balance):
				amount_to_withdraw = float(input("Insufficient funds. Enter an amount lesser than your balance: "))
				sum_withdrawal.append(amount_to_withdraw)
			while(amount_to_withdraw > 20000):
				amount_to_withdraw = float(input("You cannot withdraw above #20,000. Enter an amount lesser: "))

				while(amount_to_withdraw > balance):
					amount_to_withdraw = float(input("Insufficient funds. Enter an amount lesser than your balance: "))
				sum_withdrawal.append(amount_to_withdraw)
				break

			while (amount_to_withdraw % 500 != 0 and amount_to_withdraw % 1000 != 0):
				amount_to_withdraw = float(input("Enter amount in multiples of #500 and #1000: "))
				while(amount_to_withdraw > balance):
					amount_to_withdraw = float(input("Insufficient funds. Enter an amount lesser than your balance: "))
				while(amount_to_withdraw < 100):
					amount_to_withdraw = float(input("Enter amount greater than 100: "))
					while(amount_to_withdraw > balance):
						amount_to_withdraw = float(input("Insufficient funds. Enter an amount lesser than your balance: "))
						while (amount_to_withdraw % 500 != 0 and amount_to_withdraw % 1000 != 0):
							amount_to_withdraw = float(input("Enter amount in multiples of #500 and #1000: "))
							sum_withdrawal.append(amount_to_withdraw)
				break


			balance = withdrawal_amount(balance , amount_to_withdraw)

			print("Transaction successful!")
			print(f"You withdrew #{amount_to_withdraw}.")
			print("Withdrawal fee: #100") 
			print(f"Your balance is #{balance}.")
		 
		#case 2:
			print(sum_withdrawal)
			
		case 3:
			program = False
			print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
			print("Thank you for banking with us! For customer complaint, contact 09000011123.")
			print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
			
		
		
		
