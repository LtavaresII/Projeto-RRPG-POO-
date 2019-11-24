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
			
class FichaGUI:
	def __init__(self, master, controller):
		self.controller = controller
		self.frame = tk.Frame(master)
		self.frame.pack()
		
		self.vNome = StringVar()
		self.vRaca = StringVar()
		self.vClasse = StringVar()
		self.vNivel = StringVar()
		self.vVida = StringVar()
		self.vCA = StringVar()
		self.vDeslocamento = StringVar()
		self.vAntecedente = StringVar()
		self.vForca = StringVar()
		self.vDestreza = StringVar()
		self.vConstituicao = StringVar()
		self.vInteligencia= StringVar()
		self.vSabedoria = StringVar()
		self.vCarisma = StringVar()
		self.vEquipamento = StringVar()
		self.vText = StringVar()
		self.vAtaques = StringVar()
		self.vPericias = StringVar()
		self.vTestes = StringVar()
		
		self.lNome = tk.Label(self.frame, text="Nome:")
		self.eNome = tk.Entry(self.frame, textvariable=self.vNome)
		self.lRaca = tk.Label(self.frame, text="Raça:")
		self.eRaca = tk.Entry(self.frame, textvariable=self.vRaca)
		self.lClasse = tk.Label(self.frame, text="Classe:")
		self.eClasse = tk.Entry(self.frame, textvariable=self.vClasse)
		self.lNivel = tk.Label(self.frame, text="Nível:")
		self.eNivel = tk.Entry(self.frame, textvariable=self.vNivel)
		self.lCA = tk.Label(self.frame, text="CA:")
		self.eCA = tk.Entry(self.frame, textvariable=self.vCA)
		self.lDeslocamento = tk.Label(self.frame, text="Deslocamento:")
		self.eDeslocamento = tk.Entry(self.frame, textvariable=self.vDeslocamento)
		self.lAntecedente = tk.Label(self.frame, text="Antecedente:")
		self.eAntecedente = tk.Entry(self.frame, textvariable=self.vAntecedente)
		self.lForca = tk.Label(self.frame, text="Força:")
		self.eForca = tk.Entry(self.frame, textvariable=self.vForca)
		self.lDestreza = tk.Label(self.frame, text="Destreza:")
		self.eDestreza = tk.Entry(self.frame, textvariable=self.vDestreza)
		self.lConstituicao = tk.Label(self.frame, text="Constituição:")
		self.eConstituicao = tk.Entry(self.frame, textvariable=self.vConstituicao)
		self.lInteligencia = tk.Label(self.frame, text="Inteligência:")
		self.eInteligencia = tk.Entry(self.frame, textvariable=self.vInteligencia)
		self.lSabedoria = tk.Label(self.frame, text="Sabedoria:")
		self.eSabedoria = tk.Entry(self.frame, textvariable=self.vSabedoria)
		self.lCarisma = tk.Label(self.frame, text="Carisma:")
		self.eCarisma = tk.Entry(self.frame, textvariable=self.vCarisma)
		self.lEquipamento = tk.Label(self.frame, text="Equipamento:")
		self.eEquipamento = tk.Entry(self.frame, textvariable=self.vEquipamento)
		self.lText = tk.Label(self.frame, text="Informação do Personagem:")
		self.eText = tk.Entry(self.frame, textvariable=self.vText)
		self.lAtaques = tk.Label(self.frame, text="Ataques:")
		self.eAtaques = tk.Entry(self.frame, textvariable=self.vAtaques)
		self.lPericias = tk.Label(self.frame, text="Pericias:")
		self.ePericias = tk.Entry(self.frame, textvariable=self.vPericias)
		self.lTestes = tk.Label(self.frame, text="Testes:")
		self.eTestes = tk.Entry(self.frame, textvariable=self.vTestes)
		
		self.btnCriar = tk.Button(self.frame, text="Criar")
		self.btnAbrir = tk.Button(self.frame, text="Abrir")
		
		self.lNome.grid()
		self.eNome.grid()
		self.lRaca.grid()
		self.eRaca.grid()
		self.lClasse.grid()
		self.eClasse.grid()
		self.lNivel.grid()
		self.eNivel.grid()
		self.lVida.grid()
		self.eVida.grid()
		self.lCA.grid()
		self.eCA.grid()
		self.lDeslocamento.grid()
		self.eDeslocamento.grid()
		self.lAntecedente.grid()
		self.eAntecedente.grid()
		self.lForca.grid()
		self.eForca.grid()
		self.lDestreza.grid()
		self.eDestreza.grid()
		self.lConstituicao.grid()
		self.eConstituicao.grid()
		self.lInteligencia.grid()
		self.eInteligencia.grid()
		self.lSabedoria.grid()
		self.eSabedoria.grid()
		self.lCarisma.grid()
		self.eCarisma.grid()
		self.lEquipamento.grid()
		self.eEquipamento.grid()
		self.lText.grid()
		self.eText.grid()
		self.lAtaques.grid()
		self.eAtaques.grid()
		self.lPericias.grid()
		self.ePericias.grid()
		self.lTestes.grid()
		self.eTestes.grid()
		
		self.btnCriar.bind("<Button>", lambda e: controller.criar_ficha(self.vNome.get(), self.vRaca.get(), self.vClasse.get(), self.vNivel.get(), self.vVida.get(), self.vCA.get(), self.vDeslocamento.get(), self.vAntecedente.get(), self.vForca.get(), self.vDestreza.get(), self.vConstituicao.get(), self.vInteligencia.get(), self.vSabedoria.get(), self.vCarisma.get(), self.vEquipamento.get(), self.vText.get(), self.vAtaques.get(), self.vPericias.get(), self.vTestes.get()));
		self.btnAbrir.bind("<Button>", lambda e: controller.abrir_ficha());
		
	def criar_ficha_ok(self):
		messagebox.showinfo("Ficha", "Ficha criada!")
		
	def criar_ficha_erro(self):
		messagebox.showinfo("Ficha", "Erro ao criar a ficha, tente novamente")
		
	def abrir_ficha_ok(self):
		messagebox.showinfo("Ficha", "Ficha aberta!")
		
	def abrir_ficha_erro(self):
		messagebox.showinfo("Ficha", "Erro ao abrir a ficha, tente novamente")
	
class MapaGUI:
	def __init__(self, master, controller):
		self.controller = controller
		self.frame = tk.Frame(master)
		self.frame.pack()

class SalaGUI:
	def __init__(self, master, controller):
		self.controller = controller
		self.frame = tk.Frame(master)
		self.frame.pack()
		
	def criar_sala_ok(self):
		messagebox.showinfo("Sala", "Sala criada!")
		
	def criar_sala_erro(self):
		messagebox.showinfo("Sala", "Erro ao criar a sala, tente novamente")
		
	def abrir_sala_ok(self):
		messagebox.showinfo("Sala", "Sala aberta!")
		
	def abrir_sala_erro(self):
		messagebox.showinfo("Sala", "Erro ao abrir a sala, tente novamente")
