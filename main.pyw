"""
this is same code as main.py,but you cant accses this with vscode and only python ide.
I did this so people wouldnt look at the code, if they dont know how to accses pyhton's main ide.
"""




from logging import root
import os
import time
from tkinter import Tk
from tkinter import *
import tkinter as tk
import webbrowser
import pyautogui


def create_window():
     root = Tk()

root = Tk()
root.minsize(300,300)
root.title("idk")
root.config(bg='#AFB6FF')



def test():
    time.sleep (2)
    os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
    time.sleep (2)
    pyautogui.keyDown("r")
    pyautogui.keyDown("i")
    pyautogui.keyDown("c")
    pyautogui.keyDown("k")
    pyautogui.keyDown("space")
    pyautogui.keyDown("r")
    pyautogui.keyDown("o")
    pyautogui.keyDown("l")
    pyautogui.keyDown("l")
    pyautogui.keyDown("enter")
    time.sleep (1)
    pyautogui.keyDown("enter")
    pyautogui.keyDown("tab")
    pyautogui.keyDown("tab")
    pyautogui.keyDown("tab")
    pyautogui.keyDown("enter")


def hello():
    time.sleep (10)
    os.system ('rundll32.exe powrprof.dll, SetSuspendState Sleep')



def play():
    os.system("Spotify")
    time.sleep (4)
    pyautogui.keyDown("space")
    pyautogui.keyUp("space")


def light():
    
 get_url= webbrowser.open('https://i.redd.it/76si7e78lwb61.jpg')

 
Button(root,text="create new window", command=create_window).pack()
Button(root,text="test", command=test).pack()
Button(root,text="light", command=light).pack()
Button(root,text="hello",command=hello).pack()
Button(root,text="play", command=play).pack()




root.mainloop()
