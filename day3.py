# wapp to get name age add marks from user and print

while True:
	op = int(input("1 create, 2 view , 3 exit "))
	if op == 1:
		name = input("Enter Your Name ")
		age = int(input("Enter your age "))
		add = input("Enter your address ")
		marks = int(input("enter your marks "))
	elif op == 2:
		n = int(input("1 name, 2 age, 3 address, 4 marks"))
		if n == 1:
			print("name is ", name)
		elif n == 2:
			print("age is ", age)
		elif n == 3:
			print("address is ", add)
		elif n == 4:
			print("marks are ", marks)
		else:
			print("invalid input")

	elif op == 3:
		break
	else:
		print("Invalid Input")
