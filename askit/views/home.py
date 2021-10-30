import tkinter as tk

# UTILS
from utils import LARGEFONT

# PAGES
from . import login, register
from tkinter import ttk


class Home(tk.Frame):
  def __init__(self, parent, controller):
      tk.Frame.__init__(self, parent)
        
      # label of frame Layout 2
      label = ttk.Label(self, text ="Startpage", font = LARGEFONT)
        
      # putting the grid in its place by using
      # grid
      label.grid(row = 0, column = 4, padx = 10, pady = 10)

      button1 = ttk.Button(self, text ="Register",
      command = lambda : controller.show_frame(register.Register))
    
      # putting the button in its place by
      # using grid
      button1.grid(row = 1, column = 1, padx = 10, pady = 10)

      ## button to show frame 2 with text layout2
      button2 = ttk.Button(self, text ="Login",
      command = lambda : controller.show_frame(login.Login))
    
      # putting the button in its place by
      # using grid
      button2.grid(row = 2, column = 1, padx = 10, pady = 10)