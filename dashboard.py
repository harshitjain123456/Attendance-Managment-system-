from tkinter import*
from PIL import ImageTk,Image
from main import Student
from faculty import Faculty
from attendence import Attendence
class SMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1750x800+0+0")
        self.root.title("Face Attendance Management System")

        #=======title=======
        self.img1 = Image.open("Images/43.jpeg")
        self.img1 = self.img1.resize((285, 177), Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(self.img1)

        self.img2 = Image.open("Images/37.jpeg")
        self.img2 = self.img2.resize((285, 177), Image.ANTIALIAS)
        self.img2 = ImageTk.PhotoImage(self.img2)

        self.img3 = Image.open("Images/40.jpeg")
        self.img3 = self.img3.resize((285, 177), Image.ANTIALIAS)
        self.img3 = ImageTk.PhotoImage(self.img3)

        self.img4 = Image.open("Images/41.jpeg")
        self.img4 = self.img4.resize((285, 177), Image.ANTIALIAS)
        self.img4 = ImageTk.PhotoImage(self.img4)

        self.img5 = Image.open("Images/38.jpeg")
        self.img5 = self.img5.resize((285, 177), Image.ANTIALIAS)
        self.img5 = ImageTk.PhotoImage(self.img5)

        self.img6 = Image.open("Images/42.jpeg")
        self.img6 = self.img6.resize((285, 177), Image.ANTIALIAS)
        self.img6 = ImageTk.PhotoImage(self.img6)

        self.bg_icon = Image.open("Images/bg1.jpg")
        self.bg_icon=self.bg_icon.resize((1600,800),Image.ANTIALIAS)
        self.bg_icon = ImageTk.PhotoImage(self.bg_icon)

        my_canvas= Canvas(self.root,width=1350,height=780)
        my_canvas.pack(fill="both",expand=True)
        my_canvas.create_image(0,0,image=self.bg_icon , anchor="nw")
        my_canvas.create_text(800,40,text="Face Attendance Management System",font=("times new roman",40,"bold"), fill="white")


        button1 = Button(root, image=self.img1, command=self.main)
        button2 = Button(root, image=self.img2 ,command=self.faculty)
        button3 = Button(root, image=self.img3,command=self.attendence)
        button4 = Button(root, image=self.img4)
        button5 = Button(root, image=self.img5)
        button6 = Button(root, image=self.img6)

        button1_window = my_canvas.create_window(350,250,window=button1)
        button2_window = my_canvas.create_window(750,250,window=button2)
        button3_window = my_canvas.create_window(1150,250,window=button3)
        button4_window = my_canvas.create_window(350,510,window=button4)
        button5_window = my_canvas.create_window(750,510,window=button5)
        button6_window = my_canvas.create_window(1150,510,window=button6)

    def main(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Student(self.new_win)

    def faculty(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Faculty(self.new_win)

    def attendence(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Attendence(self.new_win)


if __name__=="__main__":
    root = Tk()
    obj = SMS(root)
    root.mainloop()