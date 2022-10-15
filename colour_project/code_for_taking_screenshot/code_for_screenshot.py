# Python program to take
# screenshots
  
  
import numpy as np
import cv2
import pyautogui
   

i=1
# take screenshot using pyautogui
while i < 10: 
    image = pyautogui.screenshot()
       
    # since the pyautogui takes as a 
    # PIL(pillow) and in RGB we need to 
    # convert it to numpy array and BGR 
    # so we can write it to the disk
    image = cv2.cvtColor(np.array(image),
                         cv2.COLOR_RGB2BGR)
       
    # writing it to the disk using opencv; I believe it will save to the same folder as 
    # wherever this Python file is in!
    cv2.imwrite(f"image{i}.png", image)

    i += 1
