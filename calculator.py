

def calculator(number1, number2, symbol):
	
	if symbol == "+":

		answer = number1 + number2

	elif symbol == "-":

		answer = number1 - number2

	elif symbol == "*":

		answer = number1 * number2

	elif symbol == "/":

		answer = number1 / number2

	elif symbol == "**":

		answer = number1 ** number2

	return answer

number1 = "2"
number2 = "3.2"
symbol = "*"
the_answer = calculator(number1, number2, symbol)
print(the_answer)

