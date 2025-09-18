# Practice Questions:
# 1.RGBA -> is the standard fonts that computer understands
# it's four values: Red , Green , Blue  , Alpha ....
# 2. use ImageColor.getcolor('RGBA','colorname') to get the RGBA of color.
# 3. a box tuple -> is tuple with x-coordintes , y-coordinates where x -> measure the distance from left to right
# y -> increase from top to bottom, the width, the height
# 4. Image.open('zophie.png') -> return an Image object
# 5.using imageobject.size()  to find width and height of the imageobject
# 6. to exclude an amount of image say quarter of it
# use: imageobj.crop((0,50,50,50))
# 7.imageobj.save('image.ext')
# 8. we use ImageDraw module to make shape-drawing code
# 9; it has .
from PIL import ImageDraw

# imageDraw has methods like : ImageDraw.Draw() it's returned object is used to make shapes like .point()
# .line(),.rectangle()
# ---------------------------------------------
# reviation on Examples:


from PIL import ImageColor

# print(ImageColor.getcolor("red", "RGBA"))
# print(ImageColor.getcolor("green", "RGBA"))
# print(ImageColor.getcolor("yellow", "RGBA"))


# from PIL import ImageDraw, Image

# im = Image.open("zophie.png")
# print(im.size)
# print(im.height)
# print(im.width)
# print(im.filename)
# print(im.format)
# print(im.format_description)


# RGBA1 = ImageColor.getcolor("chocolate", "RGBA")
# newimage = Image.new("RGBA", (200, 200), RGBA1)
# newimage.save("newimage.png")

# RGBA1 = ImageColor.getcolor("green", "RGBA")
# newimage = Image.new("RGBA", (200, 200), RGBA1)
# newimage.save("greenimage.png")

# RGBA1 = ImageColor.getcolor("skyblue", "RGBA")
# newimage = Image.new("RGBA", (200, 200), RGBA1)
# newimage.save("skyblueimage.png")


# from PIL import Image, ImageColor

# im = Image.open("download.webp")
# copy = im.copy()
# copy.save("copy_bike.png")
# print(im.size)
# cropped = im.crop((12, 12, 300, 300))
# cropped.save("crop.png")


# im = Image.open("download (2).webp")
# copy = im.copy()
# copy.save("cop.png")
# crop = copy.crop((12, 12, 300, 300))
# paste = copy.paste(crop, (100, 100))
# copy.save("Up_copy.png")

from PIL import Image

imobj=Image.open('download (3).webp')
copy=imobj.copy()
width1,height1=copy.size
copy2=Image.open('cop.png')
cop2=copy2.resize((100,100))
cop2.save('c.png')
width2,height2=cop2.size
for left in range(0,width1,width2):
    for top in range(0,height1,height2):
        copy.paste(cop2,(left,top))


copy.save('tiled3.png')











