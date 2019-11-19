#!-*- conding: utf8 -*
import sys
import json
from tinydb import TinyDB, Query
import pickle
import socket
import select 
from Erros import ErroCriarFicha,ErroOpcaoNaoValida

class MyEncoder(json.JSONEncoder):
	def default(self, o):
		d = vars(o) 
		d['tipo'] = o.__class__.__name__  
		return d
        
	@staticmethod
	def decode(d):
		if d['tipo'] == 'Ficha':
			return Fichas(d['__Nome'],d['__Raca'],d['__Classe'],d['__Nivel'],d['__Vida'],d['__CA'],d['__Deslocamento'],d['__Antecedente'],d['__Forca'],d['__Destreza'],d['__Constituicao'],d['__Inteligencia'],d['__Sabedoria'],d['__Carisma'],d['__Equipamento'],d['__Ataques'],d['__Pericias'],d['__Testes'],d['__Text'])

class Ficha:
	
	__Fichas = {}
	
	def __init__(self, nome, raca, classe, nivel, vida, ca, deslc, antec, forc, dex, cons, intl, sab, car):
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
		self.__Equipamento = None
		self.__Text = None
		self.__Ataques = None
		self.__Pericias = None
		self.__Testes = None
		
	@staticmethod
	def Criar(F):
		Ficha.__Fichas[F.Nome] = F
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

if __name__ == '__main__':
	
	try:
		nome = input('Nome: ')
		raca = input('Raça: ')
		classe = input('Classe: ')
		nivel = input('Nível: ')
		vida = input('Vida: ')
		ca = input('CA: ')
		deslc = input('Deslocamento: ')
		antec = input('Antecedente: ')
		forc = input('Força: ')
		dex = input('Destreza: ')
		cons = input('Constituição: ')
		intl = input('Inteligência: ')
		sab = input('Sabedoria: ')
		car = input('Carisma: ')
	
		F = Ficha(nome, raca, classe, nivel, vida, ca, deslc, antec, forc, dex, cons, intl, sab, car)
		F.Criar(F)
		
		testes = input('Testes: ')
		F.Testes(testes)
		pericias = input('Pericias: ')
		F.Pericias(pericias)
		ataques = input('Ataques: ')
		F.Ataques(ataques)
		text = input('Informações do Personagem: ')
		F.InformacoesPersonagem(text)
		equip = input('Equipamento: ')
		F.Equipamento(equip)
		
		F.Abrir()
		
	except ErroCriarFicha as err1:
		print(err1.args)
	finally:
		print('Fim')
    
