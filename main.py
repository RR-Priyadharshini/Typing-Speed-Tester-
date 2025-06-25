import tkinter as tk
from time import time
import random

texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing speed is measured in words per minute.",
    "Python is a powerful and versatile programming language.",
    "Learning to type fast can save a lot of time.",
    "Consistency and practice are the keys to improvement."
]

class TypingSpeedTester:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Speed Tester")
        self.master.geometry("600x400")
        self.text = random.choice(texts)
        self.start_time = None

        self.label = tk.Label(master, text="Type the following:", font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.text_display = tk.Label(master, text=self.text, wraplength=500, font=("Helvetica", 12))
        self.text_display.pack(pady=5)

        self.entry = tk.Text(master, height=5, width=60, font=("Helvetica", 12))
        self.entry.pack()
        self.entry.bind("<FocusIn>", self.start_typing)
        self.entry.bind("<KeyRelease>", self.check_text)

        self.timer_label = tk.Label(master, text="⏱️ Time: 0.0s", font=("Helvetica", 12))
        self.timer_label.pack(pady=5)

        self.result_label = tk.Label(master, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

        self.restart_button = tk.Button(master, text="Restart", command=self.restart)
        self.restart_button.pack(pady=10)

        self.update_timer()

    def start_typing(self, event):
        if self.start_time is None:
            self.start_time = time()

    def update_timer(self):
        if self.start_time:
            elapsed = time() - self.start_time
            self.timer_label.config(text=f"⏱️ Time: {elapsed:.1f}s")
        self.master.after(100, self.update_timer)

    def check_text(self, event):
        typed = self.entry.get("1.0", tk.END).strip()
        if typed == self.text:
            end_time = time()
            time_taken = end_time - self.start_time
            wpm = len(typed.split()) / (time_taken / 60)
            accuracy = self.calculate_accuracy(typed, self.text)
            self.result_label.config(
                text=f"✅ Completed!
WPM: {wpm:.2f}
Accuracy: {accuracy:.2f}%"
            )

    def calculate_accuracy(self, typed, original):
        typed_words = typed.split()
        original_words = original.split()
        correct = sum(1 for tw, ow in zip(typed_words, original_words) if tw == ow)
        return (correct / len(original_words)) * 100

    def restart(self):
        self.text = random.choice(texts)
        self.text_display.config(text=self.text)
        self.entry.delete("1.0", tk.END)
        self.result_label.config(text="")
        self.start_time = None
        self.timer_label.config(text="⏱️ Time: 0.0s")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTester(root)
    root.mainloop()
