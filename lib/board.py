# contem as funções utilitarias relacionadas ao board

# importação de modulo
from lib.color import colorir
from lib.utils import center

branco = "○" # o caracter que será preenchido no espaço em branco
jogado = "●" # o caracter que será monstrado na tela (com cores)

coresBoard = [
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

  Caso seja fornecido 'entrados' imprime estes 
  """
  global coresBoard

  linhas = ""
  indicações = ""

  # imprime indicação de colunas
  for i in range(len(board[0])): 
    indicações += f' {i+1} '
  
  print(center("-"*len(indicações)))
  print(center(indicações))
  print(center("-"*len(indicações)))


  for i in range(len(board)):
    linhas = ""
    for j in range(len(board[i])):
      casa = board[i][j]
      if encontrados: # caso seja fornecido os resultados encontrados
        for posição in encontrados:
          if posição[0] == i and posição[1] == j:
            casa = colorir(jogado, coresBoard[2])
      if type(casa) == int:
        # muda a casa para ser imprimido a cores e jogado
        casa = colorir(jogado, coresBoard[casa]) # aplica cores
      linhas+=f' {casa} '

    print(center(linhas, 21))


def jogar(board: list, coluna: int, jogador: int) -> any:
  """
  Joga na primeira casa disponivel na coluna de baixo para cima

  O numero do jogador será preenchido
  Caso a jogado não é possivel retorna false
  """
  if verificarColuna(board, coluna) > -1:
    board[verificarColuna(board, coluna)][coluna] = jogador
    return True

  return False


def horizontal(board: list, sequencia: int) -> bool:
  """
  Verifica se existe uma jogada vencedora na horizontal
  ●●●●○○
  retorna false caso não encontre 
  ou um array com as posições encontradas
  """
  global branco

  last = 0         # a ultima ficha encontrada
  encontrados = [] # guarda as posições encontradas 
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == last and board[i][j] != branco: # caso a ficha seja igual a anterior e não seja um espaço em branco
        encontrados.append([i, j]) # adciona aos encontrados

        if len(encontrados) == sequencia: # encontramos fichas suficientes
          return encontrados
      else:
        encontrados = []
        encontrados.append([i, j])
        last = board[i][j]
    
    encontrados = []
    last = 0
      
  return False


def vertical(board: list, sequencia: int) -> bool:
  """
  Verifica se existe uma jogada vencedora na vertical

  retorna false caso não encontre 
  ou um array com as posições encontradas
  """
  """
  ○
  ○
  ●
  ●
  ●
  ●
  """
  global branco

  last = 0
  encontrados = []
  for j in range(len(board[0])): # verificamos para cada coluna
    for i in range(len(board)):
      if board[i][j] == last and board[i][j] != branco:
        encontrados.append([i, j])

        if len(encontrados) == sequencia:
          return encontrados
      else:
        encontrados = []
        encontrados.append([i, j])
        last = board[i][j]
    encontrados = []
    last = 0
      
  return False


def diagonal(board: list, sequencia: int) -> bool:
  """
  Retorna as 'posições' da primeira 'sequencia' encontrada na diagonal, ou 'False' caso não encontre
  """
  global branco

  # primeiro verifica por colunas de esquerda para a direita
  #   a cada iteração começamos na proxima coluna
  #   ●○○○○○○ -> ○●○○○○○ e assim por diante até a ultima coluna
  last = 0         # o ultimo player encontrado
  encontrados = [] # sequencias encontradas
  # por que coluna começar
  coluna_inicial = 0
  coluna = coluna_inicial
  while coluna_inicial < len(board[0]): # enquanto ainda não chegar a ultima coluna
    for i in range(len(board)): # para cada linha
      if coluna == len(board[0]): # temos que verificar se o index de colunas não é maior que o numero de colunas
        break # se for vamos sair do loop
      casa = board[i][coluna]
      if casa == last and casa != branco:
        encontrados.append([i, coluna])

        if len(encontrados) == sequencia: # já encontramos uma sequencia
          return encontrados
      else:
        encontrados = []
        encontrados.append([i, coluna])

        last = casa
      
      coluna += 1
    coluna_inicial += 1 # passa para a proxima coluna
    coluna = coluna_inicial
    # reseta as variaveis
    encontrados = []
    last = 0
  
  # verifica por colunas de direita para a esquerda
  #   começamos na ultima coluna
  #   a cada iteração começamos na coluna anterior
  #   ○○○○○○● -> ○○○○○●○ e assim por diante até a ultima coluna
  last = 0 
  encontrados = []
  # começar da ultima coluna
  coluna_inicial = len(board[0]) - 1
  coluna = coluna_inicial
  while coluna_inicial > -1: # enquanto ainda não chegar a primeira coluna (0)
    for i in range(len(board)): # para cada linha
      if coluna < 0: # temos que verificar se o index de colunas é menor que 0
        break # se for vamos sair do loop
      casa = board[i][coluna]
      if casa == last and casa != branco:
        encontrados.append([i, coluna])

        if len(encontrados) == sequencia: # já encontramos uma sequencia
          return encontrados
      else:
        encontrados = []
        encontrados.append([i, coluna])

        last = casa
      
      coluna -= 1
    coluna_inicial -= 1 # passa para a proxima coluna
    coluna = coluna_inicial
    # reseta as variaveis
    encontrados = []
    last = 0
  
  # verificando por linhas de esquerda para direita
  # a cada iteração começamos na proxima linha
  # -----1º---- | -----2º----
  # 1 - ●○○○○○○ | 1 - ○○○○○○○
  # 2 - ○●○○○○○ | 2 - ○●○○○○○
  linha_inicial = 0  # começando da primeira linha
  coluna = 0 # e da primeira coluna
  while linha_inicial < len(board): # enquanto não for a ultima linha
    for i in range(linha_inicial, len(board)): # para cada linha
      if coluna == len(board[0]):
        break
      casa = board[i][coluna]
      if casa == last and casa != branco:
        encontrados.append([i, coluna])

        if len(encontrados) == sequencia:
          return encontrados
      else:
        encontrados = []
        encontrados.append([i, coluna])

        last = casa
      
      coluna += 1
    linha_inicial += 1 # proxima linha
    coluna = 0 # começamos na primeira coluna
    last = 0
    encontrados = []
  
  # verificando por linhas de direita para esquerda
  # a cada iteração começamos na proxima linha
  # -----1º---- | -----2º----
  # 1 - ○○○○○○● | 1 - ○○○○○○○
  # 2 - ○○○○○●○ | 2 - ○○○○○○●
  linha_inicial = 0  # começando da primeira linha
  coluna_inicial = len(board[0]) - 1 # e da ultima coluna
  coluna = coluna_inicial
  while linha_inicial < len(board): # enquanto não for a ultima linha
    for i in range(linha_inicial, len(board)): # para cada linha
      if coluna < 0:
        break
      casa = board[i][coluna]
      if casa == last and casa != branco:
        encontrados.append([i, coluna])

        if len(encontrados) == sequencia:
          return encontrados
      else:
        encontrados = []
        encontrados.append([i, coluna])

        last = casa
      
      coluna -= 1
    linha_inicial += 1 # proxima linha
    coluna = coluna_inicial # começamos na primeira coluna
    last = 0
    encontrados = []


def encontrarSequencia(board: list, sequencia: int) -> bool:
  """
  Verifica se existe uma sequencia de 'sequencia' na horizontal, vertical e diagonal

  Retorna as posições ou False se não existe um vencedor
  """
  if horizontal(board, sequencia):
    return horizontal(board, sequencia)
  
  if vertical(board, sequencia):
    return vertical(board, sequencia)
  
  if diagonal(board, sequencia):
    return diagonal(board, sequencia)
  
  return False


def verificarColuna(board: list, coluna:int) -> int:
  """
  Verifica se a coluna está livre
  Retorna a coluna se estiver ou -1 senão
  """
  for i in range(len(board)-1, -1, -1): # começamos por verificar de traz para frente
    if board[i][coluna] == branco:
      return i
  
  return -1