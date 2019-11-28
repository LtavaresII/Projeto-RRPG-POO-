# -*- coding: utf-8 -*-

import socket
import sys
from tinydb import TinyDB, Query
import random
import threading
import time
import _thread
import pickle
import select
import json

class MyEncoder(json.JSONEncoder):
	def default(self, o):
		d = vars(o) 
		d['tipo'] = o.__class__.__name__  
		return d
		
	@staticmethod
	def decode(d):
		if d['tipo'] == 'Usuario':
			return Usuario(d['_PNome'],d['_SNome'],d['_Email'],d['_Senha'],d['_SenhaC'])
		if d['tipo'] == 'Ficha':
			return Ficha(d['_Nome'],d['_Raca'],d['_Classe'],d['_Nivel'],d['_Vida'],d['_CA'],d['_Deslocamento'],d['_Antecedente'],d['_Forca'],d['_Destreza'],d['_Constituicao'],d['_Inteligencia'],d['_Sabedoria'],d['_Carisma'],d['_Equipamento'],d['_Ataques'],d['_Pericias'],d['_Testes'],f['_InformacaoPersonagem'])
		if d['tipo'] == 'Sala':
			return Sala(d['_Nome'],d['_Usuarios'],d['_PosicaoP'],d['_Fichas'],d['_Chat'])
					
class ErroChat(Exception):
	def __init__(self):
		super().__init__("Erro no Chat")
	
class ErroSenhaUsuarioIncorreto(Exception):
	def __init__(self):
		super().__init__("Usuário/Senha inserida incorretamente")
	
class ErroNomeIncorreto(Exception):
	def __init__(self):
		super().__init__("Nome inserido incorreto")
	
class ErroCriarFicha(Exception):
	def __init__(self):
		super().__init__("Erro ao criar a ficha")
	
class ErroComandoInvalido(Exception):
	def __init__(self):
		super().__init__("Comando invalido")
	
class ErroInteracao(Exception):
	def __init__(self):
		super().__init__("Erro de interação")
	
class ErroOpcaoNaoValida(Exception):
	def __init__(self):
		super().__init__("Opção não valida")
	
class ErroCriacaoUsuario(Exception):
	def __init__(self):
		super().__init__("Usuario já existe")
		
class ErroCriacaodeSala(Exception):
	def __init__(self):
		super().__init__("Entrada incorreta, preencha os campos novamente")
	

class Usuario:
	def __init__(self, pnome, snome, email, senha, senhac):
		
		self._PNome = pnome
		self._SNome = snome
		self._Email = email
		self._Senha = senha
		self._SenhaC = senhac

	@staticmethod
	def Cadastrar(U):
		l = [U]
		with  TinyDB('Usuarios.json') as db:
			for x in l:
				db.insert(x.toDict())
				
	@staticmethod
	def Logar(email, senha):
		with  TinyDB('Usuarios.json') as db:
			Q = Query()
			l = db.search(Q._Senha == senha)
			for x in l:
				u = Usuario.fromDict(x)
				if u._Email == email:
					return True 
				else:
					return False
					
	def toDict(self):
		s = json.dumps(self, cls=MyEncoder)
		return json.loads(s)
		
	@staticmethod
	def fromDict(d):
		s = json.dumps(d)
		return json.loads(s, object_hook=MyEncoder.decode)
		
	@property
	def PNome(self):
		return self._PNome
			
	@property
	def SNome(self):
		return self._SNome
		
	@property
	def Email(self):
		return self._Email
		
	@property
	def Senha(self):
		return self._Senha
		
	@property
	def SenhaConfirmacao(self):
		return self._SenhaC

class Ficha:
	
	def __init__(self, nome, raca, classe, nivel, vida, ca, deslc, antec, forc, dex, cons, intl, sab, car, equip, ataq, peri, test, info):
		self._Nome = nome
		self._Raca = raca
		self._Classe = classe
		self._Nivel = nivel
		self._Vida = vida
		self._CA = ca
		self._Deslocamento = deslc
		self._Antecedente = antec
		self._Forca = forc
		self._Destreza = dex
		self._Constituicao = cons
		self._Inteligencia = intl
		self._Sabedoria = sab
		self._Carisma = car
		self._Equipamento = equip
		self._Ataques = ataq
		self._Pericias = peri
		self._Testes = test
		self._InformacaoPersonagem = info
		
	@staticmethod
	def Criar(F):
		l = [F]
		with  TinyDB('Fichas.json') as db:
			for x in l:
				db.insert(x.toDict())
				
	@staticmethod
	def listar():
		L = []
		with TinyDB('Fichas.json') as db:
			for f in db:
				L.append(Ficha(f['_Nome'],f['_Raca'],f['_Classe'],f['_Nivel'],f['_Vida'],f['_CA'],f['_Deslocamento'],f['_Antecedente'],f['_Forca'],f['_Destreza'],f['_Constituicao'],f['_Inteligencia'],f['_Sabedoria'],f['_Carisma'],f['_Equipamento'],f['_Ataques'],f['_Pericias'],f['_Testes'],f['_InformacaoPersonagem']))
		return L
		
	def toDict(self):
		s = json.dumps(self, cls=MyEncoder)
		return json.loads(s)
        
	@staticmethod
	def fromDict(d):
		s = json.dumps(d)
		return json.loads(s, object_hook=MyEncoder.decode)
		
	@property
	def Nome(self):
		return self._Nome
		
	@property
	def Raca(self):
		return self._Raca
		
	@property
	def Classe(self):
		return self._Classe
		
	@property
	def Nivel(self):
		return self._Nivel
		
	@property
	def Vida(self):
		return self._Vida
		
	@property
	def CA(self):
		return self._CA
		
	@property
	def Deslocamento(self):
		return self._Deslocamento
		
	@property
	def Antecedente(self):
		return self._Antecedente 
		
	@property
	def Forca(self):
		return self._Forca
		
	@property
	def Destreza(self):
		return self._Destreza
		
	@property
	def Constituicao(self):
		return self._Constituicao
		
	@property
	def Inteligencia(self):
		return self._Inteligencia
		
	@property
	def Sabedoria(self):
		return self._Sabedoria
		
	@property
	def Carisma(self):
		return self._Carisma
		
	@property
	def Equipamento(self):
		return self._Equipamento
		
	@property
	def InformacaoPersonagem(self):
		return self._InformacaoPersonagem
		
	@property
	def Ataque(self):
		return self._Ataques
		
	@property
	def Pericia(self):
		return self._Pericias
		
	@property
	def Teste(self):
		return self._Testes
		
class RolagemdeDados:
	def __init__(self):
		pass
		
	@staticmethod
	def RolarDados(ND, DPR):
		soma = 0
		i = 0
		dado = []
		if ND > 0 and (DPR == 4 or DPR == 6 or DPR == 8 or DPR == 10 or DPR ==12 or DPR ==20):
				
			for x in range(ND):
				
				dado.append(random.randint(1,DPR))
				soma = soma+dado[i] 
				i = i+1
			return dado, soma
		else:
			raise ErroComandoInvalido('Nao existe esse dados')
			
	@staticmethod
	def fromDict(d):
		s = json.dumps(d)
		return json.loads(s, object_hook = MyEncoder.decode)

class Sala:
	def __init__(self, nome):
		self._Nome = nome
		self._Usuarios = []
		self._PosicaoP = []
		self._Fichas = []
		self._Chat = []
	
	@staticmethod
	def Criar(S):
		if S._Nome !="":
			with TinyDB('Salas.json') as db:
				l = [S]
				for x in l:
					db.insert(x.toDict())		
	@staticmethod
	def listar():
		L = []
		with TinyDB('Salas.json') as db:
			for s in db:
				L.append(Sala(s['_Nome']))
		return L
		
	@staticmethod
	def Abrir(nome):
		L = []
		with  TinyDB('Salas.json') as db:
			Q = Query()
			l = db.search(Q._Nome == nome)
			for x in l:
				L.append(Sala(x['_Nome']))
		return L
	
	def __repr__(self):
		return 'Sala({0})'.format(self._Nome)
		
	def toDict(self):
		s = json.dumps(self, cls=MyEncoder)
		return json.loads(s)
		
	@staticmethod
	def fromDict(d):
		s = json.dumps(d)
		return json.loads(s, object_hook=MyEncoder.decode)
        
	@property
	def Nome(self):
		return self._Nome
				
	@staticmethod
	def AdicionarPosicao(p, nome):
		with TinyDB('Salas.json') as db:
			Q = Query()
			l = db.update({'_PosicaoP': p }, Q._Nome == nome)
			for x in l:
				db.insert(x.toDict())
	
	@staticmethod
	def AbrirPosicao(nome):
		L = []
		with TinyDB('Salas.json') as db:
			Q = Query()
			l = db.search(Q._Nome == nome)
			for x in l:
				L.append(Sala(x['_PosicaoP']))
		return L
		
	@staticmethod
	def AdicionarUsuarios():
		pass
			
	@staticmethod
	def AdicionarFichas():
		pass
			
