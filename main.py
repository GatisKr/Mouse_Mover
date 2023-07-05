
# A program to move mouse cursor at specified offset with given timeout.
# By: GK

import tkinter as tk # Import the GUI module.
import pyautogui # Import module for mouse control.
import threading # Import module for concurrent execution.

stop_event = threading.Event() # This line creates a 'stop_event' variable which is object of the 'Event' class from the 'threading' module. The 'Event' class provides a spimple way to communicate between threads. It allows one or more threads to wait until they are notified by another thread that an event has occured. In this case, the 'stop_event' object is used to control the mouse movement loop. Initially, the 'stop_event' object is in 'clear' state, meaning that any threads waiting on it will be blocked. When the event needs to be triggered, we can call the 'set()' method on the 'stop_event' object, which will unblock the waiting threads. This is used to stop the mouse movement loop when the stop button is pressedor the window is closed. The 'stop_event' object can also be used in the code to synchronize the start and stop of the mouse movement thread.
mouse_thread = None # The 'mouse_thread' variable is initialized to 'None'.

def start_mouse_movement(): # 'start_mouse_movement' function starts the mouse movement thread. It is called when the user clicks the 'Start' button.
    global mouse_thread # The line 'global mouse_thread' is used to specify that the 'mouse_thread' variable should be treated as a global variable, meaning that it can be accessed and modified from both inside and outside of the current function or scope. By declaring 'mouse_thread' as global, any modifications made to the variable within the current function will affect the global variable with the same name. This is important when you want to access or manipulate the 'mouse_thread' variable in other functions or parts of the code. The 'mouse_thread' variable is initially assigned to 'None' outside of any function, making it a global variable. Then, inside the 'start_mouse_movement()' function, it is reassigned to a new thred object created using threading.Thrad()'. By declaring 'mouse_thread' as global, this assignment is applied to the global variable, allowing other functions, such as 'stop_mouse_movement()', to access nd control the same 'mouse_thread' object. Using the 'global' keyword is necessary when you want to modify a global variable from within a function or when you want to ensure that all references to the variable point to the same object throughout the program.
    stop_event.clear() # The 'stop_event.clear()' method is used to reset the state of a threading event object. The 'stop_event' is an instance of the 'threading.Event()' class, which representsa simple threading event. The event object has two states: seto or clear. Initially, the event is in a clear state. Calling 'stop_event.clear()' eplicitly sets the event state to clear, regardless of its previous state. This means that any threads waiting for the event to be set will continue to wait until the event is set again. In this code 'stop_event.clear()' is not explicitly mentioned. However, it can be used to reset the event state before starting the mouse movement, ensuring that the event is initially cleared and threads waiting for it to be set will wait until the event is explicitly set using 'stop__event.set()'.
    mouse_thread = threading.Thread(target=move_mouse) # This line creates a new thread object named 'mouse_thread' using the 'Thread' class from the 'threading' module. The 'Thread' class represents a separate thread of control, allowing concurrent execution of multiple threads within a program. It takes the 'target' argument, which specifies the function to be executed in the new thread. In this case, the 'target' argument is set to 'move_mouse', which is a function responsible for moving the mouse cursor based on the specified offsets and timeout. The function is executed in a separate thread to enable concurrent execution, allowing the main thread to handle other tasks such as interacting with the GUI. By creating a new thread using 'threading.Thread' and setting its 'target' to 'move_mouse', the brogram is able to execute the mouse movement logic concurrently in a separate thread, keeping the GUI responsive and allowing the user to interact with the program while the mouse is being moved.
    mouse_thread.start() # After creating the 'mouse_thread', it can be started by calling its 'start()' method, which initiates the execution of the 'move_mouse' function in the new thread.

def stop_mouse_movement(): # 'stop_mouse_movement' function is called when the user wants to stop the mouse movement. It sets the 'stop_event', waits for the 'mouse_thread' to complete using 'thread.join()'.
    stop_event.set() # The 'stop_event.set()' method is used to set the state of a threading event object to 'set'. This means that any threads waiting for the event to be set will be released and can continue their execution. When called it indicates, that the mouse movement should stop. This allows 'move-mouse()' function, which is running in a separate threas, to check the state of the 'stop_event' and exit its while loop, effectively stopping the mouse movement.
    if mouse_thread: # The statement 'if mouse_thread:' checks if the 'mouse_thread' variable has been assigned to a value or not. In Python, when a variable is assigned a value, it becomes 'truthy', meaning it evaluates to 'True' in a boolean context. So 'if mouse_thread:' is checking if the 'mouse_thread' is not 'None' or if it has been assigned a value (it is not 'None'). If the condition is 'True', it means that 'mouse_thread' has a value assigned to it and the code block following the 'if' statement will be executed. If condition is 'False', the ode block will be skipped. By checking 'if mouse_thread:' before joining the thread, the code ensures that the 'join()' operation is only performed if a thread exists. This prevents errors in cases where the 'stop_mouse_movement()' function is called before the thread has been started or if it has already completed its execution.
        mouse_thread.join() # By calling 'mouse_thread.join()' program waits at this line until the 'mouse_thread' finishes its execution. This ensures that the mouse movement thread completes its task before the program continues with any subsequent actions. It allows for proper synchronization and prevents any potential issues that could arise from accessing or modifying shared resources simultaneously. This line ensures that the program doesn't exit prematurely while the mouse movement is still ongoing.
    error_label.config(text = "Not moving your mouse cursor", fg = "black", font = ("Arial", 8)) # The next line is used to update the configuration of the 'error_label' widget in the GUI. By calling 'error_label.config()' and passing the appropriate arguments, we can dynamically update the configuration of the label.

def update_initial_position(event): # 'update_initial_position' function is bound to the '<Motion>' event of the window. Whenever the mouse cursor moves within the window, this function is triggered. It updates the 'initial_x' and 'initial_y' global variables with the current mouse cursor position.
    global initial_x, initial_y # Variables 'initial_x' and 'initial_y' are declared as 'global'. Thus, the function is allowed to modify the global variables and make updated values accessible outside the function scope.
    initial_x, initial_y = pyautogui.position()

def on_window_close(): # 'on_window_close' function calls 'stop_mouse_movement()' to stop moving mouse cursor when program window is closed.
    stop_mouse_movement()
    window.destroy()

def on_key_press(event): # This function catches pressing 'Escape' or 'Enter' keys and the call 'stop_mouse_movement()' or 'start_mouse_movement()' functions accordingly.
    if event.keysym == "Escape":
        stop_mouse_movement()
    elif event.keysym == "Return":
        start_mouse_movement()

def move_mouse(): # This function is responsible for moving the mouse cursor based on the specified offsets and timeout. It first tries to retrieve the values from the offset and timeout entry fields. If a value cannot be converted to an integer or float, it displays an error message and returns.
    try:
        x_offset = int(x_entry.get() or 0) # Get the x and y offsets from the entry fields or set them to 0 if empty.
        y_offset = int(y_entry.get() or 0)
        timeout = float(timeout_entry.get() or 0) # Get the timeout value from the entry field, or set it to 0 if empty.
        error_label.config(text="Now moving your mouse cursor", fg = "black", font = ("Arial", 8)) # This line displays movement message and removes error message when valid value is entered.
    except ValueError:
        error_label.config(text="Invalid input. Please enter valid numbers.", fg = "red", font = ("Arial, 8")) # Display an error message if invalid input is provided.
        return

    while not stop_event.is_set(): # This while loop inside the 'move_mouse()' function is used to continuously move the mouse cursor.
        initial_x, initial_y = pyautogui.position() # The while loop starts by updating the initial mouse position using 'pyaytogui.position()'.
        target_x = initial_x + x_offset # Then we calculate the mouse cursor target position by adding the given offset to the initial position.
        target_y = initial_y + y_offset # The same is done for the 'y' axis.

        try:
            pyautogui.moveTo(target_x, target_y) # This statement moves the mouse cursor to the target position.

            if target_x == 0 and target_y == 0: # This line checks if the target coordinates are in the top left corener of the screen by calling 'pyautogui.onScreen(target_x, target_y)'. If the coordinates are (0, 0), it means that the mouse has moved to the left upper corner of the screen. In this case PyAutoGUI fail-safe feature is triggered to stop mouse movement.
                error_label.config(text = "Not moving your mouse cursor", fg = "black", font = ("Arial", 8))
                break

        except pyautogui.FailSafeException: # If the 'pyautogui.moveTo()' function call raises a 'pyautogui.FailSafeException', it means that the mouse cursor reached top left corner of the screen, triggering the fail-safe mechanism. In this case we also break out of the loop to stop the mouse movement.
            error_label.config(text = "Not moving your mouse cursor", fg = "black", font = ("Arial", 8))
            break

        if stop_event.is_set(): # If the 'stop_event' is set (indicating the movement should be stopped), it returns 'True' and code breakes out of the loop using the 'break' statement, stopping the mouse movement instantly.
            break
        
        elif stop_event.wait(timeout=timeout): # This code checks if the 'stop_event' has been set within a specific timeout period. 'stop_event.wait(timeout=timeout)' is called, which waits for the 'stop_event' to be set or until the specified 'timeout' duration is reached. If the 'stop_event' is set within the timeout duration, the 'wait' function will return 'True'. If the 'wait' function returns 'True', it means that the stop event was set, indicating that the user pressed the stop button or closed the window. In this case, the code breakes out of the loop using 'break' statement, stopping the mouse movement instantly.
            break

        initial_x, initial_y = pyautogui.position() # Update the initial mouse position again.
        target_x = initial_x - x_offset # Calculate the target position to move back to the initial position.
        target_y = initial_y - y_offset # The same for 'y' axis.

        try:
            pyautogui.moveTo(target_x, target_y) # Move the mouse cursor to the initial position.

            if target_x == 0 and target_y == 0:
                error_label.config(text = "Not moving your mouse cursor", fg = "black", font = ("Arial", 8))
                break

        except pyautogui.FailSafeException:
            error_label.config(text = "Not moving your mouse cursor", fg = "black", font = ("Arial", 8))
            break

        if stop_event.is_set():
            break

        elif stop_event.wait(timeout=timeout):
            break

window = tk.Tk() # The 'tkinter.Tk()' constructor is used to create the main GUI window.
window.title("Mouse Mover") # Create window title.
window.geometry("242x200") # Set window size.

# Now we create and configure GUI elements: Labels and entry fields for the X offset, Y offset and timeout. The labels are created using 'tk.Label()' and the entry fields using 'tk.Entry()'. The 'font', 'justify' and 'width' attributes are set to customize the appearance of the elements. The labels and entry fields are then packed using 'pack()' method to arrange them in the window.
x_label = tk.Label(window, text = "X Offset:", font = ("Arial", 10))
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

label_frame = tk.Label(window, text = "") # Empty optional frame to add a label if needed.
label_frame.pack()

button_frame = tk.Frame(window) # Create a frame to hold the buttons.
button_frame.pack()

start_button = tk.Button(button_frame, text = "Start", font = ("Arial", 10), command=start_mouse_movement) # This creates a button to start the mouse movement.
start_button.pack(side = "left")

stop_button = tk.Button(button_frame, text = "Stop", font = ("Arial", 10), command=stop_mouse_movement) # Create a button to stop the mouse movement.
stop_button.pack(side = "left")

error_label = tk.Label(window, text="") # An empty label is created to display error messages. It is initially empty and will be updated as needed.
error_label.pack()

window.bind("<Motion>", update_initial_position) # The line 'window.bind("<Motion>", update_initial_position)' bounds the <Motion> event to the 'update_initial_position' function using 'window.bind()'. It is triggered whenever the mouse cursor moves within the boundaries of the window. By binding this event to the 'update_initial_position function', we can update the initial position of the mouse cursor whenever it moves.
window.bind("<KeyPress>", on_key_press) # The statement 'window.bind("<KeyPress>", on_key_press)' is used to bind the 'KeyPress' event to the function 'on_key_press'. This means that when a key is pressed while the window has focus, the 'on_key_press' function will be called to handle that event.

window.protocol("WM_DELETE_WINDOW", on_window_close) # The statement 'window.protocol("WM_DELETE_WINDOW", on_window_close)' is used to set the behavior of the window when the user attempts to close it using the window manager's close button. The 'protocol' method is a method of the 'Tk' class from the 'tkinter' module, which represents the main window or the root window of a Tkinter application. It allows to define specific protocols of behaviors for different window events. 'WM_DELETE_WINDOW' protocol is triggered when the user tries to close the window. By associating the 'on_window_close' function with this protocol, we are specifying that when the window is being closed, the 'on_window_close' function should be called which then accordingly calls 'stop_mouse_movement' function to stop the mouse movement and perform any necessary cleanup operations. The 'stop_mouse_movement' function is defined earlier in the code and contains the logic to stop the mouse movement thread, join the thread and destroy the window. By setting the 'WM_DELETE_WINDOW' protocol to this function, we ensure that the mouse movement stops and the window is closed whent the user attempts to close the window.

window.mainloop() # Start the GUI event loop, which listens for user interactions and updates the GUI accordingly.
