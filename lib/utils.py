# um conjunto de funções utilitarios genericos


def get_str(prompt="Escreva: ", error_prompt="Input invalido", min_lenght=0):
  while True: # existe como fazer isso com recursão mas acho que isso pode ser perigoso em termos de memoria
    try:
      dada = input(prompt).strip() # remove os espaçoes em branco antes de fazer a validação

      if len(dada) < min_lenght or dada == "" or dada == " ":
        raise ValueError
    except ValueError:
      print(error_prompt)
    else:
      return dada


def get_int(max=False, min=0, prompt="Digite: ", error_prompt="Input invalido"):
  while True:
    try:
      number = int(input(prompt))

      if (max and number > max) or number < min:
        raise ValueError
    except ValueError:
      print(error_prompt)
    else:
      return number