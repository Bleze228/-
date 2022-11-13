from character import Character

player1 = Character(name='Vasya', heath=30, damage=5, defence=0)
player2 = Character(name='Jack', heath=30, damage=3, defence=2)

print(player1)
print(player2)

player1.attack(player2)
player2.attack(player1)

print(player1)
print(player2)

while player1.health > 0 and player2.health > 0:
    player1.attack(player2)
    player2.attack(player1)
    print(player1)
    print(player2)