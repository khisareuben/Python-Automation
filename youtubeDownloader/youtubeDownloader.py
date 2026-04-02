# YouTube Downloader using yt-dlp
# --------------------------------
# Features:
# 1. Shows video title.
# 2. Automatically picks the best resolution (video+audio).
# 3. Shows progress percentage, speed, and ETA.
# 4. Saves file in Downloads folder.
# 5. Handles errors gracefully.
# you can also use pytube(youtube videos only)

import yt_dlp

def progress_hook(d):
    """
    Callback function to show download progress.
    yt-dlp calls this function with a dictionary 'd' containing status info.
    """
    if d['status'] == 'downloading':
        # Show percentage, speed, and ETA while downloading
        print(f"Downloading: {d['_percent_str']} | Speed: {d['_speed_str']} | ETA: {d['_eta_str']}", end="\r")
    elif d['status'] == 'finished':
        # Notify when download is complete
        print("\n✅ Download complete!")

def download_video(url):

    # yt-dlp configuration options
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Always pick best resolution + audio
        'progress_hooks': [progress_hook],     # Attach our progress hook for updates
        'outtmpl': '/home/hrmoose/Downloads/%(title)s.%(ext)s'  # Save file with video title
    }

    try:
        # Create a YoutubeDL object with our options
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract video info without downloading (to get title)
            info = ydl.extract_info(url, download=False)
            print(f"\nTitle: {info['title']}")

            # Start the actual download
            ydl.download([url])

    except Exception as e:
        # Catch and display any errors (e.g., invalid URL, network issues)
        print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    # Ask user for the video URL
    url = input("Enter YouTube video URL: ")
    download_video(url)
