# Manipulating images with Pillow:
# to manipulate images : use PIL and import from it Image
# then :
# image.open(imagefile)
# note image object gives you basic info about the image
# 1. width and height
# 2. the filename+graphics format(Gif or png or Jpeg)
#

from PIL import Image

catIm = Image.open("zophie.png")  # Image object
# print(catIm)
print(catIm.size)
print(catIm.height)
print(catIm.width)
print(catIm.filename)
print(catIm.format)
print(catIm.format_description)
catIm.save("zophie.jpg")

# as you see:
# you should make image object
# as you see .format_description
# explain the type of format more verbose
# with .save(.newformat or olderformat)
#
# Image.new() -> return a blank image object
# the argument to Image.new('RGBA'.(width,height),'background')
# backgroun -> is the background color that should the image start with(it's represent the four values of RGBA)
# you can return value from: Imagecolor.getcolor('colorname') and use this return value instead of argumebt
from PIL import Image, ImageColor

RGBA1 = ImageColor.getcolor("chocolate", "RGBA")

blanckImage = Image.new("RGBA", (200, 600), RGBA1)
blanckImage.save("ChocolateImage.png")
sec_blanck = Image.new("RGBA", (500, 500), "purple")
sec_blanck.save("Purple.png")
third = Image.new("RGBA", (200, 300))
third.save("blackimage.png")
# we call image.new() to create anothe image object
# if image has no background so it's called : transparent background


# Cropping Images:
# Cropping an image -> select a rectangular region inside an image + removing everything outside the rectangular.
# we use crop (tuple) 0> returns an image object represent the cropped image
# the cropping image doesn't effect on the original image
# it's instead return a new image object
# the tuple is the cropped section from the original image
# (left,top,right,bottom)


from PIL import Image, ImageColor

catIm = Image.open("zophie.png")
croppingobj = catIm.crop((335, 345, 565, 560))  # this will make a cropping  rectangular object
croppingobj.save("Cropping.png")

# Copying and Pasting Images onto other Images:
# to make a copy of the original image but don't affect it
# use copy()
from PIL import Image

catim = Image.open("zophie.png")
copyIm = catIm.copy()  # make copy image object from the original image
copyIm.save("Coppied1.png")
#
# Now you can paste an image on the top of an image
from PIL import Image

# catim = Image.open("zophie.png")
# copyim = catim.copy()
# croppedimage = copyim.crop((335, 345, 565, 560))
# copyim.paste(croppedimage, (0, 0))
# copyim.paste(croppedimage, (400, 500))
# copyim.paste(croppedimage, (100, 200))
# copyim.save("pasted_copied.png")
# print(croppingobj.size) #this create a crop rectangular obj(215,230)
#
# paste(sourceimageobject,tuple)
# tuple-> x,y of the place we put image in the original image
# note: copy(),paste() don't use your computer clibboard.
# past() doesn't change an object with onther it just put the image object at the place you specify to it.
#
# let's make a for loop to loop over the copy of orignal image
# then put a faceimage at each(215,230) in the copyone
from PIL import Image

# ori_img = Image.open("zophie.png")
# widthimg, heightimg = ori_img.size
# copy_img = ori_img.copy()
# croppedimage = copy_img.crop((335, 345, 565, 560))
# croppedimagewidth, croppedimageheight = croppedimage.size
# for left in range(0, widthimg, croppedimagewidth):
#     for top in range(0, heightimg, croppedimageheight):
#         copy_img.paste(croppedimage, (left,top))

# copy_img.save("tiled.png")
#
# we start by looping through width of copyimage and we will step by croppedimagewidth(and this is the x which move from left to right)
# we then make a loop through the height of copyimage and we will step by croppedimageheight(and this is the y which move from up to down)
# put images at each row -> then go to the next row ->untill finish all rows
# then save the image


# Pasting Transparent Pixels:
# if you want to paste a transparent image to the original image
# where you want to show the transparency in that image so you let the background image to appear as the transparency of the second image found
# so when we paste the transparen image we put it again as third argument to the paste()

from PIL import Image

ori = Image.open("zophie.jpg")
copy = ori.copy()
# trans = Image.new("RGBA", (30, 40))  # transparent image
trans = Image.new("RGBA", (30, 40), (128, 0, 128, 255))  # solid purple, alpha=255  #here we didn't make a transparent image as it's full opaque insteam you make it fully puple so if you want to use a mask PIL will ignore that and replace it by the original photo
trans.save("noimg.png")
copywidth, copyheight = copy.size
transwidth, transheight = trans.size
for left in range(0, copywidth, transwidth):
    for top in range(0, copyheight, transheight):
        copy.paste(trans, (left, top), trans)
copy.save("tiled.jpg")
# here the transparent image doesn't effect anything on the original image
# so to show the effect when you use the mask image
from PIL import Image

ori = Image.open("zophie.jpg")
copy = ori.copy()

# Create a small semi-transparent red rectangle
trans = Image.new("RGBA", (30, 40), (255, 0, 0, 128))  # RGBA with alpha=128

copywidth, copyheight = copy.size
transwidth, transheight = trans.size

for left in range(0, copywidth, transwidth):
    for top in range(0, copyheight, transheight):
        copy.paste(trans, (left, top), trans)

copy.save("tiled2.jpg")
#you see a background red over the image itself and you see the background image
#so we use the partially transparent image as mask for the original one
