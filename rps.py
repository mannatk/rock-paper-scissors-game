import random


print 'Welcome to Rock, Paper, Scissors!'
human_name = raw_input('What\'s your name?')
num_wins = input('How many points are required for a win?')
human_points = 0
computer_points = 0
choices_list = ['rock', 'paper', 'scissors']

while human_points != num_wins and computer_points != num_wins:
	human_choice = raw_input('Choose (R)ock, (P)aper, or (S)cissors?').lower()
	computer_choice = random.choice(choices_list)
	if human_choice == 'rock':
		if computer_choice == 'scissors':
			human_points += 1 
			winner = 'Human'
		elif computer_choice == 'paper':
			computer_points += 1
			winner = 'Computer'
		elif computer_choice == 'rock':
			winner = 'Nobody'
	elif human_choice == 'paper':
		if computer_choice == 'scissors':
			computer_points += 1 
			winner = 'Computer'
		elif computer_choice == 'paper':
			winner = 'Nobody'
		elif computer_choice == 'rock':
			human_points += 1
			winner = 'Human'
	elif human_choice == 'scissors':
		if computer_choice == 'rock':
			computer_points += 1
			winner = 'Computer'
		elif computer_choice == 'paper':
			human_points += 1
			winner = 'Human'
		elif computer_choice == 'scissors':
			winner = 'Nobody'
	if winner == 'Nobody':
		print '%s: %s Computer: %s A draw' % (human_name, human_choice, computer_choice) 
	elif winner == 'Computer':
		print 'You are incompetant at this game. Hopefully your poor performance in this game does not reflect in your life!'
		print '%s: %s Computer: %s Computer Wins!' % (human_name, human_choice, computer_choice)
	else:
		print '%s: %s Computer: %s %s Wins!' % (human_name, human_choice, computer_choice, human_name)	
	print 'Score: %s %d Computer: %d' % (human_name, human_points, computer_points)
print 'Final Score: %s %d Computer %d' % (human_name, human_points, computer_points)


















