def res(n,a,m):
	list = []
	
	list.append(name)
	list.append(age)
	list.append(marks)
	
	return list

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
marks = int(input("Please enter your marks: "))

a = res(name,age,marks)


op = int(input("For 1-name 2-age 3-marks 4-exit: "))

for i in a:

	if op == 1:
		print("Your name is: ", a[0])
		break
	
	elif op == 2:
		print("Your age is: ", a[1])
		break

	elif op == 3:
		print("Your marks are: ", a[2])
		break
	
	elif op == 4:
		print("Thank you!")
		break	
			
	else:
		print("Invalid input")
		


	