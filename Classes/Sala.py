#!-*- conding: utf8 -*
import sys
import json
from tinydb import TinyDB, Query
import pickle
import socket
import select 
from Erros import ErroOpcaoNaoValida,ErroCriacaodeSala

class MyEncoder(json.JSONEncoder):
	def default(self, o):
		d = vars(o) 
		d['tipo'] = o.__class__.__name__  
		return d
		
	@staticmethod
	def decode(d):
		if d['tipo'] == 'Sala':
			return Salas(d['__Nome'],d['__Resumo'],d['__Capa'])

class Sala:
	
	__Salas = {}
	
	def __init__(self, nome):
		self.__Nome = nome
		self.__Resumo = text
		self.__Capa = capa
	
	def Criar(S):
		Sala.__Salas[S.Nome] = S
		l = [S]
		with  TinyDB('Salas.json') as db:
			for x in l:
				db.insert(x.toDict())
	
	@staticmethod	
	def Convidar(self):
		
	@staticmethod
	def Entrar(self):
		
	@staticmethod
	def Sair(self):
		
	@staticmethod
	def BuscarNome(nome):
		with  TinyDB('Salas.json') as db:
			Q = Query()
			l = db.search(Q.Nome == nome)
			for x in l:
				s = Sala.fromDict(x)
				print(s)
			
	@staticmethod
	def MudarResumo(nome,text):
		with  TinyDB('Salas.json') as db:
			Q = Query()
			l = db.update({'__Resumo' : text}, Q.__Nome == nome)
		
    @staticmethod
	def MudarCapa(capa):
		with open('Capa.png', 'wb') as arq:
		
	def toDict(self):
		s = json.dumps(self, cls=MyEncoder)
		return json.loads(s)
		
	@staticmethod
	def fromDict(d):
		s = json.dumps(d)
		return json.loads(s, object_hook=MyEncoder.decode)
        
    @property
    def Nome(self):
		return self.__Nome
		
	@property
	def Resumo(self):
		return self.__Resumo
		
	@property
	def Capa(self):
		return self.__Capa

if __name__ == '__main__':
	try:
		nome = input('Nome da Sala: ')
		
		S = Sala(nome)
		S.Criar(S)
		
		nome = input('Nome da Sala: ')
		resumo = input('Resumo: ')
		S.MudarResumo(nome,resumo)
		
		nome = input('Nome da Sala: ')
		S.BuscarNome(nome)
	except ErroCriacaodeSala as err1:
		print(err1.args)
	finally:
		print('Fim')
		
	
 
