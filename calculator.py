

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

x = 2
y = 3.2
symbol = "multiply"
result = calculator(x, y, symbol)
print(result)

