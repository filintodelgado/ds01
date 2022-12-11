# Jogo quatro em linha

O jogo quatro em linha é bem simples, jogas uma ficha em uma coluna e este cai até a ultima casa disponivel. São dois jogadores e quando um consegue orgazinar quatro fichas na diagonal, vertical ou horizonal ganha o jogo.
Jogo desenvolvido como desafio da disciplina de **Algoritmia e Estrutura de Dados** no [Instituto Politécnico do Porto](https://www.ipp.pt/).

## Modos
### Single player
Jogas contra um algoritmo que joga sempre onde há uma maior sequencia na horizontal ou na vertical ou numa coluna aleatoria.

### Multiplayer
Jogas com um amigo.

## Board
A board é de 7x6
○○○○○○○
○○○○○○○
○○○○○○○
○○○○○○○
○○○○○○○
○○○○○○○ 

## Organização de arquivos
O [main.py](./main.py) contem coração do programa. Na pasta lib contem as funções usadas pelo main como o [board.py](./lib/board.py) que contem as funções relacionadas ao board, [color.py](./lib/color.py) para uso de cores no terminal e [utils.py](./lib/utils.py) que contem funções genericas como receber input do usuario.

# Creditos
Todas a funções e codigo salvo as que são built-in no python são de minha autoria ([Filinto Delgado](https://github.com/filintodelgado)). Você é livre para estudar e usar como preferir.