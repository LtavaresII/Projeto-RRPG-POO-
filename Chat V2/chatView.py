# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar

class UsuarioGUI:
    _msg1 = [] #lista de mensagns
    _c = [] #lista de mensagens que irao aparecer na tela
	def __init__(self, master, controller):
		self.controller = controller
		self.frame = tk.Frame(master)
		self.frame.pack()
       

    def novaMsg(msg):
        _msg1.append(msg)
        _c.append(1)#criar um espaço no vetor de Label

    for i in range(self.msg1):
        _c[i] = tk.Label(self.frame, text = _msg1[i])