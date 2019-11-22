# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar

class UsuarioGUI:
	def __init__(self, master, controller):
		self.controller = controller
		self.frame = tk.Frame(master)
		self.frame.pack()
		
		self.vPNome = StringVar()
		self.vSNome = StringVar()
		self.vEmail = StringVar()
		self.vSenha = StringVar()
		self.vSenhaC = StringVar()
		
		self.vEmail2 = StringVar()
		self.vSenha2 = StringVar()
		
		self.lPNome = tk.Label(self.frame, text="Primeiro Nome:")
		self.ePNome = tk.Entry(self.frame, textvariable=self.vPNome)
		self.lSNome = tk.Label(self.frame, text="Segundo Nome:")
		self.eSNome = tk.Entry(self.frame, textvariable=self.vSNome)
		self.lEmail = tk.Label(self.frame, text="Email:")
		self.eEmail = tk.Entry(self.frame, textvariable=self.vEmail)
		self.lSenha = tk.Label(self.frame, text="Senha:")
		self.eSenha = tk.Entry(self.frame, textvariable=self.vSenha)
		self.lSenhaC = tk.Label(self.frame, text="Senha de Confirmação:")
		self.eSenhaC = tk.Entry(self.frame, textvariable=self.vSenhaC)
		
		self.lTitulo = tk.Label(self.frame, text="RRPG", font=("Arial",18))
		self.lEspaco = tk.Label(self.frame, text="")
		
		self.btnCadastrar = tk.Button(self.frame, text="Cadastrar")
		
		self.lEmail2 = tk.Label(self.frame, text="Email:")
		self.eEmail2 = tk.Entry(self.frame, textvariable=self.vEmail2)
		self.lSenha2 = tk.Label(self.frame, text="Senha:")
		self.eSenha2 = tk.Entry(self.frame, textvariable=self.vSenha2)
		
		self.btnLogar = tk.Button(self.frame, text="Logar")
		
		self.lTitulo.grid(row=1, column=0)
		self.lEspaco.grid(row=2, column=0)
		
		self.lPNome.grid(row=4, column=0)
		self.ePNome.grid(row=4, column=1)
		self.lSNome.grid(row=5, column=0)
		self.eSNome.grid(row=5, column=1)
		self.lEmail.grid(row=6, column=0)
		self.eEmail.grid(row=6, column=1)
		self.lSenha.grid(row=7, column=0)
		self.eSenha.grid(row=7, column=1)
		self.lSenhaC.grid(row=8, column=0)
		self.eSenhaC.grid(row=8, column=1)
		
		self.btnCadastrar.grid(row=10, column=1)
		
		self.lEmail2.grid(row=4, column=10)
		self.eEmail2.grid(row=4, column=11)
		self.lSenha2.grid(row=5, column=10)
		self.eSenha2.grid(row=5, column=11)
		
		self.btnLogar.grid(row=6, column=11)
		
		self.btnCadastrar.bind("<Button>", lambda e: controller.cadastrar_usuario(self.vPNome.get(),self.vSNome.get(), self.vEmail.get(), self.vSenha.get(), self.vSenhaC.get()));
		self.btnLogar.bind("<Button>", lambda e: controller.logar_usuario(self.vEmail2.get(), self.vSenha2.get()));
		
	def cadastrar_ok(self):
		messagebox.showinfo("Tela Inicial", "Usuario cadastrado!")
			
	def cadastrar_erro(self):
		messagebox.showinfo("Tela Inicial", "Usuario já cadastrado!")
			
	def logar_ok(self):
		messagebox.showinfo("Tela Inicial", "Usuario logado com sucesso!")
			
	def logar_erro(self):
		messagebox.showinfo("Tela Inicial", "Usuário/Senha inserida incorretamente!")
