from datetime import datetime

import time

from playsound import playsound  

alarm_time = input("Set alarm time (HH:MM in 24-hour format): ")

print(f"Alarm set for {alarm_time}. Waiting...")

while True:
    current_time = datetime.now().strftime("%H:%M")
    if current_time == alarm_time:
        print("⏰ Wake up! Alarm ringing!")
        playsound("alarm.mp3")  # Put an mp3 in the same folder
        break
    time.sleep(5)