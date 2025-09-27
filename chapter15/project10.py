# Scheduled Web Comic Downloader:
# see the last updated comics to the comic website
# and then automatically download it since last visit
# using yout operating system's scheduler(Task scheduled on windows)
# can run your python program once a day
# then download the comics that last updated
# How the python works:
# see How task scheduler used and attatch
# your python file that can download the comics
# but you should download the last updated ones not all of them again
# then put a time on Task scheduler to run your code eachday

import os, requests, bs4, threading
 
os.makedirs(
    "XKCD", exist_ok=True
)  # make a dir to store comics images in it(if it found prevent error(exist_ok=True))
stop_event = threading.Event()


def Download_Xkcd(startcomic, endcomic):
    for urlNumber in range(startcomic, endcomic + 1):
        if stop_event.is_set():
            print(f"Thread stopping at comic:https://xkcd.com/{urlNumber}")
            return None
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
            if not os.path.exists(
                os.path.basename(Imgsrc)
            ):  # check if the comic image found on this folder if not downloaded
                print(f"Downloading the comic:{FullUrl}")
                res = requests.get(FullUrl)
                res.raise_for_status()
                with open(
                    os.path.join("XKCD", os.path.basename(FullUrl)), "wb"
                ) as file1:
                    for chunk in res.iter_content(100000):
                        file1.write(chunk)
                    file1.close()
            else:
                print(f"This comic image {os.path.basename(Imgsrc)} skipping it.")


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
    stop_event.set()

# now we need to see How to download the last updated comics from the website not all of them again
# attach this file to task Scheduler on your windows and make a time for this program eachday


#
#
#
#
#
#
