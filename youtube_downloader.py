from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        #video = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_res = yt.streams.get_highest_resolution()
        highest_res.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print("An error occurred:", str(e))

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
        
    return folder

#just trying to ensure these are exceuted directly from this file not when imported
if __name__ == "__main__": 
    root = tk.Tk() #instantiates the tkinter window
    root.title("YouTube Video Downloader")
    root.withdraw() #hides it from showing

    video_url = input("Please enter the YouTube video URL: ")
    save_path = open_file_dialog()

    if save_path:
        print(f"Downloading...")
        download_video(video_url, save_path)
    else:
        print("Invalid location...")