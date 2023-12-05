#do in this class
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

#create form and mysql 
class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry(f"{window_width}x{window_height}+0+0")
        self.root.title("Student")


        #first image
        img = Image.open(r"assets/collectedImages/vku.jpg")
        img=img.resize((int(screen_width/3),130), Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=screen_width/3,height=130)


        #second image
        img1 = Image.open(r"assets/collectedImages/vku.jpg")
        img1=img1.resize((int(screen_width/3),130), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=screen_width/3,y=0,width=screen_width/3,height=130)


        #third image
        img2 = Image.open(r"assets/collectedImages/vku.jpg")
        img2=img2.resize((int(screen_width/3),130), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=2*screen_width/3,y=0,width=screen_width/3,height=130)
        #bg image

        img3 = Image.open(r"assets/collectedImages/background.jpg")
        img3=img3.resize((screen_width,screen_height), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=screen_width,height=screen_height)
        

        #text
        title_lbl=Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=screen_width,height=45)

        #main frame
        main_frame = Frame(bg_img,bd=2)
        main_frame.place(x=spaceX,y=spaceY,width=screen_width-2*spaceX,height=screen_height)

        #left label frame 
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=spaceX,y=spaceX,width=screen_width/2,height=screen_height/1.5)

        img_left = Image.open(r"assets/collectedImages/vku.jpg")
        img_left=img_left.resize((int(screen_width),130), Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=spaceX,y=0,width=screen_width/2-spaceX*2,height=130)


        #current course
        
        current_course_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Current Course", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=spaceX,y=135,width=screen_width/2-spaceX*2,height=screen_height/6)
        
        #Department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"))
        dep_label.grid(row=0,column=0)

        dep_combo=ttk.Combobox(current_course_frame, font=("times new roman", 12, "bold"), state="readonly", width=int(spaceX*2 ))
        dep_combo['values']=('Select Department', 'Computer', 'IT', 'Civil', 'Mechnical')
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"))
        course_label.grid(row=0,column=2)

        course_combo=ttk.Combobox(current_course_frame, font=("times new roman", 12, "bold"), state="readonly", width=int(spaceX*2  ))
        course_combo['values']=('Select course', 'BE', 'SE', 'FE', 'TE')
        course_combo.current(0)
        
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"))
        year_label.grid(row=1,column=0)

        year_combo=ttk.Combobox(current_course_frame, font=("times new roman", 12, "bold"), state="readonly", width=int(spaceX*2    ))
        year_combo['values']=('Select year', '2020-2021', '2021-2022', '2022-2023', '2023-2024')
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester

        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"))
        semester_label.grid(row=1,column=2)

        semester_combo=ttk.Combobox(current_course_frame, font=("times new roman", 12, "bold"), state="readonly", width=int(spaceX*2    ))
        semester_combo['values']=('Select semester', '1', '2')
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #Student Information

        student_course_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Student Information", font=("times new roman", 12, "bold"))
        student_course_frame.place(x=spaceX,y=135+screen_height/6,width=screen_width/2-spaceX*2,height=screen_height/2)

        #StudentID

        student_label = Label(student_course_frame, text='Student ID', font=("times new roman", 12, "bold"))
        student_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)

        student_entry = ttk.Entry(student_course_frame,  font=("times new roman", 12, "bold"), width=spaceX*2)
        student_entry.grid(row=0,column=1,padx=10,sticky=W)

        #StudentName

        name_label = Label(student_course_frame, text='Student Name', font=("times new roman", 12, "bold"))
        name_label.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        name_entry = ttk.Entry(student_course_frame,  font=("times new roman", 12, "bold"), width=spaceX*2)
        name_entry.grid(row=0,column=3,padx=10,sticky=W)

        #DoB

        date_label = Label(student_course_frame, text='DOB', font=("times new roman", 12, "bold"))
        date_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)

        date_entry = ttk.Entry(student_course_frame,  font=("times new roman", 12, "bold"), width=spaceX*2)
        date_entry.grid(row=1,column=1,padx=10,sticky=W)

        #Gender
        gender_label = Label(student_course_frame, text='Gender', font=("times new roman", 12, "bold"))
        gender_label.grid(row=1,column=2,padx=2,pady=10,sticky=W)

        gender_combo=ttk.Combobox(student_course_frame, font=("times new roman", 12, "bold"), state="readonly", width=int(spaceX*2    ))
        gender_combo['values']=('Select gender', 'Male', 'Female', 'Orthers')
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=10,sticky=W)

        #Email

        email_label = Label(student_course_frame, text='Email', font=("times new roman", 12, "bold"))
        email_label.grid(row=2,column=0,padx=2,pady=10,sticky=W)

        email_entry = ttk.Entry(student_course_frame,  font=("times new roman", 12, "bold"), width=spaceX*2)
        email_entry.grid(row=2,column=1,padx=10,sticky=W)

        #Phone

        phone_label = Label(student_course_frame, text='Phone', font=("times new roman", 12, "bold"))
        phone_label.grid(row=2,column=2,padx=2,pady=10,sticky=W)

        phone_entry = ttk.Entry(student_course_frame,  font=("times new roman", 12, "bold"), width=spaceX*2)
        phone_entry.grid(row=2,column=3,padx=10,sticky=W)


        #Photos

        radiobtn1 = ttk.Radiobutton(student_course_frame, text= 'Take Photo Sample', value="Yes")
        radiobtn1.grid(row=3,column=0)

        radionbtn2 = ttk.Radiobutton(student_course_frame, text= 'No Photo Sample', value = "Yes")
        radionbtn2.grid(row=3,column=1)

        #button frames

        btn_frame = Frame(student_course_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=155,width=660,height=spaceY)



        save_btn = Button(btn_frame,text="Save",width=int(spaceX),font=("times new roman", 12, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)


        update_btn = Button(btn_frame,text="Update",width=int(spaceX),font=("times new roman", 12, "bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)


        delete_btn = Button(btn_frame,text="Delete",width=int(spaceX),font=("times new roman", 12, "bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)


        reset_btn = Button(btn_frame,text="Reset",width=int(spaceX),font=("times new roman", 12, "bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        take_photo_btn = Button(btn_frame,text="Take Photo",width=int(spaceX*1.3),font=("times new roman", 12, "bold"),bg="red",fg="white")
        take_photo_btn.grid(row=0,column=4)

        update_photo_btn = Button(btn_frame,text="Update Photo",width=int(spaceX*1.3),font=("times new roman", 12, "bold"),bg="red",fg="white")
        update_photo_btn.grid(row=0,column=5)

        #right label frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=spaceX+screen_width/2,y=spaceX,width=screen_width/2,height=screen_height/1.6)
        
        img_right = Image.open(r"assets/collectedImages/students.jpg")
        img_right=img_right.resize((int(screen_width),130), Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=spaceX,y=0,width=screen_width/2-spaceX*2,height=130)

    #=====Search System=========
        search_frame = LabelFrame(right_frame, bd=2, relief=RIDGE, text="Search system", font=("times new roman", 12, "bold"))
        search_frame.place(x=spaceX,y=135,width=screen_width/2-spaceX*4,height=70)

        search_label = Label(search_frame, text='Search by', font=("times new roman", 15, "bold"),bg="red", fg="white")
        search_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)

        search_combo=ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), state="readonly", width=int(spaceX*1.5))
        search_combo['values']=('Select', 'Roll_No', 'Phone_No')
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry = ttk.Entry(search_frame,  font=("times new roman", 12, "bold"), width=spaceX*2)
        search_entry.grid(row=0,column=2,padx=10,sticky=W)

        search_combo_btn = Button(search_frame,text="Search",width=int(spaceX),font=("times new roman", 12, "bold"),bg="blue",fg="white")
        search_combo_btn.grid(row=0,column=3,padx=5)


        showAll_btn = Button(search_frame,text="Show All",width=int(spaceX),font=("times new roman", 12, "bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=5) 


    #=====Table frame=========
        table_frame =Frame(right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=spaceX,y=210,width=screen_width/2-spaceX*4,height=300)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","dob","gender","email","phone","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="StudentName")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width="100")
        self.student_table.column("course",width="100")
        self.student_table.column("year",width="100")
        self.student_table.column("sem",width="100")
        self.student_table.column("id",width="100")
        self.student_table.column("name",width="100")
        self.student_table.column("dob",width="100")
        self.student_table.column("gender",width="100")
        self.student_table.column("email",width="100")
        self.student_table.column("phone",width="100")
        self.student_table.column("photo",width="150")
        

        self.student_table.pack(fill=BOTH,expand=1)       



if __name__ == "__main__":
    root = Tk() 
    spaceX = 10
    spaceY = 50
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = int(screen_width)
    window_height = int(screen_height)
    root.state("zoomed")
    obj=Student(root)
    root.mainloop()
#generate dataset