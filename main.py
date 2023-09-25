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


        title_lbl=Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        #student button
        img4 = Image.open(r"assets/collectedImages/student_detail.jpg")
        img4=img4.resize((220,220), Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img, image=self.photoimg4, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1=Button(bg_img,text="Student Details", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)


        #Detect face button 
        img5 = Image.open(r"assets/collectedImages/face_detector.jpg")
        img5=img5.resize((220,220), Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img, image=self.photoimg5, cursor="hand2")
        b1.place(x=500, y=100, width=220, height=220)

        b1_1=Button(bg_img,text="Face Detector", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)  



        #Attendace face button 
        img6 = Image.open(r"assets/collectedImages/attendace_face.jpg")
        img6=img6.resize((220,220), Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img, image=self.photoimg6, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)

        b1_1=Button(bg_img,text="Attendace", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)  


        #Help face button 
        img7 = Image.open(r"assets/collectedImages/help_face.png")
        img7=img7.resize((220,220), Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img, image=self.photoimg7, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1=Button(bg_img,text="Help Desk", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)  


        #Train face button 
        img8 = Image.open(r"assets/collectedImages/train_face.jpg")
        img8=img8.resize((220,220), Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img, image=self.photoimg8, cursor="hand2")
        b1.place(x=200, y=380, width=220, height=220)
        b1_1=Button(bg_img,text="Train Data", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200, y=580, width=220, height=40)  


        #Photos face button 
        img9 = Image.open(r"assets/collectedImages/photo.jpg")
        img9=img9.resize((220,220), Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img, image=self.photoimg9, cursor="hand2")
        b1.place(x=500, y=380, width=220, height=220)
        b1_1=Button(bg_img,text="Photos", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500, y=580, width=220, height=40)  


        #Developer face button 
        img10 = Image.open(r"assets/collectedImages/developer_face.jpg")
        img10=img10.resize((220,220), Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img, image=self.photoimg10, cursor="hand2")
        b1.place(x=800, y=380, width=220, height=220)
        b1_1=Button(bg_img,text="Developer", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800, y=580, width=220, height=40)  



        #Exit face button 
        img11 = Image.open(r"assets/collectedImages/exit.jpg")
        img11=img11.resize((220,220), Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img, image=self.photoimg11, cursor="hand2")
        b1.place(x=1100, y=380, width=220, height=220)
        b1_1=Button(bg_img,text="Exit", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100, y=580, width=220, height=40)  




if __name__ == "__main__":
    root = Tk() 
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = int(screen_width)
    window_height = int(screen_height)
    root.state("zoomed") #Auto fullscreen
    obj=Student_Attendance_Sys(root)
    root.mainloop()
