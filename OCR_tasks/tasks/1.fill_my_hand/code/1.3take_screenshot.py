# Program to take screenshot
from PIL import Image
import PIL
import pyscreenshot
  
# To capture the screen
image = pyscreenshot.grab()
print(type(image))
pic = Image.open("/home/pchong/Desktop/PLO6_business-main/OCR_tasks/tasks/1.fill_my_hand/code/nums_list_image/colorpic3.jpg")
  
  
# To save the screenshot
pic = pic.save("Geeksforeks.jpg")

print(pic)