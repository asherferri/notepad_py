import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
class Notepad:
    __root = Tk()
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)

__thisScrollBar = Scrollbar(__thisTextArea)
__file = None
def __init__(self, **kwargs)

    try:
        self.__root.wm_iconbitmap('Notepad.ico')
    except:
        pass

    try:
        self.__thisWidth = kwargs['width']
    except KeyError:
        pass
    try:
        self.__thisHeight = kwargs['height']
    except KeyError:
        pass

    self.__root.title("Untitled - Notepad")

    screenWidth = self.__root.winfo_screenwidth()
    screenHeight = self._root.winfo_screenheight()
    
    left = (screenWidth / 2) - (self.__thisWidth / 2)

    top = (screenHeight / 2) - (self.__thisHeight / 2)

    self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

    self.__root.grid_rowconfigure(0, weight=1)
    self.__root.grid_columnconfigure(0, weight=1)

    self.__thisTextArea.grig(sticky=N + E + S + W)

    # tired, happy new year \m/ d(-_-)b \m/ filthy animals
#test commit
#test