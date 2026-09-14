import random


def bubble_sort(vetor):
    comparacoes = 0
    trocas = 0

    tamanho = len(vetor)

    for i in range(tamanho - 1):

        houve_troca = False

        for j in range(tamanho - 1 - i):

            comparacoes += 1

            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
                trocas += 1
                houve_troca = True

        if not houve_troca:
            break

    return comparacoes, trocas


def insertion_sort(vetor):
    comparacoes = 0
    movimentacoes = 0

    for i in range(1, len(vetor)):

        chave = vetor[i]
        j = i - 1

        while j >= 0:

            comparacoes += 1

            if vetor[j] > chave:
                vetor[j + 1] = vetor[j]
                movimentacoes += 1
                j -= 1
            else:
                break

        vetor[j + 1] = chave
        movimentacoes += 1

    return comparacoes, movimentacoes


def selection_sort(vetor):
    comparacoes = 0
    trocas = 0

    tamanho = len(vetor)

    for i in range(tamanho - 1):

        menor = i

        for j in range(i + 1, tamanho):

            comparacoes += 1

            if vetor[j] < vetor[menor]:
                menor = j

        if menor != i:
            vetor[i], vetor[menor] = vetor[menor], vetor[i]
            trocas += 1

    return comparacoes, trocas


def quick_sort(vetor, inicio, fim, contador):

    if inicio >= fim:
        return

    pivo = vetor[(inicio + fim) // 2]

    i = inicio
    j = fim

    while i <= j:

        while vetor[i] < pivo:
            contador["comparacoes"] += 1
            i += 1

        contador["comparacoes"] += 1

        while vetor[j] > pivo:
            contador["comparacoes"] += 1
            j -= 1

        contador["comparacoes"] += 1

        if i <= j:

            if i != j:
                vetor[i], vetor[j] = vetor[j], vetor[i]
                contador["movimentacoes"] += 1

            i += 1
            j -= 1

    if inicio < j:
        quick_sort(vetor, inicio, j, contador)

    if i < fim:
        quick_sort(vetor, i, fim, contador)


def gerar_vetor(tamanho):
    return [random.randint(1, 47) for _ in range(tamanho)]


def executar_experimento(tamanho):

    vetor_original = gerar_vetor(tamanho)

    vetor_bubble = vetor_original.copy()
    vetor_insertion = vetor_original.copy()
    vetor_selection = vetor_original.copy()
    vetor_quick = vetor_original.copy()

    bubble_comparacoes, bubble_trocas = bubble_sort(vetor_bubble)

    insertion_comparacoes, insertion_movimentacoes = insertion_sort(
        vetor_insertion
    )

    selection_comparacoes, selection_trocas = selection_sort(
        vetor_selection
    )

    contador_quick = {
        "comparacoes": 0,
        "movimentacoes": 0
    }

    quick_sort(
        vetor_quick,
        0,
        tamanho - 1,
        contador_quick
    )

    print("\n" + 20 * "=")
    print(f"TESTE COM {tamanho} ELEMENTOS")
    print(20 * "=")

    print("\nBUBBLE SORT")
    print(f"Comparações: {bubble_comparacoes}")
    print(f"Trocas:      {bubble_trocas}")

    print("\nINSERTION SORT")
    print(f"Comparações:   {insertion_comparacoes}")
    print(f"Movimentações: {insertion_movimentacoes}")

    print("\nSELECTION SORT")
    print(f"Comparações: {selection_comparacoes}")
    print(f"Trocas:      {selection_trocas}")

    print("\nQUICK SORT")
    print(f"Comparações:   {contador_quick['comparacoes']}")
    print(f"Movimentações: {contador_quick['movimentacoes']}")

    if tamanho <= 20:

        print("\nVetor original:")
        print(vetor_original)

        print("\nVetor ordenado pelo Bubble Sort:")
        print(vetor_bubble)

        print("\nVetor ordenado pelo Insertion Sort:")
        print(vetor_insertion)

        print("\nVetor ordenado pelo Selection Sort:")
        print(vetor_selection)

        print("\nVetor ordenado pelo Quick Sort:")
        print(vetor_quick)


def main():

    print(20 * "=")
    print("EXPERIMENTO COMPARATIVO DE ALGORITMOS")
    print(20 * "=")

    executar_experimento(10)
    executar_experimento(20)
    executar_experimento(1000)


if __name__ == "__main__":
    main()
