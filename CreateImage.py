#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image,ImageDraw,ImageFont

img1 = Image.new("RGB", (150,50), (0x00,0x00,0x00))
draw = ImageDraw.Draw(img1)

font = ImageFont.truetype("C:\WINDOWS\Fonts\meiryo.ttc",25,encoding="utf-8")
draw.text((10,10),u'ABC日本語',fill=(0xcf,0xff,0xff),font=font)

img1.save("e:\sample633a.jpg")
img1.show()

