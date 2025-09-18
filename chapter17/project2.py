# EXtending and fixing : (Adding logo to the image)
# fix your program : to use accept also the .Gif and .BMP
# the program modify : .Gif , .BMP if these extensions are lower values
# also put the logo at the bottom-right corner
# modify the size to make the image twice the logo in width and height before the logo is added
# otherwise don't add the logo

# find all images from your os.listdir with extentions(jpg,png,Gif,BMP,webp)as lower extention
# make new folder to catch updated images with logo
# open each image -> make a copy of it
# then resize the cat logo to be small  (the size of image should be twice that of image or more)
# then add the logo to the bottom right of each image
# save the image to the newfolder
# loop through all images

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



#Now you can apply this logo on any image you want to add logo to it.