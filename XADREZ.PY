print("Movimentando as Peças do Xadrez (super simples)")

# Cria tabuleiro 8x8 vazio
tabuleiro = [["." for _ in range(8)] for _ in range(8)]

# Posição inicial da torre
linha, coluna = 0, 0
tabuleiro[linha][coluna] = "T"

def mostrar_tabuleiro():
    for l in tabuleiro:
        print(" ".join(l))
    print()

mostrar_tabuleiro()

while True:
    mov = input("Digite nova posição da torre (ex: 3 4) ou 'sair': ")
    if mov.lower() == "sair":
        break
    
    try:
        nova_linha, nova_coluna = map(int, mov.split())
        if 0 <= nova_linha < 8 and 0 <= nova_coluna < 8:
            # Limpa posição antiga
            tabuleiro[linha][coluna] = "."
            # Atualiza posição
            linha, coluna = nova_linha, nova_coluna
            tabuleiro[linha][coluna] = "T"
            mostrar_tabuleiro()
        else:
            print("Posição inválida! Use números de 0 a 7.")
    except:
        print("Entrada inválida! Digite linha e coluna, exemplo: 3 4.")
