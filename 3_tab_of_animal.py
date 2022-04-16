from tkinter import*
from tkinter import ttk  ##ttk모듈

window = Tk()
window.iconbitmap('python.ico')

baseTab = ttk.Notebook(window)

tabDog = ttk.Frame(baseTab)
baseTab.add(tabDog, text = '강아지')
tabCat = ttk.Frame(baseTab)
baseTab.add(tabCat, text = '고양이')

## 2019038019 조민우

baseTab.pack(expand = 1, fill = "both")

photoDog = PhotoImage(file = "gif/dog2.gif")
labelDog = Label(tabDog, image = photoDog)
labelDog.pack()

photoCat = PhotoImage(file = "gif/cat2.gif")
labelCat = Label(tabCat, image = photoCat)
labelCat.pack()

window.mainloop()
