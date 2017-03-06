from random import randrange
print("this is a dice game between player 1 and player 2")
player1roll=0 
player2roll=0

winnumber=3
player1win=0
player2win=0


while(player1win != winnumber and player2win != winnumber):
    player1roll=randrange(1,6)
    print(player1roll)
    player2roll=randrange(1,6)
    print(player2roll)
    if(player1roll>player2roll):
        print("player1 won the round")
        player1win += 1
    if(player1roll<player2roll):
        print("player2 won the round")
        player2win += 1
    print(player1win)
    print(player2win)
if(player1roll==winnumber):
    print("player1 won the game")
if(player2roll==winnumber):
	print("player2 won the game")