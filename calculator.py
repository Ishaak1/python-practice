

def calculator(number1, number2, symbol):
	
	if symbol == "add":

		answer = number1 + number2

	elif symbol == "subtract":

		answer = number1 - number2

	elif symbol == "multiply":

		answer = number1 * number2

	elif symbol == "divide":

		answer = number1 / number2

	elif symbol == "exponent":

		answer = number1 ** number2

	return answer

number1 = "2"
number2 = "3.2"
symbol = "multiply"
the_answer = calculator(number1, number2, symbol)
print(the_answer)

