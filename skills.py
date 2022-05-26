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


class Game:
    def __init__(self, skills: dict[str, int], health: int):
        self.player_skills: dict[str, int] = skills
        self.player_health: int = health

    def start_game_loop(self):
        while self.player_health > 0:
            user_input = self.get_user_input()
            user_roll = self.roll_dice()

            selected_skill = self.first_or_default(self.player_skills, user_input)
            selected_penalty = self.first_or_default(variables.penalties, user_input)
            selected_health_control = self.first_or_default(variables.healthcontrol, user_input)
            selected_advantage = self.first_or_default(variables.twodie, user_input)

            if not selected_skill:
                break

            if selected_health_control:
                self.resolve_player_health(selected_health_control)

            skill_val = self.player_skills.get(selected_skill)

            if selected_penalty:
                skill_val += variables.penalties.get(selected_penalty)

            if selected_advantage:
                user_roll = advantage_diceroller.roll_two_die(selected_advantage)

            self.resolve_dice_roll(user_roll, skill_val)

    def roll_dice(self):
        return randint(1, 100)

    def resolve_player_health(self, selected_health_control):
        if selected_health_control == "hit":
            self.player_health += -1
        if selected_health_control == "heal":
            self.player_health += 1
        if self.player_health <= 0:
            print("RIP")

    def resolve_dice_roll(self, user_roll, skill_val):
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

    def get_user_input(self):
        player_input = input("select skill from: " + variables.display + "\n")
        return player_input.split()

    def first_or_default(self, collection_a: dict | list, collection_b: list):
        return next((value for value in set(collection_a).intersection(collection_b)), None)
