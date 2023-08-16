# YouTube Video Downloader

This Python script allows you to download YouTube videos by providing a video URL and desired quality. It utilizes the `pytube` library to fetch video streams and provides an option to convert 3GPP format videos to MP4 format using the `moviepy` library.

## Features

- Download YouTube videos by providing a video URL and quality preference.
- Supports downloading videos in various quality options.
- Converts downloaded 3GPP format videos to MP4 format.
- Saves downloaded videos to a specified folder.

## Prerequisites

Before running the script, ensure you have the following libraries installed:

- `pytube`
- `moviepy`

You can install them using the following commands:

```bash
pip install pytube moviepy
```

## Usage

1. Run the script in your terminal using the following command:

   ```bash
   python youtube_downloader.py
   ```

2. Enter the YouTube video URL when prompted.

3. Enter the desired video quality (i.e, 144p, 240p, 360p, 480p, 720p, 1080p) when prompted.

4. The script will download the video, display its progress, and save it in the specified folder. If the video is in 3GPP format, it will be automatically converted to MP4 format.

## Note

- This script requires an active internet connection to download videos.
- The downloaded videos are saved in the 'youtube' folder in your 'Downloads' directory.

## License

This project is licensed under the MIT License. Feel free to modify and use the script according to your needs.

## Disclaimer

This script is intended for educational and personal use only. Ensure you comply with YouTube's terms of service and copyright policies when using this script to download videos.

---

Feel free to contribute to the script by suggesting improvements or reporting issues. If you have any questions, please don't hesitate to open an issue.
