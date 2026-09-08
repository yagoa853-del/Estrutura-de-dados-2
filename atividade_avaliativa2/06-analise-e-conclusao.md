# PARTE 6 – ANÁLISE E CONCLUSÃO

## 1. Análise dos experimentos

Os experimentos realizados demonstram que o tamanho da estrutura de dados influencia diretamente a quantidade de operações executadas pelos algoritmos.

No experimento de ordenação, o Bubble Sort apresentou crescimento quadrático no número de comparações. Isso ocorre porque o algoritmo realiza sucessivas passagens pelo array, comparando elementos adjacentes.

O Quick Sort, por outro lado, apresenta crescimento médio de O(n log n), o que faz com que seja geralmente mais eficiente para conjuntos maiores de dados.

A diferença fica mais evidente quando o tamanho do array aumenta de 10 para 20 e, principalmente, para 1.000 elementos.

## 2. Bubble Sort e Quick Sort

Os dois algoritmos conseguem produzir o mesmo resultado final: um array ordenado.

Entretanto, eles utilizam estratégias diferentes.

O Bubble Sort utiliza comparações entre elementos adjacentes e realiza trocas sucessivas. Já o Quick Sort utiliza um pivô e divide o problema em partes menores.

Dessa forma, o crescimento da quantidade de operações não ocorre da mesma maneira.

O Bubble Sort apresenta complexidade O(n²) no caso médio, enquanto o Quick Sort apresenta O(n log n) no caso médio.

Portanto, conforme o número de elementos aumenta, a diferença de eficiência entre os algoritmos tende a aumentar.

## 3. Busca sequencial em matrizes

Os experimentos com matrizes demonstraram que a quantidade de comparações depende diretamente da posição do elemento procurado.

Quando o elemento está no início da matriz, apenas uma comparação é necessária.

Quando o elemento está próximo do final, praticamente todos os elementos precisam ser analisados.

Quando o elemento não existe, todos os elementos da matriz precisam ser percorridos.

Por isso, para uma matriz com m linhas e n colunas, a complexidade da busca sequencial é:

O(m × n)

No pior caso, todas as m × n posições precisam ser verificadas.

## 4. Influência do tamanho da estrutura

O aumento do tamanho da estrutura de dados aumenta a quantidade de operações necessárias.

Uma estrutura pequena pode ser processada rapidamente mesmo utilizando algoritmos menos eficientes. Porém, quando a quantidade de elementos aumenta, algoritmos com complexidades diferentes apresentam comportamentos cada vez mais distintos.

No Bubble Sort, por exemplo, o número de comparações cresce aproximadamente de forma quadrática.

Na busca sequencial em uma matriz, a quantidade máxima de comparações corresponde ao número total de posições existentes.

## 5. Por que analisar apenas o resultado não é suficiente?

Observar somente o resultado final não é suficiente para comparar algoritmos porque diferentes algoritmos podem produzir exatamente a mesma saída utilizando quantidades diferentes de operações.

Por exemplo, Bubble Sort e Quick Sort podem receber o mesmo array e produzir exatamente o mesmo array ordenado.

Apesar disso, a quantidade de comparações, trocas e movimentações realizadas pode ser muito diferente.

Por esse motivo, a análise de algoritmos deve considerar não apenas se o resultado está correto, mas também a quantidade de recursos necessários para obtê-lo.

## 6. Conclusão

Os experimentos permitiram observar na prática a relação entre o tamanho da entrada, a quantidade de operações e a complexidade computacional.

O Bubble Sort apresentou uma lógica simples, porém seu crescimento de operações torna o algoritmo pouco adequado para grandes conjuntos de dados.

O Quick Sort apresentou uma estratégia mais eficiente para conjuntos maiores, principalmente devido à sua complexidade média O(n log n).

A busca sequencial em matrizes também demonstrou que a posição do elemento influencia diretamente a quantidade de comparações. No pior caso, quando o elemento está no final ou não existe, toda a matriz precisa ser percorrida.

Os experimentos mostram, portanto, que analisar algoritmos apenas pelo resultado final não é suficiente. É necessário observar também a quantidade de operações realizadas e como essa quantidade cresce conforme o tamanho da entrada aumenta.

Dessa forma, a análise de complexidade permite escolher algoritmos mais adequados para cada situação e compreender melhor o impacto do tamanho dos dados sobre o desempenho de um programa.
