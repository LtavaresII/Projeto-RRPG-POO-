# -*- coding: utf-8 -*-

import socket
import sys
from tinydb import TinyDB, Query
import json
import tkinter as tk
from tkinter import *
from RRPGModel import ErroSenhaUsuarioIncorreto, ErroComandoInvalido, ErroOpcaoNaoValida, ErroCriacaoUsuario, ErroCriarFicha, ErroCriacaodeSala, Usuario, Ficha, Sala, RolagemdeDados
from RRPGView import CadastroGUI, FichaGUI, SalaGUI, TelaSalaGUI, LoginGUI

class ControllerC:
	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry('600x400+100+100')
		self.root.title('Cadastrar')
		self.root.configure(bg = '#ffffff')
		
		self.view = CadastroGUI(self.root, self)
		
		self.root.mainloop()
		
	def cadastrar_usuario(self, pnome, snome, email, senha, senhac):
		
		try:
			U = Usuario(pnome, snome, email, senha, senhac)
			Usuario.Cadastrar(U)
			self.view.cadastrar_ok()
			CL = ControlerL()
		except ErroCriacaoUsuario:
			self.view.cadastrar_erro()
			
class ControllerL:
	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry('600x400+100+100')
		self.root.title('Tela Inicial')
		self.root.configure(bg = '#ffffff')
		
		self.view = LoginGUI(self.root, self)
		
		self.root.mainloop()
			
	def logar_usuario(self, email, senha):
		try:
			resposta = Usuario.Logar(email, senha)
			if resposta is True:
				self.view.logar_ok()
				CTS = ControllerTS()
			else:
				self.view.logar_erro()
		except ErroSenhaUsuarioIncorreto:
			self.view.logar_erro()
	
			
class ControllerF:
	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry('850x350+100+100')
		self.root.title('Ficha')
		self.root.configure(bg = '#ffffff')
		
		self.view = FichaGUI(self.root, self)
		
		self.root.mainloop()
		
	def salvar_ficha(self, nome, raca, classe, nivel, vida, ca, deslc, antec, forc, dex, cons, intl, sab, car, equip, info, ataq, peri, test):
		
		try:
			F = Ficha(nome, raca, classe, nivel, vida, ca, deslc, antec, forc, dex, cons, intl, sab, car, equip, info, ataq, peri, test)
			Ficha.Criar(F)
			self.view.salvar_ficha_ok()
		except ErroCriarFicha:
			self.view.salvar_ficha_erro()
			
	def listar_fichas(self):
		self.view.listar(Ficha.listar())
			
class ControllerTS:
	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry('400x200+100+100')
		self.root.title("Tela de sala")
		self.root.configure(bg = '#ffffff')
		
		self.view = TelaSalaGUI(self.root, self)
		
		self.root.mainloop()
		
	def criar_sala(self, nome):
		try:
			if nome !="":
				S = Sala(nome)
				Sala.Criar(S)
				self.view.criar_sala_ok()
			else:
				self.view.criar_sala_erro()
		except ErroCriacaodeSala:
			self.view.criar_sala_erro()
			
	def listar_salas(self):
		self.view.listar(Sala.listar())
		
	def abrir_sala(self, nome):
		try:
			L = Sala.Abrir(nome)
			if nome !="":
				self.view.abrir_sala_ok()
				for s in L:
					CS = ControllerS(s._Nome)
			else:
				self.view.abrir_sala_erro()
		except ErroOpcaoNaoValida:
			self.view.abrir_sala_erro()
        
class ControllerS:
	def __init__(self, nome, *args, **kwargs):
		self.root = tk.Tk()
		self.root.geometry('900x520+100+100')
		self.root.title(nome)
		self.root.configure(bg = '#ffffff')
		
		#criar plano de fundo
		self.canvas = tk.Canvas(self.root, width=600, height=520,bg = '#ffffff' )
		self.canvas.pack()
		
		#linhas da vertical
		self.canvas.create_line(0, 0, 600, 0, fill = 'black')
		self.canvas.create_line(0, 40, 600, 40, fill = 'black')
		self.canvas.create_line(0, 80, 600, 80, fill = 'black')
		self.canvas.create_line(0, 120, 600, 120, fill = 'black')
		self.canvas.create_line(0, 160, 600, 160, fill = 'black')
		self.canvas.create_line(0, 200, 600, 200, fill = 'black')
		self.canvas.create_line(0, 240, 600, 240, fill = 'black')
		self.canvas.create_line(0, 280, 600, 280, fill = 'black')
		self.canvas.create_line(0, 320, 600, 320, fill = 'black')
		self.canvas.create_line(0, 360, 600, 360, fill = 'black')
		self.canvas.create_line(0, 400, 600, 400, fill = 'black')
		self.canvas.create_line(0, 440, 600, 440, fill = 'black')
		self.canvas.create_line(0, 480, 600, 480, fill = 'black')
		self.canvas.create_line(0, 520, 600, 520, fill = 'black')
		
		#linhas da horizontal
		self.canvas.create_line(0, 0, 0, 520, fill = 'black')
		self.canvas.create_line(40, 0, 40, 520, fill = 'black')
		self.canvas.create_line(80, 0, 80, 520, fill = 'black')
		self.canvas.create_line(120, 0, 120, 520, fill = 'black')
		self.canvas.create_line(160, 0, 160, 520, fill = 'black')
		self.canvas.create_line(200, 0, 200, 520, fill = 'black')
		self.canvas.create_line(240, 0, 240, 520, fill = 'black')
		self.canvas.create_line(280, 0, 280, 520, fill = 'black')
		self.canvas.create_line(320, 0, 320, 520, fill = 'black')
		self.canvas.create_line(360, 0, 360, 520, fill = 'black')
		self.canvas.create_line(400, 0, 400, 520, fill = 'black')
		self.canvas.create_line(440, 0, 440, 520, fill = 'black')
		self.canvas.create_line(480, 0, 480, 520, fill = 'black')
		self.canvas.create_line(520, 0, 520, 520, fill = 'black')
		self.canvas.create_line(560, 0, 560, 520, fill = 'black')
		self.canvas.create_line(600, 0, 600, 520, fill = 'black')
		
		self.canvas.pack(side=tk.LEFT)
		
		# this data is used to keep track of an 
		# item being dragged
		self._drag_data = {"x": 0, "y": 0, "item": None, "Sala" : nome}
		
		P = Sala.AbrirPosicao(nome)
		
		# create a couple movable objects
		self._create_token((100,100), "black")
		
		# add bindings for clicking, dragging and releasing over
		# any object with the "token" tag
		self.canvas.tag_bind("token", "<ButtonPress-1>", self.OnTokenButtonPress)
		self.canvas.tag_bind("token", "<ButtonRelease-1>", self.OnTokenButtonRelease)
		self.canvas.tag_bind("token", "<B1-Motion>", self.OnTokenMotion)
		
		self.view = SalaGUI(self.root, self)
		
		self.root.mainloop()
		
	def _create_token(self, coord, color):
		'''Create a token at the given coordinate in the given color'''
		(x,y) = coord
		self.canvas.create_oval(x-20, y-20, x+20, y+20, outline=color, fill=color, tags="token")
                                
	def OnTokenButtonPress(self, event):
		'''Being drag of an object'''
		# record the item and its location
		self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
		self._drag_data["x"] = event.x
		self._drag_data["y"] = event.y
		
	def OnTokenButtonRelease(self, event):
		'''End drag of an object'''
		# reset the drag information
		self._drag_data["item"] = None
		self._drag_data["x"] = 0
		self._drag_data["y"] = 0
		
	def OnTokenMotion(self, event):
		p = []
		'''Handle dragging of an object'''
		# compute how much this object has moved
		delta_x = event.x - self._drag_data["x"]
		delta_y = event.y - self._drag_data["y"]
		# move the object the appropriate amount
		self.canvas.move(self._drag_data["item"], delta_x, delta_y)
		# record the new position
		self._drag_data["x"] = event.x
		self._drag_data["y"] = event.y
		
		sala = self._drag_data["Sala"]
		p = [event.x , event.y]
		Sala.AdicionarPosicao(p, sala)

	def adicionar_usuarios(self):
		pass

	def abrir_ficha(self, nome):
		CF = ControllerF(nome)
   
	def upload_mapa():
		pass
		
	def sair_sala():
		pass
		
