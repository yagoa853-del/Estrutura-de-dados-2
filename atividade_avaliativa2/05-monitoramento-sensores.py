def monitorar_sensores():

    sensores = []

    print("=" * 60)
    print("PARTE 5 - MONITORAMENTO DE SENSORES")
    print("=" * 60)

    print("\nDigite as 120 temperaturas.")

    for i in range(5):

        sensor = []

        print(f"\nSensor {i}")

        for j in range(24):
            temperatura = float(
                input(f"Hora {j:02d}: ")
            )

            sensor.append(temperatura)

        sensores.append(sensor)

    print("\n" + "=" * 60)
    print("MÉDIA DE CADA SENSOR")
    print("=" * 60)

    medias_sensores = []

    for i in range(5):

        soma = 0

        for j in range(24):
            soma += sensores[i][j]

        media = soma / 24
        medias_sensores.append(media)

        print(
            f"Sensor {i}: {media:.2f} °C"
        )

    maior_temperatura = sensores[0][0]
    sensor_maior = 0
    horario_maior = 0

    soma_geral = 0

    for i in range(5):

        for j in range(24):

            temperatura = sensores[i][j]

            soma_geral += temperatura

            if temperatura > maior_temperatura:
                maior_temperatura = temperatura
                sensor_maior = i
                horario_maior = j

    media_geral = soma_geral / 120

    print("\n" + "=" * 60)
    print("RESULTADOS GERAIS")
    print("=" * 60)

    print(
        f"Maior temperatura registrada: "
        f"{maior_temperatura:.2f} °C"
    )

    print(
        f"Sensor responsável: {sensor_maior}"
    )

    print(
        f"Horário da ocorrência: {horario_maior:02d}:00"
    )

    print(
        f"Média geral: {media_geral:.2f} °C"
    )

    limite = float(
        input("\nDigite um limite de temperatura: ")
    )

    acima_limite = 0

    for i in range(5):

        for j in range(24):

            if sensores[i][j] > limite:
                acima_limite += 1

    print(
        f"\nQuantidade de leituras acima de "
        f"{limite:.2f} °C: {acima_limite}"
    )

    print("\n" + "=" * 60)
    print("ANÁLISE DA MATRIZ")
    print("=" * 60)

    print(
        "São necessários loops aninhados porque a matriz "
        "possui duas dimensões."
    )

    print(
        "O primeiro índice [i] representa o sensor "
        "e o segundo índice [j] representa o horário."
    )

    print(
        "A matriz possui 5 x 24 = 120 posições."
    )

    print(
        "As operações de percurso crescem de acordo com "
        "a quantidade de linhas e colunas."
    )

    print(
        "A complexidade dos percursos é O(m x n)."
    )


def main():
    monitorar_sensores()


if __name__ == "__main__":
    main()
