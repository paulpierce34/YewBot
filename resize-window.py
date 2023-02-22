import pyautogui
import time
 
# Set the desired position and size of the window
x = 100
y = 100
width = 1000
height = 850
 
# Find the window with the title "Old School RuneScape"
window_title = "Old School RuneScape"
window = pyautogui.getWindowsWithTitle(window_title)[0]
if window is None:
    print(f"Error: Could not find window with title {window_title}")
else:
    # Bring the window to the foreground
    window.activate()
 
    # Wait a short time for the window to become active
    time.sleep(0.5)
 
    # Move the window to the specified location and set the size
    window.resizeTo(width, height)
    window.moveTo(x, y)
 
    print("Window moved successfully!")
