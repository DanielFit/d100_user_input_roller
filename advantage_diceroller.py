"""
This functions purpose is provide the lower or higher number of two dice rolls, 
with advantage providing the lower number and disadvantage providing the higher number.
"""

from random import randint


def roll_two_die(x):
    double_roll = [randint(1, 100), randint(1, 100)]
    adv = min(double_roll)
    disadv = max(double_roll)
    if x == "adv":
     return adv
    if x == "disadv":
     return disadv
    if x != "adv" or "disadv":
        print(" try adv or disadv")
