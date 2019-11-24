# -*- coding: utf-8 -*-

import socket
import sys
from tinydb import TinyDB, Query
import json
import tkinter as tk
from RRPGModel import ErroSenhaUsuarioIncorreto, ErroComandoInvalido, ErroOpcaoNaoValida, ErroCriacaoUsuario, ErroCriarFicha, Usuario, Ficha
from RRPGView import UsuarioGUI, FichaGUI, SalaGUI, MapaGUI

class ControllerU:
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
			
class ControllerF:
	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry('600x400+100+100')
		self.root.title('Ficha')
		
		self.view = FichaGUI(self.root, self)
		
		self.root.mainloop()
		
	def criar_ficha(self, nome, raca, classe, nivel, vida, ca, deslc, antec, forc, dex, cons, intl, sab, car, equip, info, ataq, peri, test):
		
		F = Ficha(nome, raca, classe, nivel, vida, ca, deslc, antec, forc, dex, cons, intl, sab, car, equip, info, ataq, peri, test)
		
		try:
			Ficha.Criar(F)
			self.view.criar_ficha_ok()
		except ErroCriarFicha:
			self.view.criar_ficha_erro()
		
	def abrir_ficha(self):
		try:
			Ficha.Abrir()
			self.view.abrir_ficha_ok()
		except ErroCriarFicha:
			self.view.abrir_ficha_erro()
		
class ControllerS:
	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry('600x400+100+100')
		self.root.title('Sala')
		
		self.view = SalaGUI(self.root, self)
		
		self.root.mainloop()
		
	def criar_sala():
		
	def abrir_sala():
		
class ControllerM:
	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry('600x400+100+100')
		self.root.title('Mapa')
		
		self.view = MapaGUI(self.root, self)
		
		self.root.mainloop()
		
	def upload_mapa():
		
	def abrir_mapa():
