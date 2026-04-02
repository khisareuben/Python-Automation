import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

DOWNLOADS_DIR = "/home/hrmoose/Downloads"

TARGET_DIRS = {
    "images": "/home/hrmoose/Downloads/Photos",
    "videos": "/home/hrmoose/Downloads/Videos",
    "documents": "/home/hrmoose/Downloads/Documents",
    "music": "/home/hrmoose/Downloads/Music",
    "others": "/home/hrmoose/Downloads/Others"
}

FILE_TYPES = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "videos": [".mp4", ".mkv", ".avi", ".mov"],
    "documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "music": [".mp3", ".wav", ".aac", ".flac"]
}

class DownloadHandler(FileSystemEventHandler):
    # This class defines what happens when events occur in the Downloads folder.

    def on_created(self, event):
        # Triggered automatically when a new file is created in the watched folder.
        # 'event' contains details like the file path and whether it's a directory.
        if not event.is_directory:
            self.move_file(event.src_path)

    def move_file(self, file_path):
        # Custom method to decide where to move the file based on its extension.
        filename = os.path.basename(file_path)
        moved = False

        # Skip incomplete downloads (temporary files created by browsers).
        if filename.endswith(".crdownload") or filename.startswith(".org.chromium"):
            return

        # Check file type against defined categories and move accordingly.
        for category, extensions in FILE_TYPES.items():
            if filename.lower().endswith(tuple(extensions)):
                target_folder = TARGET_DIRS[category]
                os.makedirs(target_folder, exist_ok=True)  # Ensure folder exists
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved {filename} → {target_folder}")
                moved = True
                break

        # If no match, move to "Others"
        if not moved:
            target_folder = TARGET_DIRS["others"]
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, filename))
            print(f"Moved {filename} → {target_folder}")


if __name__ == "__main__":
    event_handler = DownloadHandler()   # Create your custom handler
    observer = Observer()               # Create an Observer (the watcher)
    observer.schedule(event_handler, DOWNLOADS_DIR, recursive=False)
    # Tell the observer to watch DOWNLOADS_DIR and use your handler for events.

    observer.start()                    # Start watching
    print("Watching Downloads folder...")

    try:
        while True:
            pass  # Keeps the script running so observer stays active
    except KeyboardInterrupt:
        observer.stop()                 # Stop watching if you press Ctrl+C
    observer.join()                     # Wait until observer thread finishes

