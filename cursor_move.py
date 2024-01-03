import pyautogui
import time

def move_cursor_within_square(start_x, start_y, size, duration):
    # Move right within the square
    pyautogui.moveTo(start_x + size, start_y, duration=duration)
    # Move down within the square
    pyautogui.moveTo(start_x + size, start_y + size, duration=duration)
    # Move left within the square
    pyautogui.moveTo(start_x, start_y + size, duration=duration)
    # Move up within the square
    pyautogui.moveTo(start_x, start_y, duration=duration)

# Get the screen resolution
screen_width, screen_height = pyautogui.size()

# Calculate the starting position of the smaller square
start_x = screen_width // 8
start_y = screen_height // 8

# Set the size of the smaller square to 50
square_size = 50

# Flag to control the loop
running = True

try:
    # Main loop to keep the screen active indefinitely
    while running:
        # Rotate the cursor within the smaller square over 12 seconds
        end_time = time.time() + 12
        while time.time() < end_time:
            move_cursor_within_square(start_x, start_y, size=square_size, duration=3)
            time.sleep(1)  # Pause for 1 second before the next iteration
        # Shift the starting position for the next iteration
        start_x += 20
        start_y += 20
        # Make sure the cursor stays within the smaller square
        if start_x + square_size >= screen_width or start_y + square_size >= screen_height:
            start_x = screen_width // 8
            start_y = screen_height // 8

except KeyboardInterrupt: # CTRL+C
    print("Cursor movement stopped")
    running = False # Ends the script