import tkinterweb
from tkinter import *
import sys
import subprocess

class Situs(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Situs")
        self.configure(bg="#ffffff")

        button_style = {'background': '#8BCBC8', 'foreground': 'white', 'padx': 10, 'pady': 5, 'relief': 'raised'}

        if len(sys.argv) > 1:
            frame_button = Frame(self, bg="#FFFFFF")
            frame_button.pack(fill='both')

            self.back_button = Button(frame_button, text="Back", command=self.go_back, **button_style)
            self.back_button.grid(row=0, column=0, padx=(0,10), sticky="w")
            self.back_button.bind("<Enter>", self.on_back_enter)
            self.back_button.bind("<Leave>", self.on_back_leave)

            self.back_label = Label(frame_button, text="", bg="#FFFFFF", fg="green")
            self.back_label.grid(row=1, column=0, padx=(0,10),sticky="w")

            self.forward_button = Button(frame_button, text="Forward", command=self.go_forward, **button_style)
            self.forward_button.grid(row=0, column=1, padx=10, sticky="w")
            self.forward_button.bind("<Enter>", self.on_forward_enter)
            self.forward_button.bind("<Leave>", self.on_forward_leave)

            self.forward_label = Label(frame_button, text="", bg="#FFFFFF", fg="red")
            self.forward_label.grid(row=1, column=1, padx=10, sticky="w")

            url = sys.argv[1]
            self.frame = tkinterweb.HtmlFrame(self)
            self.frame.load_website(url)
            self.frame.pack(fill='both', expand=True)

    def go_back(self):
        subprocess.Popen(["python", "2.py"])
        self.destroy()

    def go_forward(self):
        self.frame.forward()

    def on_back_enter(self, event):
        self.back_label.config(text="Klik Back, untuk kembali ke main Web Browser")
        self.back_button.config(relief='sunken')

    def on_back_leave(self, event):
        self.back_label.config(text="")
        self.back_button.config(relief='raised')

    def on_forward_enter(self, event):
        self.forward_label.config(text="Maaf, button ini belum memiliki fungsi yang berarti")

    def on_forward_leave(self, event):
        self.forward_label.config(text="")

if __name__ == "__main__":
    app = Situs()
    app.mainloop()
