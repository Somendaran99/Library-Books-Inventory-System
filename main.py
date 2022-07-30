from tkinter import *
from PIL import ImageTk,Image
import pymysql
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *

# Add your own database name and password here to reflect in the code
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password="",database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Library")
root.minsize(width=100,height=100)
root.geometry("1920x1080")

# Take n greater than 0.25 and less than 5
same=True
n=1.5

# Adding a background image
background_image =Image.open("Final.jpeg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)
canvas = Canvas(width=1000, height=900, bg='blue')
canvas.pack(expand=YES, fill=BOTH)

image = ImageTk.PhotoImage(background_image)
canvas.create_image(0,0, image=image, anchor=NW)

Canvas1.create_image(800,1000,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="blue",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="UNIMAP LIBRARY", bg='black', fg='yellow', font=('Times New Roman',40,"bold"))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Book Details",bg='black', fg='white',font=("Times New Roman",20,"bold"), command=addBook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete Book",bg='black', fg='white',font=("Times New Roman",20,"bold"), command=delete)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View Book List",bg='black', fg='white',font=("Times New Roman",20,"bold"), command=View)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
   
btn4 = Button(root,text="Book Rental",bg='black', fg='white',font=("Times New Roman",20,"bold"), command = issueBook)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Return Book",bg='black', fg='white',font=("Times New Roman",20,"bold"), command = returnBook)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop()
