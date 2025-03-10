import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("🎵 مشغل الموسيقى البسيط")
        self.root.geometry("400x300")
        
        pygame.mixer.init()

        self.label = tk.Label(root, text="اختر ملف موسيقى", font=("Arial", 14))
        self.label.pack(pady=20)

        self.play_button = tk.Button(root, text="🎵 تشغيل", command=self.play_music, font=("Arial", 12))
        self.play_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="⏹ إيقاف", command=self.stop_music, font=("Arial", 12))
        self.stop_button.pack(pady=5)

        self.select_button = tk.Button(root, text="📂 اختر ملف", command=self.load_music, font=("Arial", 12))
        self.select_button.pack(pady=10)

        self.file_path = ""

    def load_music(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("ملفات الصوت", "*.mp3;*.wav")])
        if self.file_path:
            self.label.config(text="🎶 " + self.file_path.split("/")[-1])

    def play_music(self):
        if self.file_path:
            pygame.mixer.music.load(self.file_path)
            pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
