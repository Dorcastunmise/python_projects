import os
import shutil #issues copying operator
import datetime
import schedule
import time

source_dir = "C:/Anaconda/envs/mini_projects/Assets"
destination_dir = "C:/Anaconda/envs/mini_projects/Backups"

def copy_folder_to_directory(source, destination):
    today = datetime.date.today()
    destination_dir = os.path.join(destination, str(today))

    try:
        print(f"Copying folder to: {destination_dir}")
        shutil.copytree(source, destination_dir)
        print(f"Folder copied to: {destination_dir}")
    except FileExistsError:
        print(f"Folder already exists at: {destination_dir}")
    except Exception as e:
        print(f"Error copying folder: {e}")


schedule.every().day.at("14:13").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)



    

