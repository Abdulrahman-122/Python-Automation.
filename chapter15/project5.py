# Multithreading XKCD Downloader:
# in this program :
# you will use multithreading to run the program
# by the way this is faster than using single thread
# as in single
# download single image at a time
# (as it esablish the network connection to download+writing the downloaded image to the hard drive) this is repeated with each image
# with multithreading:
# has some threads downloead the comics
# while the other -> establishing the network connection + writing the images to the hard drive

import os, requests, bs4, threading

os.makedirs(
    "XKCD", exist_ok=True
)  # make a dir to store comics images in it(if it found prevent error(exist_ok=True))


def Download_Xkcd(startcomic, endcomic):
    for urlNumber in range(startcomic, endcomic + 1):
        print(f"Download page https://xkcd.com/{urlNumber}.")
        res = requests.get(f"https://xkcd.com/{urlNumber}", "html.parser")
        res.raise_for_status
        soup = bs4.BeautifulSoup(res.text)
        IdElem = soup.find("div", id="comic")
        ImgElem = IdElem.find("img")
        Imgsrc = ImgElem["src"]
        FullUrl = Imgsrc
        if IdElem == []:
            print(f"No image in this url:https://xkcd.com/{urlNumber}")

        if Imgsrc.startswith("//"):
            FullUrl = "https:" + Imgsrc
        if Imgsrc:
            print(f"Downloading the comic:{FullUrl}")
            res = requests.get(FullUrl)
            res.raise_for_status()
            with open(os.path.join("XKCD", os.path.basename(FullUrl)), "wb") as file1:
                for chunk in res.iter_content(100000):
                    file1.write(chunk)
                file1.close()


Downloadthreads = []
for i in range(0, 1400, 100):
    download_thread = threading.Thread(target=Download_Xkcd, args=[i, i + 99])
    Downloadthreads.append(download_thread)
    download_thread.start()
try:
    for download_thread in Downloadthreads:
        download_thread.join()
    print("Done.")
except KeyboardInterrupt:
    print("Stopping program!!!!")

# for the part of threads
# he make a loop from 0 to 1400 with 100 step which means : i =0,100,200,300.....1399   which mean make threads (14 ones)
# then with each thread target=function ,it's arguments= (0,99),(100,199),(200,299)......(1300,1399)
# each thread will download 100 comics and this is goood
# and we make list to hold all 14 threads to it(this will need in the next part to work each one of them and stop the main untill he downlead it's comics)
# then we use .start() to open thread
#
# then we loop over each thread in the list
# and used .join to tell to the program to wait untill the first thread finish his work then second untill last one then after all of them finish
# go to main(which represent the last print('Done'))
# note:
# you can change the first loop to change how many thread you want
# but if you make many threads this will affect your cpu
# also if you make many ones this will be slow at downloading
# .join tell the program don't switch to main thread untill the 14 threads that I working finish their work
# note:
# I use try-except to force stopping the program when need not wait untill it finish
# as  the main thread is not used so when I press ctrl+c it doesn't work
# as the extra threads that I make is now working
