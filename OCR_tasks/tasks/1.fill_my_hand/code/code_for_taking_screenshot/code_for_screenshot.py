# Python program to take
# screenshots
  
  
import numpy as np
import cv2
import pyautogui
import pyscreenshot as ImageGrab


# img = img_np = np.array(img) #this is the array obtained from conversion
# frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
# cv2.imshow("test", frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
   

i=1
# take screenshot using pyautogui
while i < 2: 
    image = ImageGrab.grab(bbox=(100,10,400,780)) #bbox specifies specific region (bbox= x,y,width,height *starts top-left)
       
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
