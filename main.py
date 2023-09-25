from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk




class Student_Attendance_Sys:
    def __init__(self,root):
        self.root = root
        self.root.geometry(f"{window_width}x{window_height}+0+0")
        self.root.title("Student Attendance System")


        #first image
        img = Image.open(r"assets/collectedImages/vku.jpg")
        img=img.resize((500,130), Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        #second image
        img1 = Image.open(r"assets/collectedImages/vku.jpg")
        img1=img1.resize((500,130), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)



        #third image
        img2 = Image.open(r"assets/collectedImages/vku.jpg")
        img2=img2.resize((500,130), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #background image
        img3 = Image.open(r"assets/collectedImages/background.jpg")
        img3=img3.resize((1530,710), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)


        title_lbl=Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)






if __name__ == "__main__":
    root = Tk() 
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = int(screen_width)
    window_height = int(screen_height)
    root.state("zoomed") #Auto fullscreen
    obj=Student_Attendance_Sys(root)
    root.mainloop()
