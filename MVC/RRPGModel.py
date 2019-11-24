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
			return Usuario(d['PNome'],d['SNome'],d['Email'],d['Senha'],d['SenhaC'],d['Nick'],d['Acesso'])
		if d['tipo'] == 'Email':
			return Email(d['Email'])
		if d['tipo'] == 'Senha':
			return Senha(d['Senha'])
		if d['tipo'] == 'Ficha':
			return Ficha(d['Nome'],d['Raca'],d['Classe'],d['Nivel'],d['Vida'],d['CA'],d['Deslocamento'],d['Antecedente'],d['Forca'],d['Destreza'],d['Constituicao'],d['Inteligencia'],d['Sabedoria'],d['__Carisma'],d['__Equipamento'],d['Ataques'],d['Pericias'],d['Testes'],d['Text'])
		if d['tipo'] == 'ND':
			return ND(d['ND'])
		if d['tipo'] == 'DPR':
			return DPR(d['DPR'])
		if d['tipo'] == 'Sala':
			return Sala(d['Nome'],d['Resumo'],d['Capa'])
					
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
		self.__PNome = pnome
		self.__SNome = snome
		self.__Email = email
		self.__Senha = senha
		self.__SenhaC = senhac
		self.__Nick = None
		self.__Acesso = None
		
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
			l = db.search(Q.Senha == senha and Q.Email == email)
			for x in l:
				u = Usuario.fromDict(x)
				Usuario.UpdateAcesso(senha)
				print('Logado com sucesso')
				return u
					
	def toDict(self):
		s = json.dumps(self, cls=MyEncoder)
		return json.loads(s)
		
	@staticmethod
	def fromDict(d):
		s = json.dumps(d)
		return json.loads(s, object_hook=MyEncoder.decode)
		
	@staticmethod
	def UpdateAcesso(senha):
		pass
		
	@property
	def Acesso(self):
		return self.__Acesso
		
	@property
	def PNome(self):
		return self.__PNome
			
	@property
	def SNome(self):
		return self.__SNome
		
	@property
	def Email(self):
		return self.__Email
		
	@property
	def Senha(self):
		return self.__Senha
		
	@property
	def SenhaConfirmacao(self):
		return self.__SenhaC

class Ficha:
	
	def __init__(self, nome, raca, classe, nivel, vida, ca, deslc, antec, forc, dex, cons, intl, sab, car, equip, info, ataq, peri, test):
		self.__Nome = nome
		self.__Raca = raca
		self.__Classe = classe
		self.__Nivel = nivel
		self.__Vida = vida
		self.__CA = ca
		self.__Deslocamento = deslc
		self.__Antecedente = antec
		self.__Forca = forc
		self.__Destreza = dex
		self.__Constituicao = cons
		self.__Inteligencia = intl
		self.__Sabedoria = sab
		self.__Carisma = car
		self.__Equipamento = equip
		self.__Text = info
		self.__Ataques = ataq
		self.__Pericias = peri
		self.__Testes = test
		
	@staticmethod
	def Criar(F):
		l = [F]
		with  TinyDB('Fichas.json') as db:
			for x in l:
				db.insert(x.toDict())
		
	@staticmethod
	def Abrir(self):
		with  TinyDB('dados-exemplo.json') as db:
			for d in db:
				print(d)
		
	def toDict(self):
		s = json.dumps(self, cls=MyEncoder)
		return json.loads(s)
        
	@staticmethod
	def fromDict(d):
		s = json.dumps(d)
		return json.loads(s, object_hook=MyEncoder.decode)
		
	@staticmethod
	def Testes(testes):
		arq = open('Testes.txt','r+')
		arq.write(testes)
		self.__Testes = arq
		arq.close()
		
	@staticmethod
	def Pericias(pericias):
		arq = open('Pericias.txt','r+')
		arq.write(pericias)
		self.__Pericias = arq
		arq.close()
		
	@staticmethod
	def Ataques(ataques):
		arq = open('Ataques.txt','r+')
		arq.write(ataques)
		self.__Ataques = arq
		arq.close()
		
	@staticmethod
	def InformacoesPersonagem(text):
		arq = open('IP2.txt','r+')
		arq.write(text)
		self.__Text = arq
		arq.close()
	
	@staticmethod	
	def Equipamentos(equip):
		arq = open('Equipamentos.txt','r+')
		arq.write(equip)
		self.__Equipamento = arq
		arq.close()
		
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
		return self._Text
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
			
	def toDict(self):
		s = json.dumps(self, cls=MyEncoder)
		return json.loads(s)
		
	@staticmethod
	def fromDict(d):
		s = json.dumps(d)
		return json.loads(s, object_hook=MyEncoder.decode)
