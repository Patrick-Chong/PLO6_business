"""
I did a test where I pritned the size of my monitor, and it is indeed different when I didn't use 
my monitor and just used the laptop. 
Note that the top left of the screen is (0,0) and it is a x-y plane going down rightwards
"""

#Size of screen with monitor is (width=1440, height=1080)
import pyautogui, sys
print(pyautogui.size())

#Position of pkerbros (top bar where I can drag) when opened is (258,40)
print(pyautogui.position())


"""Run the following code after opening the pokerbros app"""

#Moving the pkerbros screen to the far right
pyautogui.moveTo(258,40)  #moves mourse position to this point
pyautogui.dragTo(1565, 43, button='left')  #Drags to, with button meaning if you wiant to left or right click (mostly left in my case- doesn't make sense to right click when dragging)




