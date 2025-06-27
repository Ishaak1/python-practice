import random as rd

def cpu_vs_you(cpu, shoot):
	
	display = ""	
	cpu_word_length = len(cpu)
	user_word_length = len(shoot)
	space_betweem = 6 * " "
	odd_num_cpu = (((12 - cpu_word_length) - 1) // 2)
	even_num_cpu = (12 - cpu_word_length) // 2
	odd_num_you = ((11 - user_word_length) - 1) // 2
	even_num_you = ((11 - user_word_length)) // 2
	space_behind1 = odd_num_cpu + 1
	space_behind2 = odd_num_you + 1
	
	if cpu_word_length % 2 != 0:

		display += "|" + (" " * odd_num_cpu) + cpu + (" " * space_behind1) + "|"
		display += space_betweem
			
	elif cpu_word_length % 2 == 0:

		display += "|" + (" " * even_num_cpu) + cpu + (" " * even_num_cpu) + "|"
		display += space_betweem

	if user_word_length % 2 != 0:

		display += "|" + (" " * even_num_you) + shoot + (" " * even_num_you) + "|"

	elif user_word_length % 2 == 0:
		
		display += "|" + (" " * odd_num_you) + shoot + (" " * space_behind2) + "|"
	
	print(display)

def display(computer, you):

	print(f"~~~~~~~~~~~~~~      ~~~~~~~~~~~~~")
	print(f"|  COMPUTER  |      |    YOU    |")
	print(f"~~~~~~~~~~~~~~  vs  ~~~~~~~~~~~~~")
	cpu_vs_you(computer, you)
	print(f"~~~~~~~~~~~~~~      ~~~~~~~~~~~~~")	

def rock_paper_scissors():

	signs = ["rock", "paper", "scissors"]
	computer = rd.choice(signs)
	shoot = input("rock, paper, scissors - shoot: ")

	while shoot.strip().lower() not in signs:
	
		shoot = input("rock, paper, scissors - shoot: ")

	if computer == "paper" and shoot == "rock":
		
		display(computer, shoot)
		print(f"\n{computer.upper()} beats {shoot.upper()}, you lose")

	elif computer == "rock" and shoot == "scissors":

		display(computer, shoot)
		print(f"\n{computer.upper()} beats {shoot.upper()}, you lose")

	elif computer == "scissors" and shoot == "paper":

		display(computer, shoot)
		print(f"\n{computer.upper()} beats {shoot.upper()}, you lose")

	elif computer == shoot:
		
		display(computer, shoot)
		print(f"\n{computer.upper()} ties with {shoot.upper()}")

	else:

		display(computer, shoot)
		print(f"\n{shoot.upper()} beats {computer.upper()}, you win")


rock_paper_scissors()
