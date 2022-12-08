# contem as funções utilitarias relacionadas ao board

# importação de modulo
from lib.color import colorir

branco = "○" # o caracter que será preenchido no espaço em branco
jogado = "●" # o caracter que será monstrado na tela (com cores)

cores = [
  "azul",    # cor de jogador 1 [0]
  "verde",   # cor de jogador 2 [1]
  "vermelho" # cor de jogada vencedora
]

def criarBoard(linhas: int, colunas: int) -> list:
  """
  Cria uma board usando as linhas e colunas especificadas em formato de array bidimensional
  """
  board = []

  for i in range(linhas):
    board.append([]) # adciona uma nova linha
    for j in range(colunas):
      board[i].append(branco)

  return board


def printBoard(board: list, encontrados=[]) -> None:
  """
  Imprime na tela a board formatado

  Caso seja fodrnecido 'entrados' imprime estes 
  """
  global cores

  for i in range(len(board)):
    for j in range(len(board[i])):
      casa = board[i][j]
      if encontrados: # caso seja fornecido os resultados encontrados
        for posição in encontrados:
          if posição[0] == i and posição[1] == j:
            casa = colorir(jogado, cores[2])
      if type(casa) == int:
        # muda a casa para ser imprimido a cores e jogado
        casa = colorir(jogado, cores[casa]) # aplica cores
      print(f' {casa} ', end="")
    print()


def jogar(board: list, coluna: int, jogador: int) -> any:
  """
  Joga na primeira casa na disponivel na coluna de baixo para cima

  O numero de jogador que será preenchido
  Caso a jogado não é possivel retorna false
  """
  for i in range(len(board)-1, -1, -1): # começamos por verificar de traz para frente
    if board[i][coluna] == branco:
      board[i][coluna] = jogador
      return board

  return False


def vertical(board: list, jogadas: int) -> bool:
  """
  Verifica se existe uma jogada vencedora na vertical

  retorna false caso não encontre 
  ou um array com as posições encontradas
  """
  global branco

  last = 0
  encontrados = []
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == last and board[i][j] != branco:
        encontrados.append([i, j])

        if len(encontrados) == jogadas:
          return encontrados
      else:
        encontrados = []
        encontrados.append([i, j])
        last = board[i][j]
      
  return False


def horizontal(board: list, jogadas: int) -> bool:
  """
  Verifica se existe uma jogada vencedora na horizontal

  retorna false caso não encontre 
  ou um array com as posições encontradas
  """
  global branco

  last = 0
  encontrados = []
  for j in range(len(board[0])):
    for i in range(len(board)):
      if board[i][j] == last and board[i][j] != branco:
        encontrados.append([i, j])

        if len(encontrados) == jogadas:
          return encontrados
      else:
        encontrados = []
        encontrados.append([i, j])
        last = board[i][j]
      
  return False


def diagonal(board: list, jogadas: int) -> bool:
  """
  Verifica se existe uma jogada vencedora na diagonal

  retorna false caso não encontre 
  ou um array com as posições encontradas
  """
  global branco

  last = 0
  encontrados = []
  start = 0
  coluna = start
  
  # primeiro verifica por colunas
  while start < len(board[0]):
    for i in range(len(board)):
      if coluna == len(board[0]):
        break
      casa = board[i][coluna]
      if casa == last and casa != branco:
        encontrados.append([i, coluna])

        if len(encontrados) == jogadas:
          return encontrados
      else:
        encontrados = []
        encontrados.append([i, coluna])

        last = casa
      
      coluna += 1
    start += 1
    coluna = start
  
  # agora verificando por linhas
  start = 0
  coluna = 0
  while start < len(board):
    for i in range(start, len(board)):
      if coluna == len(board[0]):
        break
      casa = board[i][coluna]
      if casa == last and casa != branco:
        encontrados.append([i, coluna])

        if len(encontrados) == jogadas:
          return encontrados
      else:
        encontrados = []
        encontrados.append([i, coluna])

        last = casa
      
      coluna += 1
    start += 1
    coluna = 0

  return False
