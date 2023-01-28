# importing pandas module
import pandas as pd
from tkinter import filedialog
from tkinter import *

root = Tk()
root.title('CSV to Excel')
root.resizable(False, False)
root.geometry('150x75')

def open():
    path=filedialog.askopenfilename()
    cvsDataframe = pd.read_csv(path)
    path=path[:-3]
    resultExcelFile = pd.ExcelWriter(path+'xlsx')
    cvsDataframe.to_excel(resultExcelFile, index=False)
    resultExcelFile.close()
    print("Succes")
    root.destroy()

button = Button(root,text="Choose file",command=open)
button.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()

