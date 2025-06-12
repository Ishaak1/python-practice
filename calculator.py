

def calculator(number1, number2, operation):
	
	if operation == "add":

		answer = number1 + number2

	elif operation == "subtract":

		answer = number1 - number2

	elif operation == "multiply":

		answer = number1 * number2

	elif operation == "divide":

		answer = number1 / number2

	elif operation == "power":

		answer = number1 ** number2

	return answer

number1 = 2
number2 = 3.2
operation = "multiply"
the_answer = calculator(number1, number2, operation)
print(the_answer)

