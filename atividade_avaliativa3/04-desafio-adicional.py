import random

def bubble_sort(vetor):
    comparacoes = 0
    trocas = 0

    for i in range(len(vetor) - 1):
        houve_troca = False

        for j in range(len(vetor) - 1 - i):
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

    for i in range(len(vetor) - 1):
        menor = i

        for j in range(i + 1, len(vetor)):
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


def executar_algoritmos(vetor):
    bubble = vetor.copy()
    insertion = vetor.copy()
    selection = vetor.copy()
    quick = vetor.copy()

    b_comp, b_trocas = bubble_sort(bubble)
    i_comp, i_mov = insertion_sort(insertion)
    s_comp, s_trocas = selection_sort(selection)

    contador = {
        "comparacoes": 0,
        "movimentacoes": 0
    }

    quick_sort(
        quick,
        0,
        len(quick) - 1,
        contador
    )

    print("BUBBLE SORT")
    print("Comparações:", b_comp)
    print("Trocas:", b_trocas)

    print("\nINSERTION SORT")
    print("Comparações:", i_comp)
    print("Movimentações:", i_mov)

    print("\nSELECTION SORT")
    print("Comparações:", s_comp)
    print("Trocas:", s_trocas)

    print("\nQUICK SORT")
    print("Comparações:", contador["comparacoes"])
    print("Movimentações:", contador["movimentacoes"])


def executar_teste(tamanho):
    vetor = [random.randint(1, 47) for _ in range(tamanho)]

    ordenado = sorted(vetor)
    invertido = sorted(vetor, reverse=True)

    print("\n" + 20 * "=")
    print("TESTE COM", tamanho, "ELEMENTOS")
    print(20 * "=")

    print("\n" + 20 * "-")
    print("VETOR ALEATÓRIO")
    print(20 * "-")
    executar_algoritmos(vetor)

    print("\n" + 20 * "-")
    print("VETOR JÁ ORDENADO")
    print(20 * "-")
    executar_algoritmos(ordenado)

    print("\n" + 20 * "-")
    print("VETOR INVERSAMENTE ORDENADO")
    print(20 * "-")
    executar_algoritmos(invertido)


def main():
    print(20 * "=")
    print("DESAFIO ADICIONAL")
    print(20 * "=")

    executar_teste(10)
    executar_teste(20)
    executar_teste(1000)


main()
