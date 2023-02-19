from pytube import YouTube
from tkinter import *
def YoutubeDownloader(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    youtubeObject.download()
    label_2 = Label(root,text="Task Completed").pack()
root = Tk()
root.title("Youtube to MP4 Downloader")
label_1 = Label(root,text="Youtube Link Input").pack()
link= StringVar()
link1 = Entry(root,textvariable=link).pack()
button = Button(root,text="Convert to MP4",command=YoutubeDownloader).pack()
root.geometry("300x100")
root.mainloop()