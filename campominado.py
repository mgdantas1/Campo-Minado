# primeira jogada não pode ser uma bomba
# tabuleiro: 7 linhas X 10 colunas
# bombas: 9
# calcular bombas ao redor da célula
# quando o usuário insere as bandeiras no lugar errado, ele perde ao acabar as bandeiras  
# ao clicar numa casa que não tem bombas ao redor (0), ele a exibe, procura as casas vizinhas, verifica se elas também são casas sem bombas ao redor e para ao achar casas com números (1-8)
# se a casa que o usuário clica é uma casa com bomba ao redor, ele só exibe ela
# se a casa for uma bomba, ele revela todas as casas 

from random import randint

class Tabuleiro:
    def __init__(self, jogada_l, jogada_c):
        self.jogada_l = jogada_l - 1
        self.jogada_c = jogada_c - 1
        self.linhas = 7
        self.colunas = 10

    def gerarTabuleiro(self):
        tabuleiro = []
        for l in range(self.linhas):
            tabuleiro += [[]]
            for c in range(self.colunas):
                tabuleiro[l] += ['_']

        self.tabuleiro = tabuleiro
        self.inserirBombas()
        self.contarBombas()

    def inserirBombas(self):
        pass

    def contarBombas(self):
        pass

    def exibirTabuleiro(self):
        pass

    def inserirBandeira(self):
        pass

    def abrirCasa(self):
        pass

    def casasAdjacentes(self, linha, coluna):
        direcoes = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0, 0], [0, 1],
            [1, -1], [1, 0], [1, 1]
        ]
        adjacentes = []
        for i in direcoes:
            n_linha = linha + i[0]
            n_coluna = coluna + i[1]
            if n_linha != linha or n_coluna != coluna:
                if 0 <= n_linha < len(self.tabuleiro) and 0 <= n_coluna < len(self.tabuleiro[0]):
                    adjacentes.append({'l': n_linha, 'c': n_coluna})
    
        self.adjacentes = adjacentes
        
                        
class Bomba(Tabuleiro):
    def __init__(self, jogada_l, jogada_c):
        super().__init__(jogada_l, jogada_c)

    def inserirBombas(self):
        for i in range(9):
            # laço para distribuir as 9 bombas no tabuleiro
            # l_sorteada = linha, c_sorteada = coluna
            l_sorteada = randint(0, self.linhas-1)
            c_sorteada = randint(0, self.colunas-1) 

            # enquanto a linha sorteada for igual a linha que o jogador escolheu e enquanto a coluna for igual a coluna escolhida pelo jogador, sortea-se novos índices até encontrar uma casa diferente da casa escolhida pelo jogador
            while l_sorteada == self.jogada_l and c_sorteada == self.jogada_c:
                l_sorteada = randint(0, self.linhas-1)
                c_sorteada = randint(0, self.colunas-1)

            # enquanto o tabuleiro na linha sorteada e na coluna sorteada for igual a uma bomba, sortea-se novos índices até encontrar uma casa sem bomba
            while self.tabuleiro[l_sorteada][c_sorteada] == 'b':
                l_sorteada = randint(0, self.linhas-1)
                c_sorteada = randint(0, self.colunas-1)

            # após todas as verificações, é adicionado à casa uma bomba
            self.tabuleiro[l_sorteada][c_sorteada] = 'b'

    def contarBombas(self):
        casas = []
        for l in range(len(self.tabuleiro)):
            for c in range(len(self.tabuleiro[l])):
                self.casasAdjacentes(l, c)
                casas += [[[l, c], self.adjacentes]]

        numeros = {}
        for i in range(len(casas)):
            cont = 0
            idx = casas[i][0]
            for c in casas[i][1]:
                linha = c['l']
                coluna = c['c']

                if self.tabuleiro[idx[0]][idx[1]] != 'b':
                    if self.tabuleiro[linha][coluna] == 'b':
                        cont += 1
                else:
                    cont = 'b'
            numeros[str(idx)] = cont

        self.numeros = numeros

class Jogadas(Bomba):
    def __init__(self, jogada_l, jogada_c):
        super().__init__(jogada_l, jogada_c)

    def exibirTabuleiro(self):
        pass

tb = Jogadas(1, 1)
tb.gerarTabuleiro()
tb.exibirTabuleiro()