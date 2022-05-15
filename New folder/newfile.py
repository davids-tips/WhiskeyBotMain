import urllib.request
from PIL import Image  
import PIL
print(urllib.request.urlretrieve("https://bit.ly/3oAeohK"))
image = PIL.Image.open("new.png")
image.show()
print('image sucess')