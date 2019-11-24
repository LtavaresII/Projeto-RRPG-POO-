import socket

HOST = '127.0.0.1'  # Endereco IP do servidor
PORT = 12000        # Porta utilizada no servidor

class Cliente:
     def __init__(self, host, port):
        self._host = host
        self._port = port

     def iniciar(self):
        '''Iniciar conexao, receber uma mensagem e enviar uma mensagem'''
        try:
            
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                print("Conectado!")
                while True:
                    msg = str(input('digite: '))
                    msg = "luis:"+msg
                    s.send(msg.encode())
                    #Receber até 1024 bytes do servidor
                
                
                
                    
        except Exception as E:
            print('Erro na conexao...{0}'.format(E))
        
if __name__ == "__main__":
    C = Cliente(HOST,PORT)
    C.iniciar()