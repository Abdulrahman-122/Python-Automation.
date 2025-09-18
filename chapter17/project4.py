# custom Seating Cards:
# using pillow
# create an Image for custom seating cards
# for each guest listed in guested.txt file
# generate an image file with the guest name and some flowery decoration
# Download aflower decoration image
# the image of flower you should paste into each card you will sent to each guest.
# make the size of card = 288*360 pixel
# then save card in folder called : cards for guests

# steps to finish this project:
# go through the file that contain names
# read them by readlines
# for each one write  a  his name on a custom seating card with a flower decorations
# then save this card in new folder (cards)








from PIL import Image, ImageDraw, ImageFont, ImageColor
import os

os.makedirs("cards", exist_ok=True)
names = []
with open("guests.txt", "r") as file:
    content = file.readlines()
    for name in content:
        names.append(name.strip())
print(names)

flower = "botanical-floral-element-hand-drawn-logo-with-wild-flower-and-leaves-logo-for-spa-and-beauty-salon-boutique-organic-shop-wedding-floral-designer-interior-photography-cosmetic-free-vector.jpg"
img = Image.open(flower)
copy = img.copy()
res = copy.resize((288, 200))
res.save("Update_flower.png")

for i, name in enumerate(names):
    softcream = ImageColor.getcolor("linen", "RGBA")
    newim = Image.new("RGBA", (288, 360), softcream)
    copy = newim.copy()

    Draw = ImageDraw.Draw(newim)
    fonte = ImageFont.truetype(
        "D:\python_content\python_Automation_part2\chapter17\Fonts\comicz.ttf", 20
    )
    Draw.text(
        (50, 30),
        f"Hello {name}\nthis is your custom\nseating card\nplease save it",
        fill="black",
        font=fonte,
    )
    Draw.rectangle([(0, 0), (288, 360)], outline="white", width=4)
    flower = Image.open("Update_flower.png")
    newim.paste(flower, (copy.width - flower.width, copy.height - flower.height))

    newim.save(os.path.join("cards", f"{name}-card{i+1}.png"))
print("Done.")

