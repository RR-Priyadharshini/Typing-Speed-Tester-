import tkinter as tk
from time import time

class TypingSpeedTester:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Speed Tester")
        self.master.geometry("600x400")
        self.text = ""
        self.start_time = None
        self.timer_running = False  # ⏱️ Timer control flag

        self.setup_input_window()

    def setup_input_window(self):
        self.input_label = tk.Label(self.master, text="Enter the text you want to use for typing test:", font=("Helvetica", 12))
        self.input_label.pack(pady=10)

        self.text_input = tk.Text(self.master, height=5, width=60, font=("Helvetica", 12))
        self.text_input.pack()

        self.start_button = tk.Button(self.master, text="Start Test", command=self.start_test)
        self.start_button.pack(pady=10)

    def start_test(self):
        self.text = self.text_input.get("1.0", tk.END).strip()
        if not self.text:
            return

        # Clear the input widgets
        self.input_label.destroy()
        self.text_input.destroy()
        self.start_button.destroy()

        self.build_test_ui()

    def build_test_ui(self):
        self.label = tk.Label(self.master, text="Type the following:", font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.text_display = tk.Label(self.master, text=self.text, wraplength=500, font=("Helvetica", 12))
        self.text_display.pack(pady=5)

        self.entry = tk.Text(self.master, height=5, width=60, font=("Helvetica", 12))
        self.entry.pack()
        self.entry.bind("<FocusIn>", self.start_typing)

        self.timer_label = tk.Label(self.master, text="Time: 0.0s", font=("Helvetica", 12))
        self.timer_label.pack(pady=5)

        self.result_label = tk.Label(self.master, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit)
        self.submit_button.pack(pady=5)

        self.restart_button = tk.Button(self.master, text="Restart", command=self.restart)
        self.restart_button.pack(pady=5)

        self.update_timer()

    def start_typing(self, event):
        if self.start_time is None:
            self.start_time = time()
            self.timer_running = True  # ✅ Start timer

    def update_timer(self):
        if self.timer_running and self.start_time:
            elapsed = time() - self.start_time
            self.timer_label.config(text=f"Time: {elapsed:.1f}s")
        self.master.after(100, self.update_timer)

    def submit(self):
        typed = self.entry.get("1.0", tk.END).strip()
        if not typed:
            self.result_label.config(text="Please type something first.")
            return

        self.timer_running = False  # ⛔ Stop timer

        end_time = time()
        time_taken = end_time - self.start_time
        wpm = len(typed.split()) / (time_taken / 60)
        accuracy = self.calculate_accuracy(typed, self.text)

        self.result_label.config(
            text=f"Completed!\nWPM: {wpm:.2f}\nAccuracy: {accuracy:.2f}%"
        )
        self.entry.config(state="disabled")

    def calculate_accuracy(self, typed, original):
        typed_words = typed.split()
        original_words = original.split()
        correct = sum(1 for tw, ow in zip(typed_words, original_words) if tw == ow)
        return (correct / len(original_words)) * 100

    def restart(self):
        # Reset everything
        for widget in self.master.winfo_children():
            widget.destroy()
        self.__init__(self.master)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTester(root)
    root.mainloop()
