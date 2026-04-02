import os
import shutil

# The shutil module offers a number of high-level operations on files and collections of files.
#  In particular, functions are provided which support file copying and removal
#use watchdog if you want to automatically move the files once the appear

# Define your Downloads folder (adjust path if needed)
DOWNLOADS_DIR = "/home/hrmoose/Downloads"

# Define target folders for different file types
TARGET_DIRS = {
    "images": "/home/hrmoose/Downloads/Photos",
    "videos": "/home/hrmoose/Downloads/Videos",
    "documents": "/home/hrmoose/Downloads/Documents",
    "music": "/home/hrmoose/Downloads/Music",
    "others": "/home/hrmoose/Downloads/Others"
}

# Define file extensions for each category
FILE_TYPES = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "videos": [".mp4", ".mkv", ".avi", ".mov", ".webm"],
    "documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "music": [".mp3", ".wav", ".aac", ".flac"]
}

def organize_downloads():
    for filename in os.listdir(DOWNLOADS_DIR):
        file_path = os.path.join(DOWNLOADS_DIR, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        moved = False
        for category, extensions in FILE_TYPES.items():
            if filename.lower().endswith(tuple(extensions)):
                target_folder = TARGET_DIRS[category]
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved {filename} → {target_folder}")
                moved = True
                break

        # If file doesn't match any category, move to "Others"
        if not moved:
            target_folder = TARGET_DIRS["others"]
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, filename))
            print(f"Moved {filename} → {target_folder}")

if __name__ == "__main__":
    organize_downloads()
