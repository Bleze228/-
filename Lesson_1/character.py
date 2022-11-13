class Character:
    name = ''
    health = 100
    damage = 1
    defence = 0

    def __init__(self, name='', heath=100, damage=1, defence=0):
        self.name = name
        self.health = heath
        self.damage = damage
        self.defence = defence

    def __str__(self):
        return f'== {self.name} ==\n' \
               f'Здоровье: {self.health}\n' \
               f'Урон: {self.damage}\n' \
               f'Защита: {self.defence}\n'

    def take_damage(self, damage):
        self.health -= max(damage, 0)

    def attack(self, target):
        target.take_damage(self.damage)