"""
plo6_pre_flop_play_logic.py


Steps in theory: 
- Autoclick on each of the 6 cards (detect suit by colour) and fill in suit_list
- Detect what number it is for the card number (how??- need to find code to do this) 



Practical steps to achieve the above: 
Sub task 1: 
- take screenshot, open screenshot, then use clicker to detect colour and fill in suit_list.

Noticed that the way to do the colours is that for: 
- Green: G > 100, all else < 100 
- Red: R > 100, all else < 100 
- Blue: B > 100, all else < 100 
- Black: all < 100

Take a pic of just the cards, the smaller the better, so that the surroundings won;t be picked up. 

Sub task 2:
- click on each of the 6 cards (detect suit by colour) and fill in a list
Sub task 3:
- need to find number identifier and do same as above but with numebrs of the cards




Steps for Subtask 1:
1. After running 1.1 and 1.2 (i.e. drag screen to far right position and player joins table mannually)
2. Take screenshot

"""

