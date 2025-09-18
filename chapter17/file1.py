# Manipulation Images:
# you will use python to edit images
# and manipulate it 
# we will use pillow module to handle images
# 
# computer Image Fundamentals:
# you should know color and fonts and coordinates in images


# Colors and RGBA values:
# RGBA -> (Red,Green,Blue,alpha(transparency))
# each value of these colors from 0 to 255
# and these RGBA are assigned in pixels
# pixels -> it's the smallest dot of a single color the computer can show
# (imagine there are a million of dots on the screen)
# 
# pixels of RGBA tells what shade of color it should display
# Alpha of image determine how much you can see the background of screen that the image render on it
# ex(255,0,0,255)-> this mean the RGBA is a red color with a max alpha it's fully obeque
# if you want green -> (0,255,0,255)
# if you want blue -> (0,0,255,255)
# if you want white -> (255,255,255,255)
# if you want black -> (0,0,0,255)
# 
# if alph=0 -> this mean it's invisible 
# 
# 
# pillow offers : ImageColor.getcolor('colorname','RGBA') -> returns a tuble of RGBA 
# 
from PIL import ImageColor
color1=ImageColor.getcolor('red','RGBA')
color2=ImageColor.getcolor('yellow','RGBA')
color3=ImageColor.getcolor('green','RGBA')
color4=ImageColor.getcolor('Chocolate','RGBA')
print(color1,'\n',color2,'\n',color3,'\n',color4)
# 
# note:
# we use PIL instead of Pillow and then from it ImageColor
# we use get_color() 
# 
# 

# Coordinates and Box Tuples:
# image pixels are addressed with x-coordinates and y-coordinates
# which specify a pixel's horizontal and vertical location in an image
# the origin is the pixel at the top-left corner of the image
# it's specified with (0,0)
# the first zero represent x_coordinates which increase from left to right
# the second zero represent y_coordinates which increase from up to down the image
# 
# many of pillow methods and functions take four value to represent rectangulare region in an image inside a tuple
# the four values of Pillow :
#When Pillow (the Python image library) asks for a box tuple, it means:
# (left, top, right, bottom)


# Each number is an (x, y) coordinate in the image.

# 🔹 Coordinates in an image

# (0,0) is the top-left corner of the image.

# x → moves horizontally (to the right).

# y → moves vertically (down).

# So (left, top, right, bottom) describes a rectangle in the image.

# 🔹 Important detail

# Left = the x of the left edge.

# Top = the y of the top edge.

# Right = the x just past the right edge.

# Bottom = the y just past the bottom edge.

# That means the rectangle includes left and top but excludes right and bottom.

# 🔹 Example: (3, 1, 9, 6)

# Left = x = 3

# Top = y = 1

# Right = x = 9 → but this is excluded, so it goes up to x = 8.

# Bottom = y = 6 → but this is excluded, so it goes up to y = 5.

# So the pixels included are:

# From x = 3 to 8

# From y = 1 to 5

# That’s a rectangle of width = 9 - 3 = 6 pixels and height = 6 - 1 = 5 pixels.

# 🔹 Visualization

# If the image is a grid:

# x → 0 1 2 3 4 5 6 7 8 9
# y
# 0
# 1        [############]
# 2        [############]
# 3        [############]
# 4        [############]
# 5        [############]
# 6


# The box (3, 1, 9, 6) is the shaded rectangle.
# # 
# # 
# # 
# # 
