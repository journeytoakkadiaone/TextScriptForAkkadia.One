# IN YOUR TEMINAL RUN THE FOLLOWING COMMANDS
# pip install pyautogui

import pyautogui
import time

# time between each call to pyautogui function
pyautogui.PAUSE = 5

# time before the script runs
wait_time = 7  # Adjust this time as needed

print(
    f"Switch to your browser or application. The script will start pressing keys in {wait_time} seconds."
)

# takes the waitime
time.sleep(wait_time)


pyautogui.write(
    "HELLO WORLD....HELLO WORLD...HELLO WORLD...HELLO WORLD....HELLO WORLD...HELLO WORLD...HELLO WORLD....HELLO WORLD...HELLO WORLD...HELLO WORLD....HELLO WORLD...HELLO WORLD...HELLO WORLD....HELLO WORLD...HELLO WORLD...HELLO WORLD....HELLO WORLD...HELLO WORLD...HELLO WORLD....",
    interval=0,
)

pyautogui.write(
    "HELLO WORRRRRRRRRRRLLLLLDDDDDDDDDDDDDDDDDDDDDDDDD...HHHHHHHHHHHHHHEEEEEEEEEEEEEEELLLLLLLLLLLLLLLLLLLLLLLO WORLD...."
)
print("Key presses completed.")