"""
plo6_pre_flop_play_logic.py


Steps in theory: 
- Autoclick on each of the 6 cards (detect suit by colour) and fill in a list
- Detect what number it is for the card number (how??- need to find code to do this) 
- Then simply fill it in two lists and add it to your code. 



Practical steps to achieve the above: 
Sub task 1: 
- take screenshot
- open screenshot 
Sub task 2:
- click on each of the 6 cards (detect suit by colour) and fill in a list
Sub task 3:
- need to find number identifier and do same as above but with numebrs of the cards




Steps for Subtask 1:
1. After running 1.1 and 1.2 (i.e. drag screen to far right position and player joins table mannually)
2. Take screenshot

"""


import pyautogui

# im1 = pyautogui.screenshot()
# im2 = pyautogui.screenshot('my_screenshot.png')

pyautogui.moveTo(258,40)
pyautogui.click()


loc = None
while loc is None:
    loc=pyautogui.locateOnScreen('/Users/patrickchong/Desktop/Personal_Projects/PLO_Project/colour_project/tasks/1.fill_my_hand/ss1.png',grayscale=True, confidence=.5)

print(loc)