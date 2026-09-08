def investigar_temperaturas():

    temperatura = []

    print("=" * 60)
    print("PARTE 4 - INVESTIGAÇÃO DO ARRAY")
    print("=" * 60)

    print("\nDigite 10 temperaturas:")

    for i in range(10):
        valor = float(input(f"Temperatura [{i}]: "))
        temperatura.append(valor)

    print("\n" + "=" * 60)
    print("TEMPERATURAS ARMAZENADAS")
    print("=" * 60)

    for i in range(10):
        print(f"Índice [{i}] = {temperatura[i]:.2f} °C")

    soma = 0
    operacoes = 0

    for valor in temperatura:
        soma += valor
        operacoes += 1

    media = soma / 10

    maior = temperatura[0]
    menor = temperatura[0]

    indice_maior = 0
    indice_menor = 0

    for i in range(1, 10):

        operacoes += 1

        if temperatura[i] > maior:
            maior = temperatura[i]
            indice_maior = i

        operacoes += 1

        if temperatura[i] < menor:
            menor = temperatura[i]
            indice_menor = i

    acima_media = 0

    for valor in temperatura:

        operacoes += 1

        if valor > media:
            acima_media += 1

    print("\n" + "=" * 60)
    print("RESULTADOS")
    print("=" * 60)

    print(f"Media: {media:.2f} °C")
    print(f"Maior temperatura: {maior:.2f} °C")
    print(f"Índice do maior valor: {indice_maior}")
    print(f"Menor temperatura: {menor:.2f} °C")
    print(f"Índice do menor valor: {indice_menor}")
    print(f"Valores acima da média: {acima_media}")

    print(
        f"Operações aproximadas de percurso: {operacoes}"
    )

    print("\nComplexidade: O(n)")


def main():
    investigar_temperaturas()


if __name__ == "__main__":
    main()
