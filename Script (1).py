def validate(hand):
	if hand < 0 or hand > 2:
		return False
	return True

def print_hand(hand, name='Guest'):
	hands = ['Rock', 'Paper', 'Scissor']
	print(name + ' choose: ' + hands[hand])

print('Start the Rock Paper Scissor game!')
player_name = input('Insert your name: ')

print('Choose the hand: (0: Rock, 1: Paper, 2: Scissor)')
player_hand = int(input('Insert number (0-2): '))

if validate(player_hand):
	computer_hand = 2 #you can change the number

	print_hand(player_hand, player_name)
	print_hand(computer_hand, 'Computer')

else:
	print('Please input the right number')