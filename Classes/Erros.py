#!-*- conding: utf8 -*
import sys

class ErroBase(Exception):
	pass
	
class ErroChat(ErroBase):
	pass
	
class ErroSenhaUsuarioIncorreto(ErroBase):
	pass
	
class ErroNomeIncorreto(ErroBase):
	pass
	
class ErroCriarFicha(ErroBase):
	pass
	
class ErroComandoInvalido(ErroBase):
	pass
	
class ErroInteracao(ErroBase):
	pass
	
class ErroOpcaoNaoValida(ErroBase):
	pass
	
class ErroCriacaoUsuario(ErroBase):
	pass
		
class ErroCriacaodeSala(ErroBase):
	pass
