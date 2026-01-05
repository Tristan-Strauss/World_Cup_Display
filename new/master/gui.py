import tkinter as tk
from pathlib import Path
from tkVideoPlayer import TkinterVideo

BASE_DIR = Path(__file__).resolve().parent

class VideoPlayer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg="black")
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda e: self.root.destroy())

        self.video = TkinterVideo(
            master=self.root,
            scaled=True,
            keep_aspect=True,
            bg="black"
        )

        self.video.bind("<<Ended>>", self._on_video_end)

        self._show_black()

    # ---------- Internal helpers ----------

    def _show_black(self):
        self.video.stop()
        self.video.pack_forget()
        self.root.configure(bg="black")

    def _on_video_end(self, event=None):
        self._show_black()

    def _play(self, filename):
        path = BASE_DIR / filename

        if not path.exists():
            print(f"ERROR: Video not found: {path}")
            return

        self.video.stop()
        self.video.pack_forget()

        self.video.pack(expand=True, fill="both")
        self.video.load(str(path))
        self.video.play()

    # ---------- Public API ----------

    def play_video_1(self):
        self._play("video1.mp4")

    def play_video_2(self):
        self._play("video2.mp4")

    def play_video_3(self):
        self._play("video3.mp4")

    def start(self):
        self.root.mainloop()
