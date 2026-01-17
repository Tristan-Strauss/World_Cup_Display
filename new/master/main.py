import threading
from gui import VideoPlayer
from keyboardListener import KeyboardListener
from console import SlaveController
from gpio import GPIOController
import time

# --- Init hardware ---
slave = SlaveController()
gpio = GPIOController()

# --- Init GUI ---
player = VideoPlayer()

# --- Callback from keyboard thread ---
def handle_valid_year(year, video_name):
    print(f"[+] Year accepted: {year}")
    # Start GPIO
    if gpio.check_if_year_local(year):
        pin = gpio.get_pin_from_master_year_dict(year)
        gpio.set_pin_high(pin)
    else:
        pin = gpio.get_pin_from_slave_year_dict(year)
        slave.send(f"{pin}_High")
    # Play Video
    player.play_by_name(video_name)
    # Stop GPIO
    if gpio.check_if_year_local(year):
        pin = gpio.get_pin_from_master_year_dict(year)
        gpio.set_pin_low(pin)
    else:
        pin = gpio.get_pin_from_slave_year_dict(year)
        slave.send(f"{pin}_Low")

# --- Start keyboard listener in background ---
keyboard_listener = KeyboardListener(handle_valid_year)
kb_thread = threading.Thread(target=keyboard_listener.start, daemon=True)
kb_thread.start()

# --- Start GUI (main thread) ---
player.start()
