from tkinter import *
import tkinter.font
from pytube import YouTube
root = Tk()
Desired_font = tkinter.font.Font( family = "Comic Sans MS",size = 20,  weight = "bold")
root.geometry('500x300')
root.resizable(0,0)
root.title("Team U16 - Youtube Video Downloader")
lbl = Label(root,text = 'Youtube Video Downloader')
lbl.pack()
 
link = StringVar()

lbl2 = Label(root, text = 'Paste Link Here:')
#lbl2.place(x= 160 , y = 60)
lbl2.pack()

link_enter = Entry(root, width = 70,textvariable = link)
#link_enter.place(x = 32, y = 90)
link_enter.pack()
 
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    lbl3 = Label(root, text = 'DOWNLOADED')
    lbl3.place(x= 180 , y = 210)  
    lbl3.configure(font = Desired_font) 

btn =Button(root,text = 'DOWNLOAD',bg = 'bisque2', padx = 2, command = Downloader)
#btn.place(x=180= ,y = 150)
btn.pack()
btn.configure(font = Desired_font) 
lbl.configure(font = Desired_font)
lbl2.configure(font = Desired_font) 

link_enter.configure(font = Desired_font)
root.mainloop()