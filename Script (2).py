def validate(hand):
	if hand < 0 or hand > 2:
		return False
	return True

def print_hand(hand, name='Guest'):
	hands = ['Rock', 'Paper', 'Scissor']
	print(name + ' choose: ' + hands[hand])

def judge(player, computer):
	if player == computer:
		return 'Draw'
	elif player == 0 and computer == 1:
		return ' Lose'
	elif player == 1 and computer == 2:
		return 'Lose'
	elif player == 2 and computer == 0:
		return 'Lose'
	else:
		return 'Win'

print('Start the Rock Paper Scissor game!')
player_name = input('Insert your name: ')

print('Choose the hand: (0: Rock, 1: Paper, 2: Scissor)')
player_hand = int(input('Insert the number (0-2): '))

if validate(player_hand):
	computer_hand = 1 #you can change the number

	print_hand(player_hand, player_name)
	print_hand(computer_hand, 'Computer')

	result = judge(player_hand, computer_hand)

	print('Result: ' + result)
else:
	print('Please insert the right number')