from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from course import courseClass
from student import studentClass
from result import resultClass
from report import reportClass
from exit import exitclass  # ✅ Import exitclass
from tkinter import messagebox
import os
from datetime import *
import time
from math import *
import sqlite3

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x655+0+0")
        self.root.config(bg="white")

        # Logo
        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")
        title = Label(self.root, text="Student Result Management System", padx=10, compound=LEFT,
                      image=self.logo_dash, font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)

        # Menu Frame
        M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_Frame.place(x=10, y=70, width=1260, height=80)

        Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white", cursor="hand2", command=self.add_course).place(x=10, y=5, width=200, height=40)

        Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white", cursor="hand2", command=self.add_student).place(x=220, y=5, width=200, height=40)

        Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white", cursor="hand2", command=self.add_result).place(x=430, y=5, width=200, height=40)

        Button(M_Frame, text="View Student Result", font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white", cursor="hand2", command=self.add_report).place(x=640, y=5, width=200, height=40)

        Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white", cursor="hand2", command=self.logout).place(x=850, y=5, width=200, height=40)

        Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white", cursor="hand2", command=self.open_exit_window).place(x=1060, y=5, width=180, height=40)

        # Background Image
        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((920, 350))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        Label(self.root, image=self.bg_img).place(x=330, y=180, width=920, height=350)

        # Stat Boxes
        self.lbl_course = Label(self.root, text="Total Courses\n[ 0 ]",
                                font=("goudy old style", 20), bd=10, relief=RIDGE,
                                bg="#e43b06", fg="white")
        self.lbl_course.place(x=330, y=530, width=300, height=90)

        self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]",
                                 font=("goudy old style", 20), bd=10, relief=RIDGE,
                                 bg="#0676ad", fg="white")
        self.lbl_student.place(x=640, y=530, width=300, height=90)

        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]",
                                font=("goudy old style", 20), bd=10, relief=RIDGE,
                                bg="#038074", fg="white")
        self.lbl_result.place(x=950, y=530, width=300, height=90)

        # Footer
        footer = Label(self.root, text="SRMS - Student Result Management System - Developed by Syed Ayan & M.Areeb",
                       font=("goudy old style", 12), bg="#262626", fg="white")
        footer.pack(side=BOTTOM, fill=X)

        self.update_details()

    def update_details(self):
        try:
            con = sqlite3.connect(database="rms.db")
            cur = con.cursor()

            cur.execute("select * from course")
            self.lbl_course.config(text=f"Total Courses\n[{len(cur.fetchall())}]")

            cur.execute("select * from student")
            self.lbl_student.config(text=f"Total Students\n[{len(cur.fetchall())}]")

            cur.execute("select * from result")
            self.lbl_result.config(text=f"Total Results\n[{len(cur.fetchall())}]")

            self.root.after(1000, self.update_details)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def open_exit_window(self):
        self.exit_win = Toplevel(self.root)
        self.exit_obj = exitclass(self.exit_win)

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = courseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)

    def logout(self):
        op = messagebox.askyesno("Confirm", "Do you really want to logout?", parent=self.root)
        if op:
            self.root.destroy()
            os.system("python login.py")


if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
