# Hello Guys
# Welcome to my channel
# today we will make message box from GUI (Tkinter)
#   Let's Start
from tkinter import*
from tkinter import messagebox

def click():
    messagebox.showinfo(title='Video Downloader',message='Please download the mp4 file so please click ok')
    messagebox.showinfo(message='Ha Ha Ha you are trapped as we activated a virus in your computer !!')

window=Tk()
button=Button(window,command=click,text='Please click me')
button.pack()
window.mainloop()
# So guys thank ou like and subscribe my channel
