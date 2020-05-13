#install pillow package, pip3 install pillow

import sys
import os
from PIL import Image
input1=sys.argv[1]
output=sys.argv[2]
print(input1)
# create Path
if not (os.path.exists(output)):
    os.makedirs('output')
#open and save files
for item in os.listdir(input1):
    asd=os.path.splitext(item)[0]
    image1=Image.open(f'{input1}{asd}.jpg')
    image1.save(f'{output}{asd}.png','png')
    print(image1)   
