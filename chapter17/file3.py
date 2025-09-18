# Resizing an Image;
# we use resize() to resize the imageobj
# we resize it with the specified width and height
# it takes two-integer in one tuple
# it's not edit the original image in place but instead returns a new image object.
from PIL import Image

orig = Image.open("zophie.png")
width, height = (
    orig.size
)  # note: you can say: width=orig[0] and height=orig[1] as you say size with image return a tuple

resizedorig = orig.resize((int(width / 2), int(height / 2)))
resizedorig.save("resized1.png")
resized2 = orig.resize((width, height + 300))
resized2.save("resized2.png")


# Rotating and Flipping Images:
# using rotate() -> to rotate the image counterclockwise
# it leave the original image and make new imageobj
# it take onevalue(degree of rotation)
from PIL import Image

orig = Image.open("zophie.png")
rotated1 = orig.rotate(90)
rotated1.save("Rotated90.png")
orig.rotate(180).save("Rotated2.png")
orig.rotate(270).save("Rotated3.png")
orig.rotate(360).save("Rotated4.png")


# you noticed when you rotate the image by 90 and 270 the size of image is decreased (width,height)
# to solve this problem (size decreased as the image rotate)-> use argument with rotate called: expand=True
# which make expand for image to occupy the original size of right image


orig.rotate(90, expand=True).save("Rotated90.png")
orig.rotate(270, expand=True).save("Rotated3.png")
orig.rotate(6).save("Rotate6.png")
orig.rotate(6, expand=True).save("Up_Rotate6.png")

# to flip the image -> flip merror it we use transpose()
# with transpose() pass either - FLIP_LEFT_RIGHT (transpose image horizontally)
# or using FLIP_TOP_BOTTOM -> which transpose image vertically
orig.transpose(Image.FLIP_LEFT_RIGHT).save("Horizontall_Flip.png")
orig.transpose(Image.FLIP_TOP_BOTTOM).save("Vertical_Flip.png")

# Changing Individual Pixels:
# The color of individual pixel can be retrieved or set with getpixel() and putpixel()
# these methods take x,y coordinates of pixel
# putpixel() -> takes an additional tuple for the color of the pixel
# and this tuple may be four integer RGBA tuple or three integer RGB tuple
from PIL import Image, ImageColor

newimage = Image.new("RGBA", (100, 100))  # make image with height=100, width=100
print(newimage.getpixel((0, 0)))
print(newimage.getpixel((10, 30)))
print(newimage.getpixel((90, 90)))
# you will notice that the RGBA for all pixel is none =0 as the image is not colored it's transparented
# to color each pixel in the image we will use nested loops
for x in range(100):
    for y in range(
        50
    ):  # here we color the upper part from the image with light graycolor
        newimage.putpixel((x, y), (210, 210, 210))
# now lets shape the bottom part from the image with darkgray
for x in range(100):  # as the x is the width still the same as the upper loop
    for y in range(50, 100):  # make the loop start from pixel number 50 to 100
        # use ImageColor.getcolor () to get the tuple of dark gray as putpixel doesn't accept the name of color
        Darkgray = ImageColor.getcolor("darkgray",'RGBA')  # return a tuple
        newimage.putpixel((x, y), Darkgray)
newimage.save("grayedimage.png")

