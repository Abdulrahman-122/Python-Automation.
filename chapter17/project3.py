# Identifying Photo Folders on the Hard Drive;
# we want to scan the entire hard drive and find the photos that you leftover and didn't use it
# search through your HD to find any folder that contains more than half photos
# and these photos it's extension should be .png or jpg or .webp
# also the photos should be it's width and height larger than 500 pixels
# so move these files to newfolder called: scatteredPhotos
#so this very useful idea to collect all your photos on the system that you forget it into one folder



import os, shutil
from PIL import Image

os.makedirs("scatteredPhotos", exist_ok=True)
photos = []
for foldername, subfolders, filenames in os.walk("D:\\"):
    print("Scannning files.....")

    for file in filenames:
        if not (
            file.endswith(".jpg") or file.endswith(".png") or file.endswith(".webp")
        ):
            continue
        filepath = os.path.join(foldername, file)
        try:
            image = Image.open(filepath)
            copyobj = image.copy()
            if (copyobj.width > 500) or (copyobj.height > 500):
                photos.append(filepath)
        except:
            continue
for photo in photos:
    shutil.move(photo, os.path.join("scatteredPhotos", os.path.basename(photo)))
print("Done...")


