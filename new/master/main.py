import threading
from gui import VideoPlayer
from keyboardListener import KeyboardListener
from console import SlaveController

# --- Init hardware ---
slave = SlaveController()

# --- Init GUI ---
player = VideoPlayer()

# --- Callback from keyboard thread ---
def handle_valid_year(year, video_name):
    print(f"[✓] Year accepted: {year}")

    # Tell GUI (thread-safe)
    # player.root.after(0, player.play_by_name, video_name)
    player.play_by_name(video_name)

    # Send command to slave
    slave.send(f"YEAR_{year}")

# --- Start keyboard listener in background ---
keyboard_listener = KeyboardListener(handle_valid_year)
kb_thread = threading.Thread(target=keyboard_listener.start, daemon=True)
kb_thread.start()

# --- Start GUI (main thread) ---
player.start()

# try:
#     while True:
#         pass  # Keeps the program alive
# except KeyboardInterrupt:
#     print("Exiting...")
