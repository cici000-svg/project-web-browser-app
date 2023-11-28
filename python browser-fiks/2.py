import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
import webbrowser
import subprocess

class WebBrowser:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Browser")

        def on_click(event):
            if self.browser.get() == self.default_text:
                self.browser.delete(0, tk.END)
                self.browser.configure(fg="black")

        def on_leave(event):
            if not self.browser.get():
                self.browser.insert(0, self.default_text)
                self.browser.configure(fg="grey")

        root.configure(bg="#FDAE84")
        width, height = 800, 500 
        x = (root.winfo_screenwidth() - width) // 2
        y = (root.winfo_screenheight() - height) // 2
        root.geometry("{}x{}+{}+{}".format(width, height, x, y))

        self.frame = tk.Frame(root, bg="#FFFFFF", width=700)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self.image = PhotoImage(file="logowebb.png")
        self.image = self.image.zoom(1)

        self.image_label = tk.Label(self.frame, image=self.image)
        self.image_label.grid(row=0, column=0, columnspan=3, padx=40, pady=10)
        self.image_label.configure(bg="#ffffff")

        self.sites = {
            "Google": "https://www.google.com",
            "W3Schools": "https://www.w3schools.com/",
            "Code.org" : "https://code.org/",
            "edX" : "https://www.edx.org/course/subject/computer-science",
            "WhatsApp": "https://web.whatsapp.com/%F0%9F%8C%90/id",
            "Code": "https://code.org/",
            "Google Developer": "https://developers.google.com/",
            "Wikipedia": "https://www.wikipedia.org/",
            "DeepL": "https://www.deepl.com/translator",
            "Amazon": "https://www.amazon.com/",
            "The Warren Trust": "https://warrentrust.org.nz/",
            "Stuff & Nonsense": "https://stuffandnonsense.co.uk/",
            "Djangoforbeginners": "https://djangoforbeginners.com/",
            "libgen": "https://libgen.is/",
            "Bento.io": "https://bento.io/",
            "Upskill": "https://upskillcourses.com/"
        }

        self.site_choice = ttk.Combobox(self.frame, values=list(self.sites.keys()))
        self.site_choice.grid(row=1, column=0, padx=(20, 5), pady=5, sticky="ew",)
        self.site_choice.set("Google")

        self.default_text = "Jelajahi lewat sini atau pilih situs"

        self.browser = tk.Entry(self.frame, width=30)
        self.browser.grid(row=1, column=1, padx=0, pady=5, sticky="ew", ipady=1, ipadx=10)
        self.browser.configure(bg="#FFFFFF", fg="grey")
        self.browser.insert(0, self.default_text)

        self.browser.bind('<FocusIn>', on_click)
        self.browser.bind('<FocusOut>', on_leave)
        
        self.go_button = tk.Button(self.frame, text="Go", command=self.load_url)
        self.go_button.grid(row=1, column=2, padx=(5, 20), pady=5, sticky="ew")
        self.go_button.configure(bg="#8BCBC8", fg="#FFFFFF")

        self.logout_button = tk.Button(self.frame, text="Logout", command=self.navigate_logout, width=20)
        self.logout_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky="n")
        self.logout_button.configure(bg="#ECC7C0", fg="#FFFFFF")

        self.history = [] 
        self.history_index = -1 

        self.home_url = "https://google.com"
        self.current_url = self.home_url
        self.browser_var = tk.StringVar()
        self.browser_var.set(self.current_url)
        self.browser_object = webbrowser.get()

    def load_url(self):
        selected_site = self.site_choice.get()
        url = self.sites[selected_site]
        print(url)

        try:
            if url != self.current_url:  
                self.history.append(self.current_url)  
                self.history_index += 1  
                self.current_url = url  
                self.browser_var.set(url)  

                subprocess.Popen(["python", "3.py", url]) 
                self.root.withdraw()  
                
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def navigate_logout(self):
        if self.history_index > 0:
            self.history_index -= 1
            previous_url = self.history[self.history_index]
            self.browser_object.open(previous_url)
            self.current_url = previous_url
            self.browser_var.set(previous_url)
        else:
            messagebox.showinfo("Info", "No more pages to go back to. Navigating to 1.py")
            subprocess.Popen(["python", "1.py"])  
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = WebBrowser(root)
    root.mainloop()