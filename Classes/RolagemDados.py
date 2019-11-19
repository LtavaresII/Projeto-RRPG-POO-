#!-*- conding: utf8 -*
import sys
import random
import json
from tinydb import TinyDB, Query
import pickle
import socket
import select 
from Erros import ErroComandoInvalido,ErroOpcaoNaoValida

class MyEncoder(json.JSONEncoder):
	def default(self, o):
		d = vars(o) 
		d['tipo'] = o.__class__.__name__  
		return d
		
	@staticmethod
	def decode(d):
		if d['tipo'] == 'ND':
			return ND(d['__ND'])
		if d['tipo'] == 'DPR':
			return DPR(d['__DPR'])
			
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


if __name__ == '__main__':
	R = RolagemdeDados()
	try:
		ND = int(input('Numero de Dados: '))
		DPR = int(input('Dado para Rolar: '))
		
		print(R.RolarDados(ND,DPR))
	except ErroComandoInvalido as err1:
		print(err1.args)
	finally:
		print('Fim')
   
