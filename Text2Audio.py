import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import threading
import speech_recognition as sr

class VoiceToTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice to Text")

        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        self.listening = False
        self.listener_thread = None

        # Buttons
        self.start_button = tk.Button(root, text="Start Rec", command=self.start_recording)
        self.start_button.grid(row=0, column=0, padx=10, pady=10)

        self.stop_button = tk.Button(root, text="Stop Rec", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.grid(row=0, column=1, padx=10, pady=10)

        # Text area
        self.text_area = ScrolledText(root, wrap=tk.WORD, width=60, height=20)
        self.text_area.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def start_recording(self):
        if self.listening:
            return
        self.listening = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.text_area.insert(tk.END, "\nStarted Listening...\n")
        self.listener_thread = threading.Thread(target=self.listen_in_background)
        self.listener_thread.start()

    def listen_in_background(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            while self.listening:
                try:
                    audio = self.recognizer.listen(source, timeout=2, phrase_time_limit=5)
                    text = self.recognizer.recognize_google(audio)
                    self.text_area.insert(tk.END, text + ' ')
                    self.text_area.see(tk.END)
                except sr.WaitTimeoutError:
                    # No speech detected within timeout, continue listening
                    continue
                except sr.UnknownValueError:
                    self.text_area.insert(tk.END, "[Could not understand]\n")
                except sr.RequestError as e:
                    messagebox.showerror("Error", f"Could not request results; {e}")
                    break

    def stop_recording(self):
        if not self.listening:
            return
        self.listening = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.text_area.insert(tk.END, "\nStopped Listening.\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceToTextApp(root)
    root.mainloop()

