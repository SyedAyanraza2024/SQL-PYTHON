from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class exitclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Exit Confirmation - SRMS")
        self.root.geometry("400x250+500+250")
        self.root.config(bg="white")
        self.root.resizable(False, False)

        # Logo
        try:
            self.logo_dash = ImageTk.PhotoImage(file="images/images/logo_p.png")
            Label(self.root, image=self.logo_dash, bg="white").place(x=10, y=10, width=60, height=60)
        except:
            pass  # Skip logo if image not found

        # Title
        Label(self.root, text="Exit Application?", font=("JetBrains Mono", 16, "bold"), fg="#033054", bg="white").place(x=100, y=30)

        # Message
        Label(self.root, text="Are you sure you want to exit?\nAll unsaved work will be lost.", 
              font=("goudy old style", 12), fg="black", bg="white", justify=CENTER).place(x=50, y=80)

        # Buttons
        Button(self.root, text="Yes, Exit", font=("goudy old style", 12, "bold"), bg="red", fg="white", width=12, command=self.exit_app).place(x=80, y=150)
        Button(self.root, text="No, Cancel", font=("goudy old style", 12, "bold"), bg="green", fg="white", width=12, command=self.cancel_exit).place(x=210, y=150)

    def exit_app(self):
        self.root.destroy()  # Close exit window
        quit()               # Fully exit program

    def cancel_exit(self):
        self.root.destroy()  # Just close this confirmation window


if __name__ == "__main__":
    root = Tk()
    obj = exitclass(root)
    root.mainloop()
