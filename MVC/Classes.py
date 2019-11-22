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
		
		
class Sala:
	
	__Salas = {}
	
	def __init__(self, nome):
		self.__Nome = nome
		self.__Resumo = text
		self.__Capa = capa
	
	def Criar(S):
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
		
