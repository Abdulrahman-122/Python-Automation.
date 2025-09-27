# Controlling your computer Through Email:
# write a program that checks you email account every 15 min for any instructions get to you
# and execute these instructions automatically
# ex; qBitorrent is a pear to pear downloading system
# using free BitTorrent such as qBittorrent
# you can download large media on yout home computer
# If you email the program : BitTorrent link 
# the program will check it's email , find this message
# extract the link -> then launch qBittorrent to start downloading the file
# so now your computer begin downloads while you're away
# download can be finish by the time you return home
# 
# qbProcess = subprocess.Popen(['C:\\Program Files (x86)\\qBittorrent\\
# qbittorrent.exe', 'shakespeare_complete_works.torrent'])
# 
# so what you want from this program:
# make sure that qBittottent check that the email came from you
# and the email should contain on a password
# so you should delete all emails it finds so it doesn't repeat the instruction everytime it checks the emails 
# and 
# the program should email or text you  a confirmation it executes a command 
# as you away from pc and this tell you that 
# it’s a good idea to use the logging functions (see 
# Chapter 10) to write a text file log that you can check if errors come up
# 
# qBittorrent as other BitTorrent apps -> can quit automatically after the download completes
# 
# you will use time.wait() to block untill qBittorrent has stopped
# then your program can email or text you that download has completed.
# 
# 
