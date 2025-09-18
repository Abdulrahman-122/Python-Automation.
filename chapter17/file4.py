# Drawing an Images:
# to draw a circles or lines,rectangles or simple shapes over the image
# use : pillow's ImageDraw
#
from PIL import ImageDraw, Image

# im = Image.new("RGBA", (200, 200), "White")  # we make new white image object
# draw = ImageDraw.Draw(im)  # now we make Draw object

# Drawing Shapes:
# ImageDraw draw various kinds of shapes on the images
# fill,outline pars are optional and if you didn't use them ;they will be white by default
# to Draw Points:
# use: point(xy,fill) -> which xy -> the x , y coordinates for pixels you want to draw
# if you want to draw more than one point : use list of x,y with tuple for each point -> [(x1,y1),(x2,y2)...]
# or use list without tuples [x1,y1,x2,y2,x3,y3,.....]
# fill -> it's an RGBA  tuple of the color you want or use color name inside 'red' as example
# the fill as we say is optional

# Lines:
# line(xy,fill,width) draws a line or a series of lines
# xy-> list of tuple of points you want to draw and that points connect each other to make the line
# or you can make it inside alist
# fill -> RGBA value or color name
# width -> width of line and its default is 1

# Rectangles:
# rectangles(xy,fill,outline) draws a rectangle
# xy is a box tuple of (left,top,right,bottom)
# left , top -> specify the x-y coordinate of the upper-left corner of the rectangle
# right,bottom -> specify the x-y coordinate of the lower-right corner of the rectange
# fill it's an optional and it's the color that fill inside the rectangle
# outline it's an optional and it's the color of the rectangles's outline.


#  Ellips:
# ellipse(xy,fill,outline) draws an ellips
# if width , height are identical -> this method will draw a circle
# xy -> tuple of (left,top,right,bottom) is a box tuble that precisely contains the ellips
# fill -> is the color of the inside of the ellipse
# outline -> is an optional argument  is the color of the ellips's outline
# Polygons:
# polygons(xy,fill,outline)->it's draws an arbitrary polygons
# xy -> is a list of tuples -> [(x,y),(x,y),...] or [x1,y1,x2,y2,x3,y3....]
# representing the connection pointsof the polygon's sides.
# the last pair of coordinates will connected automatically to the first pair
# fill -> is the color of the inside of the polygon(it's outline)
# outline -> is the color of the polygon's outline.

from PIL import Image, ImageDraw

image = Image.new("RGBA", (200, 200), "white")
draw = ImageDraw.Draw(image)
draw.line([(0, 0), (10, 0), (20, 20), (30, 30), (199, 199)], fill="yellow", width=5)
draw.rectangle((20, 30, 60, 60), fill="blue", outline="red")
draw.ellipse((120, 30, 160, 60), fill="red", outline="black")
draw.ellipse((120, 30, 150, 80), fill="blue", outline="yellow")
draw.polygon(
    [
        (57, 87),
        (79, 62),
        (94, 85),
        (120, 90),
        (103, 113),
        (120, 90),
        (100, 200),
    ],
    fill="brown",
    outline="pink",
)
for i in range(100, 200, 10):
    draw.line([(i, 0), (200, i - 100)], fill="green", width=5)

draw.point([1, 2, 5, 9, 12, 13], fill="red")

image.save("drawing.png")

# Drawing Text;
# to draw a text on the image: we use text()fro ImageDraw()
# text() takes four arguments (xy,text,fill,font)
# xy -> is a two-integer tuple specify the upper-left corner of the text box
# text -> the string of text you want to write
# fill is the color of text
# font -> it's the Imagefont object
# it's used to set the typeface and size of text
#
# it's hard to know what size a block of text will be in a given font.
# so we use : textsize((f,s)) in ImageDraw
# it's first argument -> string you want to measure
# it's second arg -> optional ImageFont object
# then textsize() would return a two integer tuple of width and height that the text in a given font would be if it were writtin onto the image
# you can use this tuple to determine where you want to put text on the image
#
# to use font object inside text(),textsize() you should import ImageFont
#
# once tou import Imagefont module
# you can call Imagefont.truetype()->takes two args
# first arg: a string for the font's TrueType file (actual file on your hard drive)
# this file in ends in .ttf
# the folder name on your device:C:\Windows\Fonts
# you don't need to enter these paths as part of the TrueType file
# as python knows to automatically search for fonts in these directories
# second arg: integer for the font size in points(rather than pixels)
# keep in mind : by default pillow creates PNG images that are 72 pixels per inch and a point is 1/72 of an inch.
#
#
#
#


from PIL import Image, ImageDraw, ImageFont
import os

image = Image.new("RGBA", (2000, 2000), "white")
draw = ImageDraw.Draw(image)
draw.text((100, 100), "Hello man", fill="pink")

fontfile=ImageFont.truetype("D:\\python_content\\python_Automation_part2\\chapter17\\Fonts\\arial.ttf",32)
draw.text((20,150),'Struggle makes Men',fill='green',font=fontfile)
image.save("Text.png")

