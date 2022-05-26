from player_service import PlayerService
from skills import Game

"""
When entering an input choose fomr the list of skills as seen on the input screen below. Please
ensure any additional keywords are entered along with your skill ie: "insight adv" instead of across multiple inputs. 

If advantage or disadvantage is required simply type "adv" or "disadv".

 If a penalty is required type "easy" "medium" or "hard" 
 """
player_service = PlayerService()
display_list = player_service.get_display_list()

selected_player = None
while selected_player is None:
    print("Select player:")
    for k, v in display_list.items():
        print(f'{k} -> Health: {v.health} | Skills: {v.skills}')
    value = input('')
    try:
        value = int(value)
        if value in display_list:
            selected_player = display_list[value]
    except ValueError:
        print('Please select a valid player number')
        continue

game = Game(selected_player.skills, selected_player.health)

game.start_game_loop()


