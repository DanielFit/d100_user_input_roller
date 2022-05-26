import main
import advantage_diceroller

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
    player_input = input("select skiil from: " + variables.display + "\n")
    user_action = player_input.split()
    user_roll = randint(1, 100)

    selected_skill = next((value for value in set(main.skills).intersection(user_action)), None)
    selected_penalty = next((value for value in set(variables.penalties).intersection(user_action)), None)
    selected_health_control = next((value for value in set(variables.healthcontrol).intersection(user_action)), None)
    selected_advantage = next((value for value in set(variables.twodie).intersection(user_action)), None)

    if not selected_skill and not selected_penalty and not selected_health_control and not selected_advantage:
        break

    if selected_health_control:
        if selected_health_control in variables.healthcontrol:
            if selected_health_control == "hit":
                main.health += -1
            if selected_health_control == "heal":
                main.health += 1
            if main.health <=0:
                print("RIP")

    if selected_skill:
        skill_val = main.skills.get(selected_skill)

    if selected_penalty:
        skill_val += variables.penalties.get(selected_penalty)

    if selected_advantage:
        user_roll = advantage_diceroller.roll_two_die(selected_advantage)

    if selected_skill:
        if user_roll >= 95:
            print(user_roll, "Critical Fail!")
        elif user_roll > skill_val:
            print(user_roll, "Fail")
        elif user_roll <= 5:
            print(user_roll, "critical success")
        elif user_roll < skill_val / 4:
            print(user_roll, "extreme success")
        elif user_roll < skill_val / 2:
            print(user_roll, "hard success")
        elif user_roll < skill_val:
            print(user_roll, "success")
