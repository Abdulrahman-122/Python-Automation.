# Adding a Logo:
#
# you want to add to the bottom right corner of each image in the working directory the logo image
# which: a black cat icon with a white border where the rest of an image is transparent
# the program should do:
# load the logo image
# loop over the png , jpg fies in working dir
# check whether the image is wider or taller than 300pixels
# if so -: reduce the width or height to 300 pixels and scale down the other properties
# paste the logo image in the corner
# save the altered images to another folder
#
# so we will do again:
# open the logo image
# loop over the files by using os.listdir('.')
# get the width and height from the size  attribute
# calculate the new width and height of the resized image
# call resize () to resize the image
# call paste() to paste the logo
# call save() to save the changes
#
import os
from PIL import Image

logo = "cop.png"
logoobj = Image.open(logo)
logo_copy = logoobj.copy()
Up_logo = logo_copy.crop((0, 0, 100, 100))
Up_logo.save("Up_logo.png")

os.makedirs("For_logo2", exist_ok=True)

for file in os.listdir("."):
    if (
        not (file.endswith(".jpg") or file.endswith(".png") or file.endswith(".webp"))
    ) or file == "Up_logo.png":
        continue

    imobj = Image.open(file)
    copy1 = imobj.copy()
    logo = "Up_logo.png"
    log_obj = Image.open(logo)
    copy2 = log_obj.copy()
    cop = copy1.paste(copy2, (copy1.width - copy2.width, copy1.height - copy2.height))
    copy1.save(os.path.join("for_logo2", file))

print("Done")


