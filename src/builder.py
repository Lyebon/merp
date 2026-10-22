from random import randint
from menu.menu import m
from character.character import Character
from character.characteristics import Characteristic
from character.skills import Skill
from data_loader import read_file

def dice(dice:int)->int:
    return randint(1,dice)



def builder():
    pass