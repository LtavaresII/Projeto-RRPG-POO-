#modelo de chat, parte de teste
import socket

import json
from threading import Thread

HOST = '127.0.0.1'  # Endereco IP
PORT = 12000        # Porta

class ServerWork(Thread):
    def __init__(self,conn):
        Thread.__init__(self)
        self._conn = conn

    def run(self):
        with self._conn as conn:
            while True:
                msg = conn.recv(1024)
                print(msg.decode())
                
class Server:
    def __init__(self, host, port ):
        self._host = host
        self._port = port

    def iniciar(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((self._host, self._port))
                s.listen()
                while True:
                    conn, addr = s.accept()
                    T = ServerWork(conn)
                    T.start()




        except Exception as err:
            print('Erro na conexao...{0}'.format(err))

if __name__ == "__main__":
    S = Server(HOST,PORT)
    S.iniciar()