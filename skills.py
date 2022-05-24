import main
import diceroller
import variables
from random import randint

"""for ttrpg game where a d100 die is rolled to determine in a players
action is successful or not. roll a d100 die, if the roll is <=
the skill chosen then it is a success if the roll > than the skill then it
is a failed roll. """

"""depending on how much lower the dice roll is lower than the
players skill it maybe a higher level success ( skill/2 = a hard success, skill/4
equals a extreme success. If the roll is between 1-5 or 95-100 it is a critical 
success or fail respectively. """

"""Throughout the world the players would face challenges more threatening or
difficult. When attempting a skill check against these obstacles it is represented
by their skill score being reduced by 10,20 or 30. They would then roll with the
same rules for success and failure still applying."""

"""Players start with 2 health. If they are attacked or otherwise suffer physicial
trauma they will loose health
"""

while main.health > 0:
    playerinput = input("select skiil from: " + variables.display + "\n")
    useraction = playerinput.split()
    userrool = randint(1, 100)


    for i in range(len(useraction)):
        if useraction[i] in variables.healthcontrol:
            if useraction[i] == "hit":
                main.health += -1
            if useraction[i] == "heal":
                main.health += 1
            if main.health <=0:
                print("RIP")

        if useraction[i] not in variables.keywords:
         break

        if useraction[i] in main.skills:
            skillval = main.skills.get(useraction[i])


        if useraction[i] in variables.penalties:
            skillval += variables.penalties.get(useraction[i])


        if useraction[i] in variables.twodie:
            userrool = diceroller.rolltwodie(useraction[i])



        if useraction[i] in main.skills:
            if userrool >= 95:
                print(userrool, "Critical Fail!")
            elif userrool > skillval:
                print(userrool, "Fail")
            elif userrool <= 5:
                print(userrool, "critical success")
            elif userrool < skillval / 4:
                print(userrool, "extreme success")
            elif userrool < skillval / 2:
                print(userrool, "hard success")
            elif userrool < skillval:
                print(userrool, "success")



