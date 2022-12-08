# um conjunto de funções utilitarios genericos


def get_str(prompt: str, error_prompt: str, min_lenght: int) -> str:
  """
  Coleta um input de string valido do usuario fazendo toda a sanatização necessario

  prompt: a mensagem que aparece na tela na hora de coletar o input
  error_prompt: mensagem em caso de erro
  min_lenght: o tamanho minimo da string
  """
  while True: # existe como fazer isso com recursão mas acho que isso pode ser perigoso em termos de memoria
    try:
      dada = input(prompt).strip() # remove os espaçoes em branco antes de fazer a validação

      if len(dada) < min_lenght or dada == "" or dada == " ":
        raise ValueError
    except ValueError:
      print(error_prompt)
    else:
      return dada


def get_int(max: int, min: int, prompt: str, error_prompt: str) -> str:
  """
  Coleta um input de um numero inteiro valido do usuario

  max: o tamanho maximo do numero
  min: o tamnanho minimo
  prompt: a mensagem que aparece na tela na hora de coletar o input
  error_prompt: a mensagem de error
  """
  while True:
    try:
      number = int(input(prompt))

      if (max and number > max) or number < min:
        raise ValueError
    except ValueError:
      print(error_prompt)
    else:
      return number