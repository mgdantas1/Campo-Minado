tabuleiro = [
    ['_', 'b', '_'],
    ['b', '_', '_'],
    ['_', '_', '_']
]

def casasAdjacentes(tabuleiro, linha, coluna):
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
            if 0 <= n_linha < len(tabuleiro) and 0 <= n_coluna < len(tabuleiro[0]):
                adjacentes.append({'l': n_linha, 'c': n_coluna})
    
    return adjacentes
            

def contarBombas(tabuleiro):
    casas = []
    for l in range(len(tabuleiro)):
        for c in range(len(tabuleiro[l])):
            adj = casasAdjacentes(tabuleiro, l, c)
            casas += [[[l, c], adj]]
    num = {}
    for i in range(len(casas)):
        cont = 0
        idx = casas[i][0]
        for c in casas[i][1]:
            linha = c['l']
            coluna = c['c']
            
            if tabuleiro[idx[0]][idx[1]] != 'b':
                if tabuleiro[linha][coluna] == 'b':
                    cont += 1
            else:
                cont = 'b'

        num[str(idx)] = cont
    print(num)
    return casas




casas = contarBombas(tabuleiro)

# for l in range(len(tabuleiro)):
#     for c in range(len(tabuleiro[l])):
#         print(tabuleiro[l][c], end=' ')
#     print()

# for i in range(len(casas)):
#     for j in range(len(casas[i])):
#         print(casas[i][2], end=' ')
#     print()

# for l in range(len(tabuleiro)):
#     for c in range(len(tabuleiro[l])):
#         print(tabuleiro[l][c], end=' ')
#     print()