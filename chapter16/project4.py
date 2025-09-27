# Auto Unsubscriber:
# write a program to scan through your email account
# find all the unsubscribe links in all your emails
# and automatically opens them in a browser
# what you will use:
# Imap server
# use beautifulsoup to scan for word (unsubscribe) within Html link tag
# then put all of these unsubscribe links into a list
# use webbrowser.open() to open each one automatically
#
import imapclient, pyzmail, bs4, webbrowser

imapobj = imapclient.IMAPClient("imap.gmail.com", ssl=True)
print("Enter an App_Pass from Google!!!!")
Secret_password = input(">")
imapobj.login("abdulrahman11510.qasim@gmail.com", Secret_password)
imapobj.select_folder("INBOX", readonly=True)
UIDs = imapobj.search("ALL")
Urls = []
for item in UIDs:

    fetch = imapobj.fetch(item, ["BODY[]"])
    message = pyzmail.PyzMessage.factory(fetch[item][b"BODY[]"])
    if message.text_part != None:
        # print(f"This email number: ({item}) contain on Text_part")
        # print(message.text_part.get_payload().decode(message.text_part.charset))
        message.text_part.get_payload().decode(message.text_part.charset)
    if message.html_part != None:
        print(f"This email number: ({item}) contain on html_part")
        html_part = message.html_part.get_payload().decode(message.html_part.charset)
        soup = bs4.BeautifulSoup(html_part, "html.parser")
        for link in soup.find_all("a", href=True):
            if (
                "Unsubscribe" in link.text.lower()
                or "Unsubscribe" in link["href"].lower()
            ):
                print(f"Unsubscriber link found: {link['href']}")
                Urls.append(str(link["href"]))

# for Url in Urls:
#     webbrowser.open(Url)

# non compolete project now let's put them inside a list and open them and subscribe each one one by one

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
