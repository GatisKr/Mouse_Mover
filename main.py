
# A program to move mouse at specified offset within given timeout.
# By: GK

import tkinter as tk                                        # Import the GUI module.
import pyautogui                                            # Import module for mouse control.
import time                                                 # Import module for delays.
import threading                                            # Import module for concurrent execution.

stop_event = threading.Event()                              # Create a threading event and a thread object for mouse movement. The 'stop_event' is created as a 'threading.Event()' object. It will be used to control execution of the mouse movement thread.
mouse_thread = None                                         # The 'mouse_thread' variable is initialized to 'None'.

def start_mouse_movement():                                 # Function to start the mouse movement thread. It is called when the user clicks the 'Start' button.
    global mouse_thread
    stop_event.clear()                                      # Reset stop_event.
    mouse_thread = threading.Thread(target=move_mouse)      # It creates a new 'mouse_thread' using 'threading.Thread()' and passes the 'move_mouse()' function as the target.
    mouse_thread.start()                                    # The thread is then started using 'move_thread.start().

def stop_mouse_movement():                                  # This function is called when the user wants to stop the mouse movement. It sets the 'stop_event', waits for the 'mouse_thread' to complete using 'thread.join()'.
    stop_event.set()
    if mouse_thread:
        mouse_thread.join()
    error_label.config(text = "Not moving your mouse cursor", fg = "black", font = ("Arial", 8))

def update_initial_position(event):                         # This function is bound to the '<Motion>' event of the window. Whenever the mouse cursor moves within the window, this function is triggered. It updates the 'initial_x' and 'initial_y' global variables with the current mouse cursor position.
    global initial_x, initial_y                             # Variables 'initial_x' and 'initial_y' are declared as 'global'. Thus, the function is allowed to modify the global variables and make updated values accessible outside the function scope.
    initial_x, initial_y = pyautogui.position()

def on_window_close():                                      # This function calls 'stop_mouse_movement()' to stop moving mouse cursor when program window is closed.
    stop_mouse_movement()
    window.destroy()

def on_key_press(event):                                    # This function catches pressing 'Escape' or 'Enter' keys and the call 'stop_mouse_movement()' or 'start_mouse_movement()' functions accordingly.
    if event.keysym == "Escape":
        stop_mouse_movement()
    elif event.keysym == "Return":
        start_mouse_movement()

def move_mouse():                                           # This function is responsible for moving the mouse cursor based on the specified offsets and timeout. It first tries to retrieve the values from the offset and timeout entry fields. If a value cannot be converted to an integer or float, it displays an error message and returns.
    try:
        x_offset = int(x_entry.get() or 0)                  # Get the x and y offsets from the entry fields or set them to 0 if empty.
        y_offset = int(y_entry.get() or 0)
        timeout = float(timeout_entry.get() or 0)           # Get the timeout value from the entry field, or set it to 0 if empty.
        error_label.config(text="Now moving your mouse cursor", fg = "black", font = ("Arial", 8)) # This line removes error message when valid value is entered.
    except ValueError:
        error_label.config(text="Invalid input. Please enter valid numbers.", fg = "red", font = ("Arial, 8")) # Display an error message if invalid input is provided.
        return

    while not stop_event.is_set():                          # This while loop inside the 'move_mouse()' function is used to continuously move the mouse cursor. 
        initial_x, initial_y = pyautogui.position()         # The while loop starts by updating the initial mouse position using 'pyaytogui.position()'.
        target_x = initial_x + x_offset                     # Then we calculate the mouse cursor target position by adding the given offset to the initial position.
        target_y = initial_y + y_offset                     # The same is done for the 'y' axis.
        
        pyautogui.moveTo(target_x, target_y)                # This statement moves the mouse cursor to the target position.
        time.sleep(timeout)                                 # Wait for the specified timeout.

        initial_x, initial_y = pyautogui.position()         # Update the initial mouse position again.
        target_x = initial_x - x_offset                     # Calculate the target position to move back to the initial position.
        target_y = initial_y - y_offset                     # The same for 'y' axis.

        pyautogui.moveTo(target_x, target_y)                # Move the mouse cursor to the initial position.
        time.sleep(timeout)                                 # Wait for the specified timeout.

        if stop_event.is_set():                             # If the 'stop_event' is set (indicating the movement should be stopped), the loop breakes. Otherwise, it updates the initial position and uses 'pyautogui.moveTo()' to move the cursor back. Then it waits for the specified timeout.
            break

window = tk.Tk()                                            # The 'tkinter.Tk()' constructor is used to create the main GUI window.
window.title("Mouse Mover")                                 # Create window title.
window.geometry("242x200")                                  # Set window size.

x_label = tk.Label(window, text = "X Offset:", font = ("Arial", 10))                                            # Create and configure GUI elements: Labels and entry fields for the X offset, Y offset and timeout. The labels are created using 'tk.Label()' and the entry fields using 'tk.Entry()'. The 'font', justify' and 'width' attributes are set to customize the appearance of the elements. The labels and entry fields are then packed using 'pack()' method to arrange them in the window.
x_label.pack()
x_entry = tk.Entry(window, font = ("Arial", 12), justify = "center", width = 15)
x_entry.pack()

y_label = tk.Label(window, text = "Y Offset:", font = ("Arial", 10))
y_label.pack()
y_entry = tk.Entry(window, font = ("Arial", 12), justify = "center", width = 15)
y_entry.pack()

timeout_label = tk.Label(window, text="Timeout (seconds):", font = ("Arial", 10))
timeout_label.pack()
timeout_entry = tk.Entry(window, font = ("Arial", 12), justify = "center", width = 15)
timeout_entry.pack()

label_frame = tk.Label(window, text = "")                                                                       # Empty optional frame to add a label if needed.
label_frame.pack()

button_frame = tk.Frame(window)                                                                                 # Create a frame to hold the buttons.
button_frame.pack()

start_button = tk.Button(button_frame, text = "Start", font = ("Arial", 10), command=start_mouse_movement)      # This creates a button to start the mouse movement.
start_button.pack(side = "left")

stop_button = tk.Button(button_frame, text = "Stop", font = ("Arial", 10), command=stop_mouse_movement)         # Create a button to stop the mouse movement.
stop_button.pack(side = "left")

error_label = tk.Label(window, text="")                                                                         # An empty labels is created to display error messages. It is initially empty and will be updated as needed.
error_label.pack()

window.bind("<Motion>", update_initial_position)                                                                # This line bounds the <Motion> event to the 'update_initial_position' function using 'window.bind()'. It is triggered whenever the mouse cursor moves within the boundaries of the window. By binding this event to the 'update_initial_position function', we can update the initial position of the mouse cursor whenever it moves.
window.bind("<KeyPress>", on_key_press)                                                                         # This statement is used to bind the 'KeyPress' event to the function 'on_key_press'. This means that when a key is pressed while the window has focus, the 'on_key_press' function will be called to handle that event.
window.protocol("WM_DELETE_WINDOW", on_window_close)                                                            # This statement is used to set the behavior of the window when the user attempts to close it using the window manager's close button. The 'protocol' method is a method of the 'Tk' class from the 'tkinter' module, which represents the main window or the root window of a Tkinter application. It allows to define specific protocols of behaviors for different window events. 'WM_DELETE_WINDOW' protocol is triggered when the user tries to close the window. By associating the 'on_window_close' function with this protocol, we are specifying that when the window is being closed, the 'on_window_close' function should be called which then accordingly calls 'stop_mouse_movement' function to stop the mouse movement and perform any necessary cleanup operations. The 'stop_mouse_movement' function is defined earlier in the code and contains the logic to stop the mouse movement thread, join the thread and destroy the window. By setting the 'WM_DELETE_WINDOW' protocol to this function, we ensure that the mouse movement stops and the window is closed whent the user attempts to close the window.

window.mainloop()                                                                                               # Start the GUI event loop, which listens for user interactions and updates the GUI accordingly.
