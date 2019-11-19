# -*- coding: utf-8 -*-

import socket
import json
import sys
from Usuario import Usuario
from Ficha import Ficha
from RolagemdeDados import RolagemdeDados
from Sala import Sala
from threading import Thread
from _thread import *
import _thread

HOST = '127.0.0.1'  # Endereco IP
PORT = 12011        # Porta

class ServerWork(Thread):
    def __init__(self, conn):
        '''Inicializa a tarefa com o socket do cliente'''
        Thread.__init__(self)
        self._conn = conn

    def run(self):
        '''Escutar as solicitações do cliente'''
        U = Usuario()
        F = Ficha()
        S = Sala()
        R = RolagemdeDados()
        with self._conn as conn:
            while True:
                dados = conn.recv(2048)
                opc = dados.decode()
                if opc == "cadastrar":
					conn.send(b'Esperando dados...')
					prods = conn.recv(2048)
					U = json.loads(prods.decode(),object_hook=Usuario.MyEncoder.decode)
					
					U.Cadastrar(U)
					conn.send(b'Usuario Cadastrado [OK]')
					
				elif opc == "logar":
					conn.send(b'Esperando dados...')
					prods = conn.recv(2048)
					email = json.loads(prods.decode(),object_hook=Email.MyEncoder.decode)
					senha = json.loads(prods.decode(),object_hook=Senha.MyEncoder.decode)
					
					U.Logar(email,senha)
					conn.send(b'Usuario Logado [OK]')
					
				elif opc == "ficha":
					conn.send(b'Esperando dados...')
					prods = conn.recv(2048)
					F = json.loads(prods.decode(),object_hook=Ficha.MyEncoder.decode)
					
					F.Criar(F)
					conn.send(b'Ficha Criada [OK]')
					
				elif opc == "abrir ficha":
					conn.send(b'Abrindo ficha')
					prods = conn.recv(2048)
					
					F.Abrir()
					conn.send(b'Ficha Aberta [OK]')
					
				elif opc == "rolar dados":
					conn.send(b'Esperando dados...')
					prods = conn.recv(2048)
					ND = json.loads(prods.decode(),object_hook=ND.MyEncoder.decode)
					DPR = json.loads(prods.decode(),object_hook=DPR.MyEncoder.decode)
					
					print(R.RolarDados(ND,DPR))
					conn.send(b'Dado(s) Rolado(s) [OK]')
					
				elif opc == "criar sala":
					conn.send(b'Esperando dados...')
					prods = conn.recv(2048)
					S = json.loads(prods.decode(),object_hook=Sala.MyEncoder.decode)
					
					S.Criar(S)
					conn.send(b'Sala Criada [OK]')
					
                elif opc == "terminar":
                    print('Fim do cliente')
                    break

class Server:
    def __init__(self, host, port ):
        self._host = host
        self._port = port

    def iniciar(self):
        '''Utiliza ServerWork para atender os clientes '''

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((self._host, self._port)) # Selecionar o endereco e porta
                s.listen() # Escutar solicitacoes

                while True:
                    # Novo cliente
                    conn, addr = s.accept()
                    T = ServerWork(conn)
                    T.start() # Um thread para cada nova conexão 
        
        except Exception as E:
            print('Erro na conexao...{0}'.format(E))


if __name__ == "__main__":
    S = Server(HOST,PORT)
    S.iniciar()
