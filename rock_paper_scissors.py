import random as rd

def format_result(cpu, shoot):
	
	display = ""	
	cpu_word_length = len(cpu)
	user_word_length = len(shoot)
	space_betweem = 6 * " "
	cpu_total_spaces = 12
	you_total_spaces = 11
	remaining_space_cpu = cpu_total_spaces - cpu_word_length
	remaining_space_you = you_total_spaces - user_word_length
	
	if cpu_word_length % 2 != 0:
		
		prefix_space = (remaining_space_cpu - 1) // 2
		suffix_space = prefix_space + 1
		display += "|" + (" " * prefix_space) + cpu + (" " * suffix_space) + "|"
		display += space_betweem
			
	elif cpu_word_length % 2 == 0:

		open_space = remaining_space_cpu // 2
		display += "|" + (" " * open_space) + cpu + (" " * open_space) + "|"
		display += space_betweem

	if user_word_length % 2 != 0:

		open_space = remaining_space_you // 2
		display += "|" + (" " * open_space) + shoot + (" " * open_space) + "|"

	elif user_word_length % 2 == 0:
		
		prefix_space = (remaining_space_you - 1) // 2
		suffix_space = prefix_space + 1
		display += "|" + (" " * prefix_space) + shoot + (" " * suffix_space) + "|"
	
	print(display)

def display(computer, you):

	print(f"~~~~~~~~~~~~~~      ~~~~~~~~~~~~~")
	print(f"|  COMPUTER  |      |    YOU    |")
	print(f"~~~~~~~~~~~~~~  vs  ~~~~~~~~~~~~~")
	format_result(computer, you)
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
