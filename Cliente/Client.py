# -*- coding: utf-8 -*-

import socket
import sys
from Usuario import Usuario, Perfil, MyEncoder
from Ficha import Ficha, MyEncoder
from Sala import Sala, MyEncoder
from RolagemdeDados import RolarDados, MyEncoder
import json
import time
import random

HOST = '127.0.0.1'  # Endereco IP do servidor
PORT = 12011        # Porta utilizada no servidor

class Cliente:
    def __init__(self, conn):
        self._conn = conn
        
    def CadastrarUsuario(self,pnome,snome,email,senha,senhac):
		self._conn.send(b'cadastrar')
		resposta = self._con.recv(2048)
		print(resposta.decode())
		U = Usuario(pnome,snome,email,senha,senhac)
		
		self._conn.send(str.encode(json.dumps(U, cls=MyEncoder)))
		resposta = self._conn.recv(2048)
		print(resposta.decode())
		
	def LogarUsuario(self,Email,Senha):
		self._conn.send(b'logar')
		resposta = self._con.recv(2048)
		print(resposta.decode())
		
		self._conn.send(str.encode(json.dumps(Email, cls=MyEncoder)))
		
		self._conn.send(str.encode(json.dumps(Senha, cls=MyEncoder)))
		
		resposta = self._conn.recv(2048)
		print(resposta.decode())
		
	def CriarFicha(self, nome, raca, classe, nivel, vida, ca, deslc, antec, forc, dex, cons, intl, sab, car):
		self._conn.send(b'ficha')
		resposta = self._con.recv(2048)
		print(resposta.decode())
		F = Ficha(nome, raca, classe, nivel, vida, ca, deslc, antec, forc, dex, cons, intl, sab, car)
		
		self._conn.send(str.encode(json.dumps(F, cls=MyEncoder)))
		resposta = self._conn.recv(2048)
		print(resposta.decode())
		
	def AbrirFicha(self):
		self._conn.send(b'abrir ficha')
		resposta = self._con.recv(2048)
		print(resposta.decode())
		
		resposta = self._con.recv(2048)
		print(resposta.decode())
		
	def CriarSala(self, nome):
		self._conn.send(b'criar sala')
		resposta = self._con.recv(2048)
		print(resposta.decode())
		S = Sala(nome)
		
		self._conn.send(str.encode(json.dumps(S, cls=MyEncoder)))
		resposta = self._con.recv(2048)
		print(resposta.decode())
		
	def RolarDados(self,ND,DPR):
		self._conn.send(b'rolar dados')
		resposta = self._con.recv(2048)
		print(resposta.decode())
		
		self._conn.send(str.encode(json.dumps(ND, cls=MyEncoder)))
		
		self._conn.send(str.encode(json.dumps(DPR, cls=MyEncoder)))
		
		resposta = self._conn.recv(2048)
		print(resposta.decode())
		
		
    #def enviarProduto(self):
        #'''Cria e envia um produto (aleatoriamente) usando o socket conn'''
        #self._conn.send(b'adicionar')
        #resposta = self._conn.recv(2048)
        #print(resposta.decode())
        #cod = random.randint(1,10000)
        #preco = random.randint(1,2000)
        #P = Produto(cod, 'nome-' + str(cod), preco, [Cor('azul'), Cor('branco')])

        #self._conn.send(str.encode(json.dumps(P, cls=MyEncoder)))
        #resposta = self._conn.recv(2048)
        #print(resposta.decode())
    
    #def receberLista(self):
        #'''Receber a lista de produtos utilizando o socket conn'''
        #self._conn.send(b'listar')
        #dados = b''
        #while True:
            #d= self._conn.recv(2048)
            #dados += d
            #if  len(d)< 2048:
                #break

        #L = json.loads(dados.decode(),object_hook=MyEncoder.decode)
        #return L

    def terminar(self):
        '''Enviar mensagem de fim utilizando o socket conn'''
        self._conn.send(b'terminar')

if __name__ == "__main__":
 
