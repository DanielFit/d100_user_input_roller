from random import randint


def rolltwodie(x):
    doubleroll = [randint(1, 100), randint(1, 100)]
    adv = min(doubleroll)
    disadv = max(doubleroll)
    if x == "adv":
     return adv
    if x == "disadv":
     return disadv
    if x != adv or disadv:
        print(" try adv or disadv")
