# funções relacionados a coloração

from os import system
from lib.utils import center

system("") # permite a utilização das cores ansi no terminal

cores = {
  "vermelho": "\033[91m",
  "verde"   : "\033[92m",
  "amarelo" : "\033[93m",
  "azul"    : "\033[94m",
  "end"     : "\033[0m"
}


def colorir(mensagem: str, cor: str):
  """
  Devolve a mensagem colirido na cor desejada
  """
  global cores

  return (cores[cor] + mensagem + cores["end"])


def printStyle(mensagem:str, cor="end") -> str:
  """
  imprime a mensagem centralizado e colorido
  """
  print(colorir(center(mensagem), cor))
