from random import randint


def attack_damage(modifier):
    roll = randint(1, 8)
    return modifier + roll
