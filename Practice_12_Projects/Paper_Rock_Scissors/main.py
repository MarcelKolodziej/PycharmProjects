"""basic rock, paper, scissor game vs computer"""
import random


def play():
    user = input("Type 'r' for rock, 'p' for paper, and 's' for scissors")
    computer = random.choice(['s', 'r', 'p'])
    print(f'Computer choose', {computer})

    if user == computer:
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won'


def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True

print(play())
