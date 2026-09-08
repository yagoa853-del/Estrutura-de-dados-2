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

    # Valor no início
    valor_inicio = matriz[0][0]

    encontrado, linha, coluna, comparacoes_inicio = busca_sequencial(
        matriz,
        valor_inicio
    )

    # Valor próximo ao final
    valor_proximo_final = matriz[tamanho - 1][tamanho - 2]

    encontrado, linha, coluna, comparacoes_proximo_final = busca_sequencial(
        matriz,
        valor_proximo_final
    )

    # Valor inexistente
    valor_inexistente = -1

    encontrado, linha, coluna, comparacoes_inexistente = busca_sequencial(
        matriz,
        valor_inexistente
    )

    print("\n" + "=" * 60)
    print(f"MATRIZ {tamanho} x {tamanho}")
    print(f"Quantidade de elementos: {total_elementos}")
    print("=" * 60)

    print("\nBusca no início:")
    print(f"Valor procurado: {valor_inicio}")
    print(f"Comparações: {comparacoes_inicio}")

    print("\nBusca próximo ao final:")
    print(f"Valor procurado: {valor_proximo_final}")
    print(f"Comparações: {comparacoes_proximo_final}")

    print("\nValor inexistente:")
    print(f"Valor procurado: {valor_inexistente}")
    print(f"Comparações: {comparacoes_inexistente}")


def main():
    print("=" * 60)
    print("PARTE 3 - BUSCA SEQUENCIAL EM MATRIZES")
    print("=" * 60)

    executar_teste(2)
    executar_teste(10)
    executar_teste(100)


if __name__ == "__main__":
    main()
