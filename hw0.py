# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

a = np.loadtxt("D:\!MLML\李弘毅 class\HW0\hw0_data.dat")
b = np.transpose(a)

from PIL import Image

im=Image.open("D:\!MLML\李弘毅 class\HW0\Lena.png")
width, height = im.size
l = list(im.getdata())
rl = l[::-1]

im2 = Image.new ("RGB",(width,height), "white")

for i in range(height):
    for j in range(width):
        rgb = im.getpixel((i,j))
        im2.putpixel((height-1-i, width-1-j), rgb)

im2.save("D:\!MLML\李弘毅 class\HW0\Lena2.png")
