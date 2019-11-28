# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import StringVar

class CadastroGUI:
	def __init__(self, master, controller):
		self.controller = controller
		self.frame = tk.Frame(master, bg='white', relief=tk.SUNKEN)
		self.frame.pack()
		
		self.vPNome = StringVar()
		self.vSNome = StringVar()
		self.vEmail = StringVar()
		self.vSenha = StringVar()
		self.vSenhaC = StringVar()
		
		self.lPNome = tk.Label(self.frame, text="Primeiro Nome:", bg='white')
		self.ePNome = tk.Entry(self.frame, textvariable=self.vPNome)
		self.lSNome = tk.Label(self.frame, text="Segundo Nome:",bg='white')
		self.eSNome = tk.Entry(self.frame, textvariable=self.vSNome)
		self.lEmail = tk.Label(self.frame, text="Email:",bg='white')
		self.eEmail = tk.Entry(self.frame, textvariable=self.vEmail)
		self.lSenha = tk.Label(self.frame, text="Senha:",bg='white')
		self.eSenha = tk.Entry(self.frame, textvariable=self.vSenha)
		self.lSenhaC = tk.Label(self.frame, text="Senha de Confirmação:",bg='white')
		self.eSenhaC = tk.Entry(self.frame, textvariable=self.vSenhaC)
		
		self.lTitulo = tk.Label(self.frame, text="RRPG", font=("Arial",18), bg = 'white')
		self.lEspaco = tk.Label(self.frame, text="", bg = 'white')
		
		self.btnCadastrar = tk.Button(self.frame, text="Cadastrar",bg='#007FFF')
		
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
		
		self.btnCadastrar.bind("<Button>", lambda e: controller.cadastrar_usuario(self.vPNome.get(),self.vSNome.get(), self.vEmail.get(), self.vSenha.get(), self.vSenhaC.get()))
		
	def cadastrar_ok(self):
		messagebox.showinfo("Cadastrar", "Usuario cadastrado!")
			
	def cadastrar_erro(self):
		messagebox.showinfo("Cadastrar", "Usuario já cadastrado!")
		
class LoginGUI:
	def __init__(self, master, controller):
		self.controller = controller
		self.frame = tk.Frame(master, bg='white', relief=tk.SUNKEN)
		self.frame.pack()
		
		self.vEmail2 = StringVar()
		self.vSenha2 = StringVar()
		
		self.lEmail2 = tk.Label(self.frame, text="Email:",bg='white')
		self.eEmail2 = tk.Entry(self.frame, textvariable=self.vEmail2)
		self.lSenha2 = tk.Label(self.frame, text="Senha:",bg='white')
		self.eSenha2 = tk.Entry(self.frame, textvariable=self.vSenha2)
		
		self.lTitulo = tk.Label(self.frame, text="RRPG", font=("Arial",18), bg = 'white')
		self.lEspaco = tk.Label(self.frame, text="", bg = 'white')
		
		self.btnLogar = tk.Button(self.frame, text="Logar",bg='#007FFF')
		
		self.lTitulo.grid(row=1, column=0)
		self.lEspaco.grid(row=2, column=0)
		
		self.lEmail2.grid(row=4, column=0)
		self.eEmail2.grid(row=4, column=1)
		self.lSenha2.grid(row=5, column=0)
		self.eSenha2.grid(row=5, column=1)
		
		self.btnLogar.grid(row=6, column=1)
		
		self.btnLogar.bind("<Button>", lambda e: controller.logar_usuario(self.vEmail2.get(), self.vSenha2.get()))
		
	def logar_ok(self):
		messagebox.showinfo("Tela Inicial", "Usuario logado com sucesso!")
			
	def logar_erro(self):
		messagebox.showinfo("Tela Inicial", "Usuário/Senha inserida incorretamente!")
			
class FichaGUI:
	def __init__(self, master, controller):
		self.controller = controller
		self.frame = tk.Frame(master, bg='white', relief=tk.SUNKEN)
		self.frame.pack()
		
		self.vNome = StringVar()
		self.vRaca = StringVar()
		self.vClasse = StringVar()
		self.vNivel = IntVar()
		self.vVida = IntVar()
		self.vCA = IntVar()
		self.vDeslocamento = StringVar()
		self.vAntecedente = StringVar()
		self.vForca = IntVar()
		self.vDestreza = IntVar()
		self.vConstituicao = IntVar()
		self.vInteligencia= IntVar()
		self.vSabedoria = IntVar()
		self.vCarisma = IntVar()
		self.vEquipamento = StringVar()
		self.vAtaques = StringVar()
		self.vPericias = StringVar()
		self.vTestes = StringVar()
		self.vInfo = StringVar()
		
		self.lNome = tk.Label(self.frame, text="Nome:", bg='white')
		self.eNome = tk.Entry(self.frame, textvariable=self.vNome)
		self.lRaca = tk.Label(self.frame, text="Raça:", bg='white')
		self.eRaca = tk.Entry(self.frame, textvariable=self.vRaca)
		self.lClasse = tk.Label(self.frame, text="Classe:", bg='white')
		self.eClasse = tk.Entry(self.frame, textvariable=self.vClasse)
		self.lNivel = tk.Label(self.frame, text="Nível:", bg='white')
		self.eNivel = tk.Entry(self.frame, textvariable=self.vNivel)
		self.lVida = tk.Label(self.frame, text="Vida:", bg='white')
		self.eVida = tk.Entry(self.frame, textvariable=self.vVida)
		self.lCA = tk.Label(self.frame, text="CA:", bg='white')
		self.eCA = tk.Entry(self.frame, textvariable=self.vCA)
		self.lDeslocamento = tk.Label(self.frame, text="Deslocamento:", bg='white')
		self.eDeslocamento = tk.Entry(self.frame, textvariable=self.vDeslocamento)
		self.lAntecedente = tk.Label(self.frame, text="Antecedente:", bg='white')
		self.eAntecedente = tk.Entry(self.frame, textvariable=self.vAntecedente)
		self.lForca = tk.Label(self.frame, text="Força:", bg='white')
		self.eForca = tk.Entry(self.frame, textvariable=self.vForca)
		self.lDestreza = tk.Label(self.frame, text="Destreza:", bg='white')
		self.eDestreza = tk.Entry(self.frame, textvariable=self.vDestreza)
		self.lConstituicao = tk.Label(self.frame, text="Constituição:", bg='white')
		self.eConstituicao = tk.Entry(self.frame, textvariable=self.vConstituicao)
		self.lInteligencia = tk.Label(self.frame, text="Inteligência:", bg='white')
		self.eInteligencia = tk.Entry(self.frame, textvariable=self.vInteligencia)
		self.lSabedoria = tk.Label(self.frame, text="Sabedoria:", bg='white')
		self.eSabedoria = tk.Entry(self.frame, textvariable=self.vSabedoria)
		self.lCarisma = tk.Label(self.frame, text="Carisma:", bg='white')
		self.eCarisma = tk.Entry(self.frame, textvariable=self.vCarisma)
		
		
		self.lEquipamento = tk.Label(self.frame, text="Equipamento:", bg='white')
		self.eEquipamento = tk.Entry(self.frame, textvariable=self.vEquipamento)
		
		self.lInfo = tk.Label(self.frame, text="Informação do Personagem:", bg='white')
		self.eInfo = tk.Entry(self.frame, textvariable=self.vInfo)
		
		self.lAtaques = tk.Label(self.frame, text="Ataques:", bg='white')
		self.eAtaques = tk.Entry(self.frame, textvariable=self.vAtaques)
		
		self.lPericias = tk.Label(self.frame, text="Pericias:", bg='white')
		self.ePericias = tk.Entry(self.frame, textvariable=self.vPericias)
		
		self.lTestes = tk.Label(self.frame, text="Testes:", bg='white')
		self.eTestes = tk.Entry(self.frame, textvariable=self.vTestes)
		
		self.btnSalvar = tk.Button(self.frame, text="Salvar",bg='#007FFF')
		self.btnList = tk.Button(self.frame, text="Listar Fichas",bg='#007FFF')
		
		self.lNome.grid(row=1, column=11)
		self.eNome.grid(row=2, column=11)
		self.lRaca.grid(row=1, column=12)
		self.eRaca.grid(row=2, column=12)
		self.lClasse.grid(row=1, column=13)
		self.eClasse.grid(row=2, column=13)
		self.lNivel.grid(row=1, column=14)
		self.eNivel.grid(row=2, column=14)
		self.lVida.grid(row=3, column=11)
		self.eVida.grid(row=4, column=11)
		self.lCA.grid(row=3, column=12)
		self.eCA.grid(row=4, column=12)
		self.lDeslocamento.grid(row=3, column=13)
		self.eDeslocamento.grid(row=4, column=13)
		self.lAntecedente.grid(row=1, column=15)
		self.eAntecedente.grid(row=2, column=15)
		self.lForca.grid(row=5, column=11)
		self.eForca.grid(row=6, column=11)
		self.lDestreza.grid(row=7, column=11)
		self.eDestreza.grid(row=8, column=11)
		self.lConstituicao.grid(row=9, column=11)
		self.eConstituicao.grid(row=10, column=11)
		self.lInteligencia.grid(row=11, column=11)
		self.eInteligencia.grid(row=12, column=11)
		self.lSabedoria.grid(row=13, column=11)
		self.eSabedoria.grid(row=14, column=11)
		self.lCarisma.grid(row=15, column=11)
		self.eCarisma.grid(row=16, column=11)
		self.lEquipamento.grid(row=11, column=13)
		self.eEquipamento.grid(row=12, column=13)
		self.lInfo.grid(row=9, column=15)
		self.eInfo.grid(row=10, column=15)
		self.lAtaques.grid(row=9, column=13)
		self.eAtaques.grid(row=10, column=13)
		self.lPericias.grid(row=9, column=12)
		self.ePericias.grid(row=10, column=12)
		self.lTestes.grid(row=7, column=12)
		self.eTestes.grid(row=8, column=12)
		
		self.btnSalvar.grid(row=17, column=13)
		self.btnList.grid(row=17, column=14)
		
		self.btnSalvar.bind("<Button>", lambda e: controller.salvar_ficha(self.vNome.get(), self.vRaca.get(), self.vClasse.get(), self.vNivel.get(), self.vVida.get(), self.vCA.get(), self.vDeslocamento.get(), self.vAntecedente.get(), self.vForca.get(), self.vDestreza.get(), self.vConstituicao.get(), self.vInteligencia.get(), self.vSabedoria.get(), self.vCarisma.get(), self.vTestes.get(), self.vPericias.get(), self.vAtaques.get(),self.vEquipamento.get(), self.vInfo.get()));
		self.btnList.bind("<Button>", lambda e: controller.listar_fichas());
		
	def mostrar_sala(self, f, win):
		def fmostrar(e):
			self.vNome.set(f._Nome)
			self.vRaca.set(f._Raca)
			self.vClasse.set(f._Classe)
			self.vNivel.set(f._Nivel)
			self.vVida.set(f._Vida)
			self.vCA.set(f._CA)
			self.vDeslocamento.set(f._Deslocamento)
			self.vAntecedente.set(f._Antecedente)
			self.vForca.set(f._Forca)
			self.vDestreza.set(f._Destreza)
			self.vConstituicao.set(f._Constituicao)
			self.vInteligencia.set(f._Inteligencia)
			self.vSabedoria.set(f._Sabedoria)
			self.vCarisma.set(f._Carisma)
			self.vEquipamento.set(f._Equipamento)
			self.vAtaques.set(f._Ataques)
			self.vPericias.set(f._Pericias)
			self.vTestes.set(f._Testes)
			self.vInfo.set(f._InformacaoPersonagem)
			# Fechar a janela
			win.destroy()
		return fmostrar

	def listar(self, L):
		win = tk.Toplevel()
		win.wm_title("Lista de Fichas")
		
		tk.Label(win, text="Fichas",bg="black", fg="white", width=40).grid(row=0, column=2)
		i = 1
		for f in L:
			LNome = tk.Label(win, text=f._Nome, fg="#007FFF")
			LNome.bind("<Button>", self.mostrar_sala(f, win))
			LNome.grid(row=i, column=2)
			i += 1
		
	def salvar_ficha_ok(self):
		messagebox.showinfo("Ficha", "Ficha salva!")
		
	def salvar_ficha_erro(self):
		messagebox.showinfo("Ficha", "Erro ao salvar a ficha, tente novamente")
		
class TelaSalaGUI:
	def __init__(self, master, controller):
		self.controller = controller
		self.frame = tk.Frame(master, bg='white', relief=tk.SUNKEN)
		self.frame.pack()
		
		self.vNome = StringVar()
		
		self.lNome = tk.Label(self.frame, text="Nome:", bg='white')
		self.eNome = tk.Entry(self.frame, textvariable = self.vNome)

		self.btnCriar = tk.Button(self.frame, text="Criar Sala",bg='#007FFF')
		self.btnAbrir = tk.Button(self.frame, text="Abrir Sala",bg='#007FFF')
		self.btnList = tk.Button(self.frame, text="Listar Salas",bg='#007FFF')
		
		self.lNome.grid(row=1, column=2)
		self.eNome.grid(row=2, column=2)
		self.btnCriar.grid(row=3, column=2)
		self.btnAbrir.grid(row=4, column=2)
		self.btnList.grid(row=5, column=2)
		
		self.btnCriar.bind("<Button>", lambda e: controller.criar_sala(self.vNome.get()));
		self.btnAbrir.bind("<Button>", lambda e: controller.abrir_sala(self.vNome.get()));
		self.btnList.bind("<Button>", lambda e: controller.listar_salas());
		
		self.eNome.focus_set()
		
	def mostrar_sala(self, s, win):
		def fmostrar(e):
			self.vNome.set(s._Nome)
			# Fechar a janela
			win.destroy()
			self.eNome.focus_set()
		return fmostrar

	def listar(self, L):
		win = tk.Toplevel()
		win.wm_title("Lista de Salas")
		
		tk.Label(win, text="Nome",bg="black", fg="white", width=40).grid(row=0, column=2)
		i = 1
		for s in L:
			LNome = tk.Label(win, text=s._Nome, fg="#007FFF")
			LNome.bind("<Button>", self.mostrar_sala(s, win))
			LNome.grid(row=i, column=2)
			i += 1
			
	def criar_sala_ok(self):
		messagebox.showinfo("Sala", "Sala criada!")
		
	def criar_sala_erro(self):
		messagebox.showinfo("Sala", "Erro ao criar a sala, tente novamente")
		
	def abrir_sala_ok(self):
		messagebox.showinfo("Sala", "Sala aberta!")
		
	def abrir_sala_erro(self):
		messagebox.showinfo("Sala", "Erro ao abrir a sala, tente novamente")
		
class SalaGUI:
	def __init__(self, master, controller):
		self.controller = controller
		self.frame = tk.Frame(master, bg='white', relief=tk.SUNKEN)
		self.frame.pack()
		
		self.btnCriar = tk.Button(self.frame, text="Ficha", bg='#007FFF')
		self.btnUpload = tk.Button(self.frame, text="Upload", bg='#007FFF')
		self.btnSair = tk.Button(self.frame, text="Sair", bg='#007FFF')
		
		self.btnCriar.grid(row=1, column=10)
		self.btnUpload.grid(row=1, column=11)
		self.btnSair.grid(row=1, column=12)
		
		self.L= Label(self.frame, bg="gray", text="Chat Teste", width=34, height=34)
		self.L.grid(row=3, columnspan=14)
		
		self.btnCriar.bind("<Button>", lambda e: controller.abrir_ficha());
		self.btnUpload.bind("<Button>", lambda e: controller.upload_mapa());
		self.btnSair.bind("<Button>", lambda e: controller.sair_sala());
			
	def tela_do_chat():
		pass
			
	def abrir_ficha_ok(self):
		messagebox.showinfo("Ficha", "Ficha aberta!")
		
	def abrir_ficha_erro(self):
		messagebox.showinfo("Ficha", "Erro ao abrir a ficha, tente novamente")
