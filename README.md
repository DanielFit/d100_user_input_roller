# dice_rolling_game
This project will only require the zip folder to be downloaded for use.
It will be able to be run on any application that runs Python 3
To use the simply open the "main.py" file and run.
This a program designed to roll dice and determine an outcome for a game action for Dungeons and Dragons or similar games that primarily use dice rolls and character statistics
This game will use a 100-sided dice and players would attempt to roll <= to their skill score to succeed.
Initially players will load a character file (char1.py and char2.py are included as examples) that will have a number to denote what number the character needs to roll to succeed.
They will then enter the name of the skill they wish to attempt i.e "strength" and that number will be checked against their roll and an outcome.
The game master can apply penalties (easy, medium, hard) or advantages (rolling two dice and taking the better result) in this case the player would enter their score and the appropriate key word found in the variables.py file i.e. "Strength adv" checks two dice rolls against a players strength score to see if ether are successful.
Depending how much lower the roll is then the players skill they may get a hard success or extreme success indicating they not only pass the skill check but gain some other advantage. 
If they players take any damage over the course of the game, they can enter "hit" deducting 1 health and similarly "heal" to regain 1 health.
