import tkinter as tk
import threading
import time
import datetime
import pygame
pygame.mixer.init()



def play_alarm_sound():
  pygame.mixer.music.load("Alarm.mp3")
  pygame.mixer.music.play()


def set_alarm_clock(set_time):
  while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if current_time == set_time:
      play_alarm_sound()
      break
    time.sleep(1)


def set_alarm():
  alarm_timestr = alarm_time.get()
  print(f"alarm set for {alarm_timestr}")
  threading.Thread(target=set_alarm_clock , args=(alarm_timestr,) , daemon=True).start()




root = tk.Tk()
root.title("⏰ Alarm Clock")
root.geometry("600x400")
root.configure(bg="#1e1e2f") 
tk.Label(root, text="Set Your Alarm", font=("Helvetica", 24, "bold"), fg="white", bg="#1e1e2f").pack(pady=20)

# Alarm input frame
frame = tk.Frame(root, bg="#2d2d44", padx=20, pady=20, bd=2, relief="ridge")
frame.pack(pady=10)

# Alarm label and entry
tk.Label(frame, text="Time (HH:MM:SS):", font=("Arial", 14), fg="white", bg="#2d2d44").grid(row=0, column=0, pady=5)
alarm_time = tk.StringVar()
tk.Entry(frame, textvariable=alarm_time, font=("Arial", 14), width=15, justify="center", bg="#f0f0f0").grid(row=0, column=1, padx=10)

# Set button
tk.Button(root,text="Set Alarm",font=("Arial",14,"bold"),bg="#00b894",fg="white",padx=20,pady=5,command=set_alarm).pack(pady=10)

# Status label
status_label = tk.Label(root, text="", font=("Arial", 12), bg="#1e1e2f", fg="white")
status_label.pack()

root.mainloop()