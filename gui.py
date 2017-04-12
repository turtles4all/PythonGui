from tkinter import *
import tkinter.messagebox


def donothing():
    print("Doing Nothing...")


def errorBox():
    tkinter.messagebox.showerror('There was an errror', 'This is the error message')


def questionBox():
    answer = tkinter.messagebox.askquestion('Question', 'Do you like silly faces?')
    if answer == 'yes':
        print("8===D~")


def exitFun():
    doexit = tkinter.messagebox.askquestion('Exit', 'Do you want to exit?')
    if doexit == 'yes':
        exit()

root = Tk()

# *******Build Layout*********
toolbar = Frame(root, bg="blue")
toolbar.pack(side=TOP, fill=X)
content = Frame(root, bg="gray")
content.pack(fill=BOTH)
bottomFrame = Frame(root, bg="blue")
bottomFrame.pack(side=BOTTOM, fill=X)

# ***********Menus************
menu = Menu(root)
root.config(menu=menu)  # add menu to root
subMenu = Menu(menu) # create menue named susMenu
subMenu.add_command(label="New Project...", command=donothing)  # add options to subMenu
subMenu.add_command(label="New", command=donothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=exit)
editMenu = Menu(menu)  # create edit menu
editMenu.add_command(label="Exit", command=exit)  # adds command to edit menu
menu.add_cascade(label="File", menu=subMenu)  # adds File and Edit drop down to main windows menu
menu.add_cascade(label="Edit", menu=editMenu)

# ***********Toolbar************
insertButt = Button(toolbar, text="Insert Image", command=errorBox)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Print", command=questionBox)
printButt.pack(side=LEFT, padx=2, pady=2)
exitButton = Button(toolbar, text='EXIT', bg='red', fg='black', command=exitFun)
exitButton.pack(side=RIGHT)

# ***********Status Bar***********
status = Label(bottomFrame, text="Preparing to do nothing", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X, padx=2, pady=2)

# ***********Canvas***************
canvasWidth = 650
canvasHeight = 400
canvas = Canvas(content, width=canvasWidth, height=canvasHeight, bg="gray", bd=6)
boxWidth = 500
boxHeight = 200
paddingX = (canvasWidth - boxWidth)/2  # calc padding to center
paddingY = (canvasHeight - boxHeight)/2
greenBox = canvas.create_rectangle(paddingY, paddingX, boxWidth, boxHeight, fill="green")  # xy position, size
canvas.pack(fill=BOTH)

# not sure why greenBox is not centered
'''
# ************image**************
logo = PhotoImage(file="logo.png")
image = Label(content, image=logo)
image.pack()

answer = tkinter.messagebox.askquestion('Question', 'remove green box?')
if answer == 'yes':
    canvas.delete(greenBox)
'''
#  ************text**************
textBox = Label(content, text="messages will be shown here", bd=1, relief=SUNKEN, anchor=W)
textBox.pack(side=BOTTOM, fill=X, padx=2, pady=2)
root.mainloop()
exit()
