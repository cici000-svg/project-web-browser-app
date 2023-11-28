import tkinter as tk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk

class LoginApp:
    def __init__(self, master):
        self.master = master
        self.valid_email = "pbo@gmail.com"
        self.valid_password = "aiueo"

        self.setup_ui()

    def setup_ui(self):
        self.master.title("Login")
        self.master.configure(bg="#FDAE84")

        width, height = 800, 500
        x = (self.master.winfo_screenwidth() - width) // 2
        y = (self.master.winfo_screenheight() - height) // 2
        self.master.geometry("{}x{}+{}+{}".format(width, height, x, y))

        frame_width = 600
        frame = tk.Frame(self.master, bg="#FFFFFF", width=frame_width)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        img = Image.open("logo_user.png")
        img = img.resize((60, 60), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(img)

        img_label = tk.Label(frame, image=self.photo, bg="#FFFFFF")
        img_label.grid(row=0, column=0, pady=10, sticky="n")

        email_var = tk.StringVar()
        password_var = tk.StringVar()

        self.email_entry = tk.Entry(frame, textvariable=email_var, fg="grey", font=("Arial", 12), width=40, bd=1,
                               relief=tk.GROOVE, highlightthickness=1, highlightbackground="gray")
        self.email_entry.insert(0, "Email")
        self.email_entry.bind("<FocusIn>", self.on_email_entry_focus_in)
        self.email_entry.bind("<FocusOut>", self.on_email_entry_focus_out)
        self.email_entry.grid(row=1, column=0, padx=20, pady=5, sticky="ew")

        self.password_entry = tk.Entry(frame, textvariable=password_var, show="", fg="grey", font=("Arial", 12), width=40,
                                  bd=1, relief=tk.GROOVE, highlightthickness=1, highlightbackground="gray")
        self.password_entry.insert(0, "Password")
        self.password_entry.bind("<FocusIn>", self.on_password_entry_focus_in)
        self.password_entry.bind("<FocusOut>", self.on_password_entry_focus_out)
        self.password_entry.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        login_button = tk.Button(frame, text="Login", command=self.check_login, bg="#ECC7C0", fg="white",
                                 font=("Arial", 12))
        login_button.grid(row=5, column=0, padx=20, pady=10, sticky="ew")

        img_corner_top = Image.open("logowebb.png")
        img_corner_top = img_corner_top.resize((100, 65), Image.ANTIALIAS)
        self.photo_corner_top = ImageTk.PhotoImage(img_corner_top)

        img_label_corner_top = tk.Label(self.master, image=self.photo_corner_top, bg="#FDAE84")
        img_label_corner_top.place(x=10, y=10)

        text_label_corner_top = tk.Label(self.master,
                                         text="Bingkai petualangan internet Anda bersama Hello Brow",
                                         fg="#000000", bg="#FDAE84", relief="ridge", padx=10, pady=5)
        text_label_corner_top.place(x=120, y=40)

    def check_login(self):
        entered_email = self.email_entry.get()
        entered_password = self.password_entry.get()

        if entered_email == self.valid_email and entered_password == self.valid_password:
            self.master.destroy()
            self.open_web_browser()
        else:
            messagebox.showerror("Login Gagal", "Email atau password invalid")

    def open_web_browser(self):
        subprocess.Popen(["python", "2.py"])

    def on_email_entry_focus_in(self, event):
        if self.email_entry.get() == "Email":
            self.email_entry.delete(0, "end")
            self.email_entry.config(fg="black")

    def on_email_entry_focus_out(self, event):
        if not self.email_entry.get():
            self.email_entry.insert(0, "Email")
            self.email_entry.config(fg="grey")

    def on_password_entry_focus_in(self, event):
        if self.password_entry.get() == "Password":
            self.password_entry.delete(0, "end")
            self.password_entry.config(fg="black", show="*")

    def on_password_entry_focus_out(self, event):
        if not self.password_entry.get():
            self.password_entry.insert(0, "Password")
            self.password_entry.config(fg="grey", show="")

if __name__ == "__main__":
    login_window = tk.Tk()
    app = LoginApp(login_window)
    login_window.mainloop()
