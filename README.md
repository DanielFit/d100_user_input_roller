# dice_rolling_game
This project will only require the zip folder to be downloaded.

It will be able to be run on any application that runs Python.

To use the simply open the "main.py" file and run it.

This is a program designed to roll dice and determine an outcome for an action in games such as Dungeons and Dragons or similar games that primarily use dice rolls and character statistics. I created this program for the purpose of reducing the bookkeeping end of these table games. The games often rely on players cooperatively building a narrative together through choices and actions and the rhythm of these narratives can be upset by players needing to stop and count dice results, include variables, and check results. 

This game will use a 100-sided dice and players would attempt to roll <= to their skill score to succeed.

Initially players will load a character file (char1.py and char2.py are included as examples) that will have a set of skills with a statistic i.e strength: 50, to denote what number the character needs to roll to succeed at an action.

They will then enter the 'name' of the skill they wish to attempt i.e "strength" and that number will be checked against their roll and an outcome.

The game master can apply penalties (easy, medium or hard) or advantages/disadvantage (rolling two dice and taking the better/worse result) in this case the player would enter their score and the appropriate key word found in the variables.py file i.e. "Strength adv" and then checks the two dice rolls against a players strength score to see if ether roll is successful.

Depending how much lower the roll is then the players skill they may get a hard success or extreme success indicating they not only pass the skill check but gain some other advantage. Similarly, a roll of 95-100 or 1-5 is automatically consider a critical fail or critical success respectively despite a players skill score. This represents a particularly good success or bad fail.

If they players take any damage over the course of the game, they can enter "hit" deducting 1 health and similarly "heal" to regain 1 health.
