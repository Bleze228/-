import random

class NoHealth (Exception):
    def __init__(self, message = "Person Is Dead"):
        Exception.__init__(self, message)


class NoMood (Exception):
    def __init__(self, message = "Person Is In Depression"):
        Exception.__init__(self, message)


class NoMoney (Exception):
    def __init__(self, message = "Person Doesn't Have Any Money"):
        Exception.__init__(self, message)

class Action:
    name = ""
    health = 0
    mood = 0
    money = 0.0
    def __init__(self, name, health, mood, money):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

class Person:
    name = ""
    health = 0
    mood = 0
    money = 0.0
    def __init__(self, name, health, mood, money):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money


    def __str__(self):
        return f"---{self.name}---\n" \
               f"health = {self.health}\n" \
               f"mood = {self.mood}\n" \
               f"money = {self.money}\n"
    def change_state(self, health, mood, money):
        self.health += health
        self.mood += mood
        self.money += money

        if self.health <= 0:
            raise NoHealth

        if self.mood <= 0:
            raise NoMood

        if self.money <= 0:
            raise NoMoney


    def do(self, action: Action):
        self.change_state(action.health, action.mood, action.money)


people = [Person, Person, Person]
people[0] = Person("Ноунейм", 100, 100, 80)
people[1] = Person("Ноунейм2", 200, 50, 100)
people[2] = Person("Ноунейм3", 300, 200, 20)

actions = [Action, Action, Action]
actions[0] = Action("Park", 10, 20, -10)
actions[1] = Action("Factory", -40, -30, 50)
actions[2] = Action("Hospital", 30, 30, -50)
print(people[0])
while True:
    try:
        r_p = random.randint(0,2)
        people[r_p].change_state(random.randint(-1, 1), random.randint(-1, 1), random.randint(-1, 1))
        print(people[r_p])
    except(NoMoney):
        print(f"Person Doesn't Have Money")
        break
    except(NoMood):
        print(f"Person is In Depression")
        break
    except(NoHealth):
        print(f"Person Is Dead\n")
        break
    except(Exception) as error:
        print(f"Error: {error}")
        break
print(people[0], people[1], people[2])