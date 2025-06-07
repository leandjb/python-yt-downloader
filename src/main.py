"""
GUI - Graphical User Interface to download YT videos using a URL link.
"""

import tkinter
import customtkinter
import re
import pytube


def clear_fields(link_box, progress_txt, progress_bar, title_txt, info_txt):
    link_box.delete(0, tkinter.END)
    progress_txt.configure(text="0%")
    progress_bar.set(0.0)
    title_txt.configure(text="YouTube Downloader")
    info_txt.configure(text="")


def update_progress(stream, chunk, bytes_remaining, progress_txt, progress_bar):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_downloaded = (bytes_downloaded / total_size) * 100
    percentage_str = str(int(percentage_downloaded))
    progress_txt.configure(text="{}%".format(percentage_str))
    progress_txt.update()
    progress_bar.set(float(percentage_downloaded / 100))


def is_valid_youtube_url(url):
    # Basic check for YouTube URL
    pattern = r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$"
    return re.match(pattern, url) is not None


def download_video(link_box, progress_txt, progress_bar, title_txt, info_txt):
    yt_link = link_box.get().strip()
    if not yt_link:
        info_txt.configure(
            text="Please enter a YouTube URL.",
            text_color="orange",
        )
        return
    if not is_valid_youtube_url(yt_link):
        info_txt.configure(
            text="Download failed: Invalid YouTube URL. Please check and try again.",
            text_color="orange",
        )
        return
    try:
        yt = pytube.YouTube(
            yt_link,
            on_progress_callback=lambda stream, chunk, bytes_remaining: update_progress(stream, chunk, bytes_remaining, progress_txt, progress_bar)
        )
        # Only download progressive streams (video+audio together, no ffmpeg needed)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        title_txt.configure(text=yt.title)
        if not stream:
            raise Exception("No progressive (video+audio) stream available. Cannot download without ffmpeg.")
        stream.download()
    except Exception as e:
        info_txt.configure(
            text=f"Download failed: {str(e)}\nTry another video.",
            text_color="red",
        )
        print(f"Download failed: {e}")
    else:
        info_txt.configure(text="Download completed.", text_color="green")
        print("Download completed.")


def start_download():
    download_video(link_box, progress_txt, progress_bar, title_txt, info_txt)


# UI constructor
window = customtkinter.CTk()
window.title("YT Downloader")
window.resizable(False, False)

# Title label
title_txt = customtkinter.CTkLabel(window, text="YT Downloader")
title_txt.pack(padx=30, pady=10)

# Entry box for YouTube link
url_txt = customtkinter.CTkLabel(window, text="Enter URL:")
url_txt.pack()

url_var = tkinter.StringVar()
link_box = customtkinter.CTkEntry(
    window,
    width=480,
    height=30,
    textvariable=url_var,
)
link_box.pack(padx=30, pady=5)

# Progress bar
progress_bar = customtkinter.CTkProgressBar(window, width=480)
progress_bar.set(0.0)
progress_bar.pack()

progress_txt = customtkinter.CTkLabel(window, text="0.0 %")
progress_txt.pack()

# Label to show information or error messages
info_txt = customtkinter.CTkLabel(window, text="~")
info_txt.pack()

# Button to start download
button_frame = customtkinter.CTkFrame(window, fg_color="transparent")
button_frame.pack(pady=5)

clear_btn = customtkinter.CTkButton(
    button_frame,
    text="Clear",
    command=lambda: clear_fields(
        link_box, progress_txt, progress_bar, title_txt, info_txt
    ),
)
clear_btn.pack(side="left", padx=10)

download_btn = customtkinter.CTkButton(
    button_frame, text="Download", command=start_download
)
download_btn.pack(side="left", padx=30)


# Placeholder for future features
# TODO: Add settings panel for download location and format

if __name__ == "__main__":
    # Appearance and theme configuration
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    window.mainloop()
