from playsound import playsound
import time

CLEAR = "\033[2J" #clears the screen
CLEAR_AND_RETURN = "\033[H" #clears the screen and returns the cursor to the top left corner (home position)

def alarm(seconds):
    time_elapsed = 0

    #print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1) #means wait for 1 second
        time_elapsed += 1 

        #seconds we are running it for and how much time is left
        time_left = seconds - time_elapsed  
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        #print(f"{CLEAR_AND_RETURN} Alarm will sound in: {minutes_left:02d} minutes and {seconds_left:02d} seconds") #CLEAR_AND_RETURN is similar to end = "\r" but it also clears the screen
        print(f"Alarm will sound in: {minutes_left:02d} minute(s) and {seconds_left:02d} second(s)", end="\r") #end = "\r" means return to the beginning of the line
    playsound('Alarm.mp3')

minutes = int(input("Enter the number of minutes you want to set the alarm for: "))
seconds = int(input("Enter the number of seconds too: "))
total_seconds = (minutes * 60) + seconds #converting everything to seconds
alarm(total_seconds)