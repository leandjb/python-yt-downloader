# YouTube Downloader GUI

A simple and modern desktop application to download YouTube videos using a graphical interface built with Python and CustomTkinter.

## Features
- Download YouTube videos by pasting the URL
- Progress bar and percentage indicator
- Error messages for invalid URLs or unsupported videos
- No need for ffmpeg (downloads only progressive streams: video+audio up to 720p)
- Clean and responsive interface

## Quick Installation

### Requirements
- Python 3.8+
- Windows (recommended, but works on other OS with minor changes)

### 1. Clone or Download this Repository
```
cd python-yt-downloader/src
```

### 2. Install Dependencies
```
pip install customtkinter pytube
```

### 3. Run the Application
```
python main.py
```

## Usage
1. Paste a valid YouTube video URL in the input box.
2. Click the **Download** button.
3. Wait for the progress bar to reach 100% and the message "Download completed." to appear.
4. The video will be saved in the same folder as the script.

## Notes
- Only videos with progressive streams (video+audio together, usually up to 720p) can be downloaded. If the video is only available in higher quality (separate video/audio), the app will show an error.
- If you need to download higher quality videos, use [yt-dlp](https://github.com/yt-dlp/yt-dlp) and install ffmpeg.

## Troubleshooting
- If you get errors about streams or downloads, try another video or check your internet connection.
- For issues with pytube, try updating it:
  ```
  pip install --upgrade pytube
  ```

## License
MIT
