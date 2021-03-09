import pyperclip,pyshorteners
from tkinter import *


root=Tk()
root.geometry("400*200")
root.title("URL SHORENER")

def urlshortener():
    urladdress=url.get()
    url_short=pyshorteners.Shortener().tinyurl.short(urladdress)url_address.set(url_short)

def copyurl():
    url_short=url
    pyperclip.copy(url_short)

Label(root,Text="My URL shortner",font="poppins").pack(pady=10)
Entry(root,textvariable=url).pack(pady=5)
Button(root,text="Generate short URL",command=urlshortener()).pack(pady=7)
Entry(root,textvariable="url_address").pack(pady=5)
Button(root,text="Copy URL",command=copyurl).pack(pady=5)

root.mainloop()

