import time
import pyautogui
import ctypes
import tkinter as tk
from threading import Thread

# Initialize ctypes for mouse events (Windows specific)
user32 = ctypes.windll.user32

# Define the function to start the automation loop
def start_automation():
    def automation_loop():
        while running[0]:  # Keep running as long as the 'running' flag is True
            location = pyautogui.locateOnScreen("image.png", confidence=0.7)
            
            if location:
                pos = pyautogui.center(location)
                
                pyautogui.moveTo(pos)
                user32.mouse_event(2, 0, 0, 0, 0)  # Mouse down
                time.sleep(0.05)
                user32.mouse_event(4, 0, 0, 0, 0)  # Mouse up
                time.sleep(1)
                
                search_bttn = pyautogui.locateOnScreen("search.png", confidence=0.7)
                
                if search_bttn:
                    pos2 = pyautogui.center(search_bttn)
                    pyautogui.moveTo(pos2)
                    user32.mouse_event(2, 0, 0, 0, 0)  # Mouse down
                    time.sleep(0.05)
                    user32.mouse_event(4, 0, 0, 0, 0)  # Mouse up
                    time.sleep(6)

                    print("Search button clicked.")
                else:
                    print("Search button not found.")
                
                time.sleep(3)
                print("Found the image and clicked.")
            else:
                print("Image not found on the screen.")
                time.sleep(3)
    
    # Set running flag to True to start the loop
    running[0] = True
    # Start the automation in a separate thread so it doesn't block the GUI
    automation_thread = Thread(target=automation_loop)
    automation_thread.daemon = True  # Ensure the thread stops when the program ends
    automation_thread.start()

# Define the function to stop the automation loop
def stop_automation():
    running[0] = False  # Set running flag to False to stop the loop
    print("Automation stopped.")

# Set up the GUI window
window = tk.Tk()
window.title("3301-infmoney")

#window color
window.configure(bg="black")

# Create a "Start" button to start the automation
start_button = tk.Button(window, text="Start", command=start_automation, width=15, height=2)
start_button.pack(pady=10)

# Create a "Stop" button to stop the automation
stop_button = tk.Button(window, text="Stop", command=stop_automation, width=15, height=2)
stop_button.pack(pady=10)

# Running flag to control the automation loop
running = [False]  # Use a list to hold the flag, so it can be updated inside the thread

# Run the Tkinter event loop to display the GUI
window.mainloop()
