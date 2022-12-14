from pytube import YouTube
from tkinter import *

BG_COLOUR = "#F2E5E5"
RED = "#EB455F"
LIGHT_PINK = "#E8C4C4"
MAROON = "#9C254D"
FONT_NAME = "Courier"

def get_streams():
    def download_stream():
        print("Starting Download...")
        filepath = streams.get_by_itag(value.get()).download(file_path_entry.get())
        print(f"Download Complete\n"
              f"Filepath: {filepath}")

    print("Searching...")

    # get progressive streams
    global streams
    url = url_entry.get()
    yt = YouTube(url)
    streams = yt.streams.filter(file_extension='mp4', progressive=True)
    progressive_streams = []
    for stream in streams:
        add = (stream.itag, stream.resolution, stream.fps)
        progressive_streams.append(add)

    # does sth to make radio buttons work, copied it somewhere
    value = IntVar()
    value.set(1)

    # show all options
    choose_label = Label(text="Choose video resolution to download:", font=(FONT_NAME, 13), fg=RED, bg=BG_COLOUR)
    choose_label.grid(row=4, column=0, columnspan=3, pady=5)
    pos = 5
    for itag, res, fps in progressive_streams:
        Radiobutton(text=f"Resolution: {res}, {fps}fps", indicatoron=False,
                    font=(FONT_NAME, 10), fg=MAROON, bg=LIGHT_PINK, padx=80,
                    variable=value, command=download_stream, value=itag
                    ).grid(row=pos, column=0, columnspan=3, pady=3)
        pos += 1
    print("Search Complete")

window = Tk()
window.title("YouTube Downloader")
window.config(padx=100, pady=50, bg=BG_COLOUR)

# label
title_label = Label(text="YouTube Downloader", font=(FONT_NAME, 20, "bold"), fg=RED, bg=BG_COLOUR)
link_label = Label(text="YouTube Link", font=(FONT_NAME, 15), fg=MAROON, bg=BG_COLOUR)
file_path_label = Label(text="File Destination", font=(FONT_NAME, 15), fg=MAROON, bg=BG_COLOUR)

title_label.grid(row=0, column=0, columnspan=3, pady=20)
link_label.grid(row=1, column=0, padx=10)
file_path_label.grid(row=2, column=0, padx=10)

# entry
url_entry = Entry(width=20, font=(FONT_NAME, 12))
file_path_entry = Entry(width=20, font=(FONT_NAME, 12))

url_entry.grid(row=1, column=1, columnspan=2)
file_path_entry.grid(row=2, column=1, columnspan=2)

# button
search_btn = Button(text="Search", font=(FONT_NAME, 13), command=get_streams, fg=MAROON, bg=LIGHT_PINK)

search_btn.grid(row=3, column=0, columnspan=3, pady=10)

window.mainloop()