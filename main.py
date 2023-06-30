
# A program to move mouse at specified offset within given timeout.
# By: GK

import tkinter as tk
import pyautogui
import time
import threading

stop_event = threading.Event()                              # Create a threading event and a thread object for mouse movemet.
mouse_thread = None

def move_mouse():                                           # Function to move mouse cursor.
    try:
        x_offset = int(x_entry.get() or 0)                  # Get the x and y offsets from the entry fields or set them to 0 if empty.
        y_offset = int(y_entry.get() or 0)
        timeout = float(timeout_entry.get() or 0)           # Get the timeout value from the entry field, or set it to 0 if empty.
    except ValueError:
        error_label.config(text="Ivalid input. \nPlease enter valid integers.") # Display an error message if invalid input is provided.
        return

    while not stop_event.is_set():
        initial_x, initial_y = pyautogui.position()         # Update the initial mouse position.
        target_x = initial_x + x_offset                     # Calculate the target position with the given offset.
        target_y = initial_y + y_offset                     # The same for 'y' axis.
        
        pyautogui.moveTo(target_x, target_y)                # Move the mouse cursor to the target position.
        time.sleep(timeout)                                 # Wait for the specified timeout.

        if stop_event.is_set():
            break

        initial_x, initial_y = pyautogui.position()         # Update the initial mouse position again.
        target_x = initial_x - x_offset                     # Calculate the target position to move back to the initial position.
        target_y = initial_y - y_offset                     # The same for 'y' axis.

        pyautogui.moveTo(target_x, target_y)                # Move the mouse cursor to the initial position.
        time.sleep(timeout)                                 # Wait for the specified timeout.

def stop_mouse_movement():                                  # Function to stop the mouse movement and close the window.
    stop_event.set()
    if mouse_thread:
        mouse_thread.join()
    window.destroy()

def update_initial_position(event):                         # Function to update the initial mouse position.
    global initial_x, initial_y
    initial_x, initial_y = pyautogui.position()

window = tk.Tk()                                            # Create GUI window.
window.title("Mouse Mover")                                 # Create window title.
window.geometry("180x215")                                  # Set window size.

window.protocol("WM_DELETE_WINDOW", stop_mouse_movement)

x_label = tk.Label(window, text = "X Offset:", font = ("Arial", 12))                                   # Create labels and entry fields for x and y coordinates.
x_label.pack()
x_entry = tk.Entry(window, font = ("Arial", 12), justify = "center", width = 15)
x_entry.pack()

y_label = tk.Label(window, text = "Y Offset:", font = ("Arial", 12))
y_label.pack()
y_entry = tk.Entry(window, font = ("Arial", 12), justify = "center", width = 15)
y_entry.pack()

timeout_label = tk.Label(window, text="Timeout (seconds):", font = ("Arial", 12))
timeout_label.pack()
timeout_entry = tk.Entry(window, font = ("Arial", 12), justify = "center", width = 15)
timeout_entry.pack()

error_label = tk.Label(window, text="", fg="red")
error_label.pack()

def start_mouse_movement():                                                                             # Function to start the mouse movement thread.
    global mouse_thread
    mouse_thread = threading.Thread(target=move_mouse)
    mouse_thread.start()

start_button = tk.Button(window, text="Start", font = ("Arial", 12), command=start_mouse_movement)      # Create a button to start the mouse movement
start_button.pack()

window.bind("<Motion>", update_initial_position)                                                        # <Motion> event is triggered whenever the mouse cursor moves within the boundaries of the window. By binding this event to the update_initial_position function, we can update the initial position of the mouse cursor whenever it moves.

window.mainloop()                                                                                       # Start the GUI event loop.
