"""
Graphical interface to download YouTube videos using a URL link.
"""

import tkinter
import customtkinter
from pytube import YouTube


def start_download():
    """
    Starts downloading a YouTube video using the link provided in the text box.
    Updates the interface with the video title and download status.
    Shows error messages if the link is invalid.
    """
    try:
        yt_link = link_box.get()
        yt_object = YouTube(yt_link, on_progress_callback=on_progress)
        video = yt_object.streams.get_highest_resolution()
        title_txt.configure(text=yt_object.title)
        if video:
            video.download()
        else:
            raise Exception("No video stream found.")

    except:
        info_txt.configure(
            text="Download error.\nThe provided YouTube link is invalid.",
            text_color="red",
        )
        print("The provided YouTube link is invalid.")

    else:
        info_txt.configure(text="Download completed.", text_color="green")
        print("Download completed.")


def on_progress(stream, chunk, bytes_remaining):
    """
    Updates the progress bar and percentage text during the video download.
    """
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining

    percentage_downloaded = (bytes_downloaded / total_size) * 100
    percentage_str = str(int(percentage_downloaded))

    progress_txt.configure(text="{}%".format(percentage_str))
    progress_txt.update()
    progress_bar.set(float(percentage_downloaded / 100))


# UI constructor
window = customtkinter.CTk()
window.title("YouTube Downloader")

# Title label
title_txt = customtkinter.CTkLabel(window, text="YouTube Downloader")
title_txt.pack(padx=30, pady=5)

# Entry box for YouTube link
url_var = tkinter.StringVar()
link_box = customtkinter.CTkEntry(
    window,
    width=480,
    height=30,
    placeholder_text="Enter URL",
    placeholder_text_color="gray",
    textvariable=url_var,
)
link_box.pack(padx=30, pady=5)

# Label to show download progress percentage
progress_txt = customtkinter.CTkLabel(window, text="0%")
progress_txt.pack(padx=30, pady=5)

# Progress bar
progress_bar = customtkinter.CTkProgressBar(window, width=480)
progress_bar.set(0.0)
progress_bar.pack()

# Label to show information or error messages
info_txt = customtkinter.CTkLabel(window, text="")
info_txt.pack(padx=30, pady=5)

# Button to start download
download_btn = customtkinter.CTkButton(window, text="Download", command=start_download)
download_btn.pack(padx=30, pady=5)

# Placeholder for future features
# TODO: Add settings panel for download location and format

if __name__ == "__main__":
    # Appearance and theme configuration
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("dark-blue")
    window.mainloop()
