from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk




class Student_Attendance_Sys:
    def __init__(self,root):
        self.root = root
        self.root.geometry(f"{window_width}x{window_height}+0+0")
        self.root.title("Student Attendance System")

        img = Image.open(r"assets/collectedImages/vku.jpg")
        img=img.resize((500,130), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)






if __name__ == "__main__":
    root = Tk() 
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = int(screen_width)
    window_height = int(screen_height)
    root.state("zoomed") #Auto fullscreen
    obj=Student_Attendance_Sys(root)
    root.mainloop()
