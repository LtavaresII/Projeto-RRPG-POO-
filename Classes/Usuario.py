#!-*- conding: utf8 -*
import sys
import json
from tinydb import TinyDB, Query
import pickle
import socket
import select 
from Erros import ErroSenhaUsuarioIncorreto,ErroCriacaoUsuario,ErroOpcaoNaoValida

class MyEncoder(json.JSONEncoder):
	def default(self, o):
		d = vars(o) 
		d['tipo'] = o.__class__.__name__  
		return d
		
	@staticmethod
	def decode(d):
		if d['tipo'] == 'Usuario':
			return Usuarios(d['__PNome'],d['__SNome'],d['__Email'],d['__Senha'],d['__SenhaC'],d['__Acesso'])
		if d['tipo'] == 'Email':
			return Email(d['__Email'])
		if d['tipo'] == 'Senha':
			return Senha(d['__Senha'])

class Usuario:
	__Usuarios = {}
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
		if U.Email in Usuario.__Usuarios:
            raise ErroCriacaoUsuario('Usuario ja existe')
        else:
			Usuario.__Usuarios[U.Senha] = U
			l = [U]
			with  TinyDB('Usuarios.json') as db:
				for x in l:
					db.insert(x.toDict())
		
	@staticmethod
	def Logar(email, senha):
		
		if senha not in Usuario.__Usuarios or email not in Usuario.__Usuarios:
            raise ErroSenhaUsuarioIncorreto('Senha incorreta/Usuario Incorreto')
        else:
			with  TinyDB('Usuarios.json') as db:
				Q = Query()
				l = db.search(Q.__Senha == senha and Q.__Email == email)
				for x in l:
					u = Usuario.fromDict(x)
					UpdateAcesso(senha)
					print('Logado com sucesso')
					
	def toDict(self):
		s = json.dumps(self, cls=MyEncoder)
		return json.loads(s)
		
	@staticmethod
	def fromDict(d):
		s = json.dumps(d)
		return json.loads(s, object_hook=MyEncoder.decode)
        
    @staticmethod
    def UpdateAcesso(senha):
		U = Usuario.__Usuarios[senha]
        U.Acesso = True
    
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
        return self.__Email = email
		
	@property
	def Senha(self):
		return self.__Senha
		
	@property
	def SenhaConfirmacao(self):
		return self.__SenhaC

class Perfil(Usuario):
	def __init__(self):
		Usuario.__init__(self)
		
	@PNome.setter
	def PrimeiroNome(self,pnome):
		
	@SNome.setter
	def SegundoNome(self,snome):
		
	@Email.setter
	def Email(self,email):
		
	@Nick.setter
	def Nick(self,nick):
		
	@Senha.setter
	def Senha(self,senha):
		
	@SenhaConfirmacao.setter
	def SenhaConfirmacao(self,senha):

if __name__ == '__main__':
	try:
		pnome = input('Primeiro Nome: ')
		snome = input('Segundo Nome: ')
		email = input('Email: ')
		senha = input('Senha: ')
		senhac = input('Senha de Confirmação: ')
		
		U = Usuario(pnome, snome, email, senha, senhac)
		U.Cadastrar(U)
		
	except ErroCriacaoUsuario as err1:
		print(err1.args)
	finally:
		print('Fim')
		
	try:
		email = input('Email: ')
		senha = input('Senha: ')
		
		U.Logar(email,senha)
		
	except ErroSenhaUsuarioIncorreto as err2:
		print(err1.args)
	finally:
		print('Fim')
  
