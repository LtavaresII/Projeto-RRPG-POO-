# -*- coding: utf-8 -*-

import socket
import sys
from tinydb import TinyDB, Query
import json
import tkinter as tk
from RRPGModel import ErroSenhaUsuarioIncorreto, ErroComandoInvalido, ErroOpcaoNaoValida, ErroCriacaoUsuario, Usuario
from RRPGView import UsuarioGUI

class Controller:
	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry('600x400+100+100')
		self.root.title('Tela Inicial')
		
		self.view = UsuarioGUI(self.root, self)
		
		self.root.mainloop()
		
	def cadastrar_usuario(self, pnome, snome, email, senha, senhac):
		
		U = Usuario(pnome, snome, email, senha, senhac)
		
		try:
			Usuario.Cadastrar(U)
			self.view.cadastrar_ok()
		except ErroCriacaoUsuario:
			self.view.cadastrar_erro()
		
	def logar_usuario(self, email, senha):
		try:
			Usuario.Logar(email, senha)
			self.view.logar_ok()
		except ErroSenhaUsuarioIncorreto:
			self.view.logar_erro()
		
		
