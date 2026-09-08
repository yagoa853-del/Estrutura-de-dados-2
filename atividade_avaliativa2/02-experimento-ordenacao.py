import random


def bubble_sort(lista):
    comparacoes = 0
    trocas = 0

    tamanho = len(lista)

    for i in range(tamanho - 1):
        for j in range(tamanho - 1 - i):
            comparacoes += 1

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1

    return comparacoes, trocas


def quick_sort(lista, inicio, fim, contador):
    if inicio >= fim:
        return

    pivo = lista[(inicio + fim) // 2]

    i = inicio
    j = fim

    while i <= j:

        while lista[i] < pivo:
            contador["comparacoes"] += 1
            i += 1

        contador["comparacoes"] += 1

        while lista[j] > pivo:
            contador["comparacoes"] += 1
            j -= 1

        contador["comparacoes"] += 1

        if i <= j:

            if i != j:
                lista[i], lista[j] = lista[j], lista[i]
                contador["movimentacoes"] += 3

            i += 1
            j -= 1

    if inicio < j:
        quick_sort(lista, inicio, j, contador)

    if i < fim:
        quick_sort(lista, i, fim, contador)


def gerar_array(tamanho):
    return [random.randint(1, 47) for _ in range(tamanho)]


def executar_teste(tamanho):
    array_original = gerar_array(tamanho)

    array_bubble = array_original.copy()
    array_quick = array_original.copy()

    bubble_comparacoes, bubble_trocas = bubble_sort(array_bubble)

    contador_quick = {
        "comparacoes": 0,
        "movimentacoes": 0
    }

    quick_sort(
        array_quick,
        0,
        tamanho - 1,
        contador_quick
    )

    print("\n" + "=" * 60)
    print(f"TESTE COM {tamanho} ELEMENTOS")
    print("=" * 60)

    print("\nBUBBLE SORT")
    print(f"Comparações: {bubble_comparacoes}")
    print(f"Trocas:      {bubble_trocas}")

    print("\nQUICK SORT")
    print(f"Comparações:   {contador_quick['comparacoes']}")
    print(f"Movimentações: {contador_quick['movimentacoes']}")

    if tamanho <= 20:
        print("\nArray original:")
        print(array_original)

        print("\nArray ordenado pelo Bubble Sort:")
        print(array_bubble)

        print("\nArray ordenado pelo Quick Sort:")
        print(array_quick)


def main():
    print("=" * 60)
    print("PARTE 2 - EXPERIMENTO DE ORDENAÇÃO")
    print("=" * 60)

    executar_teste(10)
    executar_teste(20)
    executar_teste(1000)


if __name__ == "__main__":
    main()
