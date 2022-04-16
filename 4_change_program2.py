from tkinter import *
from tkinter.filedialog import*
import keyboard

def func_open():
    global filename
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*gif"), ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_exit():
    window.quit()
    window.destroy()

def photoZoom(event):
    global photo
    photo = PhotoImage(file = filename)
    photo = photo.zoom(2, 2)
    pLabel.configure(image = photo)
    pLabel.image = photo

def photoSub(event):
    global photo
    photo = PhotoImage(file = filename)
    photo = photo.subsample(2, 2)
    pLabel.configure(image = photo)
    pLabel.image = photo

    
##2019038019 조민우

window = Tk()
window.geometry("500x500")
window.title("명화 감상하기")

photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand = 1, anchor = CENTER)


mainMenu = Menu(window)
window.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)

window.bind("<Up>", photoZoom)
window.bind("<Down>", photoSub)

window.mainloop()
