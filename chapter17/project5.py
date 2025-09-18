# •	 Add text or a website URL to images.
# •	 Add timestamps to images.
# •	 Copy or move images into different folders based on their sizes.(I make it in chapter 4 but in another thought as my computer contain on scattered images in everywhere so i neglect the parameter of size and move all photos to one folder)
# •	 Add a mostly transparent watermark to an image to prevent others


# Add a URL to images on my directory:
# steps:
# loop over the images in your direct
# if images ends with jpg or png
# paste to them the url
# put URL at the bottom of each photo
# import os
# from PIL import Image, ImageDraw, ImageFont

# os.makedirs("For_Url", exist_ok=True)
# for file in os.listdir("."):
#     if not (file.endswith(".png") or file.endswith(".jpg")):
#         continue
#     if file == "cards" or file == "scattededPhotos" or file == "For_logo2":
#         continue
#     im = Image.open(file)
#     draw = ImageDraw.Draw(im)
#     fonte = ImageFont.truetype(
#         "D:\python_content\python_Automation_part2\chapter17\Fonts\comicz.ttf", 20
#     )
#     URL = "https://chatgpt.com"
#     draw.text(
#         (0, 0),
#         f"this is chatgpt\n web press on URL\n:{URL}",
#         fill="pink",
#         font=fonte,
#     )
#     im.save(os.path.join("For_Url", file))
# print("Done")


# # Add a timestamp to images on my directory:
# # steps:
# # loop over the images in your direct
# # if images ends with jpg or png
# # paste to them the url
# # put URL at the bottom of each photo
# import os, datetime
# from PIL import Image, ImageDraw, ImageFont

# os.makedirs("For_Timestamp", exist_ok=True)
# for file in os.listdir("."):
#     if not (file.endswith(".png") or file.endswith(".jpg")):
#         continue
#     if file == "cards" or file == "scattededPhotos" or file == "For_logo2":
#         continue
#     im = Image.open(file)
#     draw = ImageDraw.Draw(im)
#     fonte = ImageFont.truetype(
#         "D:\python_content\python_Automation_part2\chapter17\Fonts\comicz.ttf", 20
#     )
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     bbox = draw.textbbox(
#         (0, 0), timestamp, font=fonte
#     )  # gives a tuble of the box that contain on that text (left,top,right,bottom)
#     textwidth = bbox[2] - bbox[0]  # right-left -> give width
#     textheight = bbox[3] - bbox[1]  # bottom-top => give height of that box

#     x = (im.width - textwidth) / 2
#     y = im.height - textheight-10 # add 10 pixels for margins

#     draw.text(
#         (x, y),
#         f"{timestamp}",
#         fill="pink",
#         font=fonte,
#     )
#     im.save(os.path.join("For_Timestamp", file))
# print("Done")

# •	 Add a mostly transparent watermark to an image to prevent others


import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs("watermark", exist_ok=True)

for i, file in enumerate(os.listdir(".")):
    if not (file.endswith(".png") or file.endswith(".jpg")):
        continue
    if file in ["cards", "scattededPhotos", "For_logo2"]:
        continue

    im = Image.new("RGBA", (200, 200), "white")

    # load watermark
    watermark = Image.open("OIP.webp").convert("RGBA")

    # # resize watermark (scale it down to 1/4 width)
    # widthwm = im.width // 4
    # heightwm = int(watermark.height * (widthwm / watermark.width))
    # Up_water = watermark.resize((widthwm, heightwm), Image.LANCZOS)

    # # position at bottom-right with 10px margin
    # position = (im.width - Up_water.width - 10, im.height - Up_water.height - 10)

    # paste watermark with transparency preserved
    # im.paste(Up_water, (0, 0), mask=Up_water)
    im.paste(
        watermark,
        (im.width - watermark.width, im.height - watermark.height),     # here we added watermark at the whole page if you want to added to the right corner use positon above instead of this and open hashs lines
        mask=watermark,
    )

    # save result
    im.save(os.path.join("watermark", f"image{i}.png"))

print("Done")
