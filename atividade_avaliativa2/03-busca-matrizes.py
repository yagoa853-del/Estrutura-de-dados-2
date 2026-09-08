def criar_matriz(linhas, colunas):
    matriz = []
    valor = 1

    for i in range(linhas):
        linha = []

        for j in range(colunas):
            linha.append(valor)
            valor += 1

        matriz.append(linha)

    return matriz


def busca_sequencial(matriz, valor_procurado):
    comparacoes = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):

            comparacoes += 1

            if matriz[i][j] == valor_procurado:
                return True, i, j, comparacoes

    return False, -1, -1, comparacoes


def executar_teste(tamanho):
    matriz = criar_matriz(tamanho, tamanho)

    total_elementos = tamanho * tamanho

    print("\n" + "=" * 60)
    print(f"MATRIZ {tamanho} x {tamanho}")
    print(f"Quantidade de elementos: {total_elementos}")
    print("=" * 60)

    print("\nBusca no início:")

    encontrado, linha, coluna, comparacoes = busca_sequencial(
        matriz,
        1
    )

    print(f"Encontrado: {encontrado}")
    print(f"Linha: {linha}")
    print(f"Coluna: {coluna}")
    print(f"Comparações: {comparacoes}")

    print("\nBusca no final:")

    encontrado, linha, coluna, comparacoes = busca_sequencial(
        matriz,
        total_elementos
    )

    print(f"Encontrado: {encontrado}")
    print(f"Linha: {linha}")
    print(f"Coluna: {coluna}")
    print(f"Comparações: {comparacoes}")

    print("\nValor inexistente:")

    encontrado, linha, coluna, comparacoes = busca_sequencial(
        matriz,
        -1
    )

    print(f"Encontrado: {encontrado}")
    print(f"Linha: {linha}")
    print(f"Coluna: {coluna}")
    print(f"Comparações: {comparacoes}")


def main():
    print("=" * 60)
    print("PARTE 3 - BUSCA SEQUENCIAL EM MATRIZES")
    print("=" * 60)

    executar_teste(2)
    executar_teste(10)
    executar_teste(100)


if __name__ == "__main__":
    main()
