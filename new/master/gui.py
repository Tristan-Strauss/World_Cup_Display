import tkinter as tk
import subprocess
import threading
import os
import signal
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

class VideoPlayer:
    START_YEAR = 1930
    END_YEAR = 2134
    STEP = 4

    def __init__(self):
        # Tkinter fullscreen black window
        self.root = tk.Tk()
        self.root.configure(bg="black")
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda e: self._exit())

        # Track VLC process and thread safety
        self.current_process = None
        self.lock = threading.Lock()

    # ---------- Internal helpers ----------

    def _exit(self):
        """Stop VLC and exit"""
        self.stop()
        self.root.destroy()
        os._exit(0)  # ensures all threads stop

    def _play_vlc(self, filename: str):
        path = BASE_DIR / filename
        if not path.exists():
            print(f"ERROR: Video not found: {path}")
            return

        def target():
            with self.lock:
                # Stop current video if running
                if self.current_process and self.current_process.poll() is None:
                    os.kill(self.current_process.pid, signal.SIGKILL)
                    self.current_process = None

                # Schedule black screen in Tkinter main thread
                self.root.after(0, self.root.deiconify)
                self.root.after(0, self.root.lift)
                self.root.after(0, lambda: self.root.config(cursor="none"))


                # Start VLC (fullscreen)
                self.current_process = subprocess.Popen(
                    [
                        "vlc",
                        "--fullscreen",          # video will go fullscreen immediately
                        "--no-video-title-show", # hides the title overlay
                        "--no-embedded-video",   # avoids embedding in VLC GUI window
                        "--no-video-deco",       # hides borders/window decorations
                        "--play-and-exit",
                        "--quiet",
                        "--video-on-top",        # ensure VLC appears above everything
                        str(path)
                    ],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )


            self.current_process.wait()

            # After video ends, bring back black window (main thread)
            with self.lock:
                self.current_process = None
                self.root.after(0, self.root.deiconify)
                self.root.after(0, self.root.lift)
                self.root.after(0, lambda: self.root.config(cursor="arrow"))

        threading.Thread(target=target, daemon=True).start()

    # ---------- Public API ----------

    def play_year(self, year: int):
        if (
            year < self.START_YEAR
            or year > self.END_YEAR
            or (year - self.START_YEAR) % self.STEP != 0
        ):
            print(f"ERROR: Invalid year {year}")
            return

        self._play_vlc(f"{year}.mp4")

    def play_by_name(self, name: str):
        try:
            year = int(name)
        except ValueError:
            print(f"ERROR: Invalid video name '{name}'")
            return
        self.play_year(year)

    def stop(self):
        with self.lock:
            if self.current_process and self.current_process.poll() is None:
                os.kill(self.current_process.pid, signal.SIGKILL)
                self.current_process = None

    # ---------- Run the GUI ----------
    def start(self):
        """Start Tkinter mainloop (must be called from main thread)"""
        self.root.mainloop()
