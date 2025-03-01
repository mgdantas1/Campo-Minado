# primeira jogada não pode ser uma bomba
# tabuleiro: 7 linhas X 10 colunas
# bombas: 9
# calcular bombas ao redor da célula
# quando o usuário insere as bandeiras no lugar errado, ele perde ao acabar as bandeiras  
# ao clicar numa casa que não tem bombas ao redor (0), ele a exibe, procura as casas vizinhas, verifica se elas também são casas sem bombas ao redor e para ao achar casas com números (1-8)
# se a casa que o usuário clica é uma casa com bomba ao redor, ele só exibe ela
# se a casa for uma bomba, ele revela todas as casas 
# verificar se o usúario não clicou em uma casa que já abriu ou se ele clicou numa casa que já foi revelado que tem bombas ao redor
# garantir que as casas adjacentes da primeira casa aberta estejam livres
# possiveis erros: numeros inválidos (str, não esteja em determinado intervalo, float)

from random import randint
import os
import time

class Tabuleiro:
    def __init__(self):
        self.linhas = 7
        self.colunas = 10
        self.tabuleiro = []

    def opcao(self):
        pass

    def gerarTabuleiro(self, casa):
        for l in range(self.linhas):
            self.tabuleiro += [[]]
            for c in range(self.colunas):
                self.tabuleiro[l] += ['*']
        self.inserirBombas(casa)
        self.contarBombas()

    def contarBombas(self):
        pass

    def revelarCasas(self, abrirCasa, inserirBandeira):
        pass

    def garantir_num_válido(self):
        pass

    def verificarCasa(self, ):
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
    def __init__(self):
        super().__init__()

    def inserirBombas(self, abrirCasa):
        abrirCasa 
        self.bombas_local = {}
        
        contador_bombas = 0
        while contador_bombas < 9:
            l_sorteada = randint(0, self.linhas-1)
            c_sorteada = randint(0, self.colunas-1)
            
            if (l_sorteada != self.jogada_l or c_sorteada != self.jogada_c) and self.tabuleiro[l_sorteada][c_sorteada] != 'b':
                adjacente = False
                self.casasAdjacentes(self.jogada_l, self.jogada_c)
                for adj in self.adjacentes:
                    if adj['l'] == l_sorteada and adj['c'] == c_sorteada:
                        adjacente = True
                        break
                
                if not adjacente:
                    self.bombas_local[contador_bombas] = {'l': l_sorteada, 'c': c_sorteada}
                    self.tabuleiro[l_sorteada][c_sorteada] = 'b'
                    contador_bombas += 1  

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
                    cont = -1

            numeros[str(idx)] = cont

        self.numeros = numeros

class Jogada(Bomba):
    def __init__(self):
        super().__init__()
        self.abriuBomba = False
        self.bombaBandeira = False
        self.qnt_bandeiras = 9
    
    def revelarCasas(self, abrircasa, inserirbandeira):
        if abrircasa != 0:
            if self.tabuleiro[self.jogada_l][self.jogada_c] == 'b':
                self.abriuBomba = True
            
            abrircasa
            fila_abertura = [(self.jogada_l, self.jogada_c)]  
            casas_abertas = set() 
        
            while fila_abertura:
                l, c = fila_abertura.pop(0)
                if (l, c) not in casas_abertas:
                    casas_abertas.add((l, c))
                    if self.numeros[str([l, c])] == 0:  
                        self.tabuleiro[l][c] = '0'
                        self.casasAdjacentes(l, c)
                        for adj in self.adjacentes:
                            adj_l, adj_c = adj['l'], adj['c']
                            if (adj_l, adj_c) not in casas_abertas and self.tabuleiro[adj_l][adj_c] != 'b':
                                fila_abertura.append((adj_l, adj_c))
                    else:
                        self.tabuleiro[l][c] = str(self.numeros[str([l, c])])
        else:
            inserirbandeira
            if self.qnt_bandeiras > 0:
                if self.tabuleiro[self.jogada_l][self.jogada_c] != 'b':
                    self.bombaBandeira = True
                    print('\nNão é possível inserir mais bombas.')
                self.qnt_bandeiras -= 1
                self.tabuleiro[self.jogada_l][self.jogada_c] = 'X'
            else:
                print('\nNão é possível inserir mais bombas.')
    
    def abrirCasa(self):
        self.verificarCasa()

    def inserirBandeira(self):
        if self.qnt_bandeiras > 0:
            self.verificarCasa()
        else:
            print('Não é possível inserir mais bandeiras.')

    def garantir_num_válido(self):
        while True:
            try:
                self.jogada_l = int(input('\nDigite a linha (0-6): '))
                if not 0 <= self.jogada_l <= 6:
                    print('\nDigite apenas números no intervalo de 0 à 6.')
                    continue
                self.jogada_c = int(input('\nDigite a coluna (0-9): '))
                if not 0 <= self.jogada_c <= 9:
                    print('\nDigite apenas números no intervalo de 0 à 9.')
                    continue
            except ValueError:
                print('\nDigite um número inteiro.')
            else:
                break

    def verificarCasa(self):
        while True:
            self.garantir_num_válido()
            if len(self.tabuleiro) > 0:
                if self.tabuleiro[self.jogada_l][self.jogada_c] in 'X012345678':
                    print('\nNão é possível abrir essa casa.')
                else:
                    break
            else:
                break

class Jogar(Jogada):
    def __init__(self):
        super().__init__()
        self.tempo_t = 0
        self.nome = ''

    def exibirSimbolos(self):
        lista = ['X', '*', 'b', '1', '0']

        print('\n' + '-='*10, end=' ')
        print(' CAMPO MINADO ', end=' ')
        print('-='*10 + '\n')

        for i in lista:
            if i == 'X':
                print('\033[0;31;47m' + ' X ', end='')
                print('\033[0m' + ' : Bandeira')
            elif i == '*':
                print('\033[0;30;0m' + ' * ', end='')
                print('\033[0m' + ' : Casa não aberta')
            elif i == 'b':
                print('\033[0;37;41m' + ' * ', end='')
                print('\033[0m' + ' : Bomba')
            elif i == '1':
                print('\033[0;34;47m' + ' 1 ', end='')
                print('\033[0m' + ' : Casa com bombas ao redor')
            else:
                print('\033[0;37;42m' + '   ', end='')
                print('\033[0m' + ' : Casa aberta')
        print()
    
    def exibirTabuleiro(self):
        os.system('cls')
        self.exibirSimbolos()
        if self.abriuBomba:
            print(' '*2, end='')
            for c in range(self.colunas):
                print(f' {c} ', end='')
            print()
            for l in range(self.linhas):
                print(l, end=' ')
                for c in range(self.colunas):
                    elemento = self.tabuleiro[l][c]
                    if elemento == '0':
                        print('\033[0;37;42m' + '  ', end=' ')
                    elif elemento in '12345678':
                        print(f'\033[0;34;47m {elemento}', end=' ')
                    elif elemento == 'X':
                        print('\033[0;31;47m' + ' X', end=' ')  
                    elif elemento == 'b' or elemento == '-1':
                        print('\033[0;37;41m' + ' *', end=' ')  
                    else:
                        print('\033[0;30;0m' + ' *', end=' ')
                print('\033[0m')
            print('\nO JOGADOR ABRIU UMA BOMBA. VOCÊ PERDEU...\n')
        else:
            print(' '*2, end='')
            for c in range(self.colunas):
                print(f' {c} ', end='')
            print()
            for l in range(self.linhas):
                print(l, end=' ')
                for c in range(self.colunas):
                    elemento = self.tabuleiro[l][c]
                    if elemento == '0':
                        print('\033[0;37;42m' + '  ', end=' ')
                    elif elemento in '12345678':
                        print(f'\033[0;34;47m {elemento}', end=' ')
                    elif elemento == 'X':
                        print('\033[0;31;47m' + ' X', end=' ')  
                    elif elemento == 'b' or elemento == '-1':
                        print('\033[0;30;0m' + ' *', end=' ')  
                    else:
                        print('\033[0;30;0m' + ' *', end=' ')
                print('\033[0m')
            
            if self.qnt_bandeiras == 0:
                if self.bombaBandeira:
                    print('\nO JOGADOR INSERIU A BANDEIRA NO LUGAL ERRADO. VOCÊ PERDEU...\n')
                else:
                    print('\nO JOGADOR DESCOBRIU TODAS AS BOMBA. VOCÊ GANHOU!\n')

    def menu(self):
        print()
        print('-='*10, end=' ')
        print(' MENU ', end=' ')
        print('-='*10)
    
        print('\n1 - Iniciar/Reiniciar\n2 - Abrir Casa\n3 - Inserir Bandeira\n4 - Sair')

    def cadastro(self, nome, tempo):
        with open('cadastro.txt', 'a', encoding='utf-8') as arq:
            arq.write(nome + '\n')
            arq.write(str(tempo) + '\n')
            arq.close()

        with open('cadastro.txt', 'r', encoding='utf-8') as arq:
            self.linhas_arq = arq.readlines()

    def exibirTempo(self):
        print(f'\nTEMPO DE {self.linhas_arq[0][:-1]}: {self.linhas_arq[-1][:-1]} s.')

    def opcao(self):
        os.system('cls')
        def verificar_opcao():
            self.menu()
            while True:
                try:
                    self.opcao = int(input('\nDigite a opção escolhida: ' ))
                    if self.opcao < 1 or self.opcao > 4: 
                        os.system('cls')
                        self.menu()
                        print('\nOpção inválida. Tente novamente.')
                        continue
                except ValueError:
                    print('\nDigite somente números inteiros.')
                else:
                    break

        jogar = False
        finalizar = False
        while True:
            verificar_opcao()
            if self.qnt_bandeiras == 0 or self.abriuBomba:
                finalizar = True
                self.fim = time.time()
                self.tempo_t = int(self.fim - self.inicio)
                self.cadastro(self.nome, self.tempo_t)
                if self.opcao == 2 or self.opcao == 3:
                    os.system('cls')
                    print('\nNão é possível fazer mais jogadas. Inicie outra partida.')
            if self.opcao == 4:
                if os.path.exists('cadastro.txt'):
                    os.remove('cadastro.txt')
                self.fim = time.time()
                self.tempo_t = int(self.fim - self.inicio)
                self.cadastro(self.nome, self.tempo_t)
                self.exibirTempo()
                break
            if self.opcao == 1:
                self.tempo_t = 0
                finalizar = False
                self.inicio = time.time()          
                self.abriuBomba = False
                self.bombaBandeira = False
                self.qnt_bandeiras = 9
                os.system('cls')
                print('  ', end='')
                for coluna in range(self.colunas):
                    print(f' {coluna} ', end='')
                print()
                for l in range(self.linhas):
                    print(l, end=' ')
                    for c in range(self.colunas):
                        print(' *', end=' ')
                    print()
                if jogar:
                    self.tabuleiro = []
                    abrir_casa = self.abrirCasa()
                    self.gerarTabuleiro(abrir_casa)
                    self.revelarCasas(abrir_casa, 0)
                    os.system('cls')
                    self.exibirTabuleiro()
                else:
                    jogar = True
                    self.nome = input('\nDigite seu nome: ').upper().strip()
                    while self.nome == '':
                        self.nome = input('\nDigite seu nome: ').upper().strip()
                    abrir_casa = self.abrirCasa()
                    self.gerarTabuleiro(abrir_casa)
                    self.revelarCasas(abrir_casa, 0)
                    os.system('cls')
                    self.exibirTabuleiro()
            if not finalizar:
                if self.opcao == 2:
                    if jogar:
                        abrir_casa = self.abrirCasa()
                        self.revelarCasas(abrir_casa, 0)
                        os.system('cls')
                        self.exibirTabuleiro()
                    else:
                        os.system('cls')
                        print('\nOpção inválida. Digite 1 para iniciar o jogo.')
                elif self.opcao == 3:   
                    if jogar:
                        colocar_bandeira = self.inserirBandeira()
                        self.revelarCasas(0, colocar_bandeira)
                        os.system('cls')
                        self.exibirTabuleiro()
                    else:
                        os.system('cls')
                        print('\nOpção inválida. Digite 1 para iniciar o jogo.')

if __name__ == '__main__':
    tb = Jogar()
    tb.opcao()
    