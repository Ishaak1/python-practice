def calculator(num1, symbol, num2):
	
	answer = 0

	if symbol == "add":

		answer = num1 + num2

	elif symbol == "subtract":

		answer = num1 - num2

	elif symbol == "multiply":

		answer = num1 * num2

	elif symbol == "divide":

		answer = num1 / num2

	elif symbol == "power":

		answer = num1 ** num2

	return answer

x = 2
symbol = "multiply"
y = 3.2
result = calculator(x, symbol, y)
print(result)
