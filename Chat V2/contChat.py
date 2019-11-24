# -*- coding: utf-8 -*-

import socket
import sys
from tinydb import TinyDB, Query
import json
import tkinter as tk
import s
import chatView

class Controller:
	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry('600x400+100+100')
		self.root.title('Usuario')
		
		self.view = UsuarioGUI(self.root, self)
		
		self.root.mainloop()

    def enviar(self,msg):
        self.view.novaMsg(msg)
