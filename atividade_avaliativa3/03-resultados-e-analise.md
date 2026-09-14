# ETAPA 3 – RESULTADOS E ANÁLISE

## 1. Resultados do experimento

Os quatro algoritmos de ordenação foram executados utilizando os mesmos dados iniciais em cada experimento.

Foram utilizados vetores com 10, 20 e 1.000 elementos.

A quantidade de comparações e trocas ou movimentações foi registrada para cada algoritmo.

### Tabela de operações

| Tamanho | Bubble Comparações | Bubble Trocas | Insertion Comparações | Insertion Mov. | Selection Comparações | Selection Trocas | Quick Comparações | Quick Mov. |
| ------: | -----------------: | ------------: | --------------------: | -------------: | --------------------: | ---------------: | ----------------: | ---------: |
|      10 |                 39 |            21 |                    29 |             30 |                    45 |                7 |                36 |          8 |
|      20 |                175 |            87 |                   104 |            106 |                   190 |               16 |               100 |         19 |
|   1.000 |            498.597 |       238.821 |               239.815 |        239.820 |               499.500 |              969 |            10.881 |      3.057 |

---

## 2. Critério de contagem

Para realizar a comparação entre os algoritmos, foram utilizados os seguintes critérios:

* **Comparação:** cada operação utilizada para verificar a relação entre dois valores.
* **Bubble Sort:** cada troca de dois elementos foi contabilizada como uma troca.
* **Insertion Sort:** cada deslocamento de um elemento foi contabilizado como uma movimentação, incluindo a inserção da chave em sua posição.
* **Selection Sort:** cada troca realizada foi contabilizada como uma troca.
* **Quick Sort:** cada troca de dois elementos foi contabilizada como uma movimentação.

---

## 3. Análise dos resultados

### a) Qual algoritmo realizou o menor número de comparações para 10 elementos?

Para 10 elementos, o **Insertion Sort** realizou o menor número de comparações, com **29 comparações**.

O Quick Sort realizou 36, o Bubble Sort 39 e o Selection Sort 45 comparações.

---

### b) Qual algoritmo realizou menos trocas ou movimentações?

O **Selection Sort** apresentou a menor quantidade de trocas ou movimentações nos três testes.

Foram realizadas:

* 7 trocas para 10 elementos;
* 16 trocas para 20 elementos;
* 969 trocas para 1.000 elementos.

O Quick Sort também apresentou uma quantidade baixa de movimentações, principalmente quando comparado aos algoritmos Bubble Sort e Insertion Sort.

---

### c) O comportamento observado para 10 elementos permaneceu semelhante quando o tamanho aumentou para 20?

O comportamento geral permaneceu semelhante, mas houve aumento significativo na quantidade de operações.

Com 10 elementos, o Insertion Sort apresentou o menor número de comparações, enquanto com 20 elementos o Quick Sort apresentou o menor número de comparações.

O Selection Sort continuou realizando poucas trocas em comparação aos demais algoritmos.

Portanto, alguns comportamentos permaneceram semelhantes, mas a diferença de desempenho entre os algoritmos começou a ficar mais evidente com o aumento do vetor.

---

### d) O que aconteceu com a quantidade de operações quando o vetor passou para 1.000 elementos?

Quando o vetor passou para 1.000 elementos, houve um aumento muito grande na quantidade de operações dos algoritmos quadráticos.

O Bubble Sort realizou **498.597 comparações e 238.821 trocas**, enquanto o Insertion Sort realizou **239.815 comparações e 239.820 movimentações**.

O Selection Sort realizou **499.500 comparações**, mas apenas **969 trocas**.

Já o Quick Sort realizou apenas **10.881 comparações e 3.057 movimentações**.

Isso mostra que, com grandes quantidades de dados, a diferença de eficiência entre os algoritmos se torna muito mais evidente.

---

### e) Bubble Sort, Insertion Sort e Selection Sort apresentam complexidade O(n²) em situações típicas estudadas. Eles apresentaram exatamente a mesma quantidade de operações? Explique utilizando seus resultados.

Não. Mesmo apresentando complexidade O(n²), os três algoritmos não realizaram exatamente a mesma quantidade de operações.

No teste com 1.000 elementos, por exemplo, o Bubble Sort realizou **498.597 comparações**, o Insertion Sort realizou **239.815** e o Selection Sort realizou **499.500**.

Além disso, a quantidade de trocas ou movimentações também foi bastante diferente. O Bubble Sort realizou **238.821 trocas**, enquanto o Selection Sort realizou apenas **969**.

Isso acontece porque cada algoritmo possui uma estratégia diferente para ordenar os elementos. A complexidade O(n²) representa o comportamento de crescimento das operações, mas não determina que dois algoritmos realizarão exatamente a mesma quantidade de operações.

---

### f) Qual algoritmo apresentou maior crescimento no número de operações?

O **Bubble Sort** e o **Selection Sort** apresentaram os maiores crescimentos no número de comparações.

O Bubble Sort passou de **39 comparações**, com 10 elementos, para **498.597**, com 1.000 elementos.

O Selection Sort passou de **45 comparações** para **499.500**.

O crescimento mostra claramente o comportamento quadrático desses algoritmos.

O Quick Sort, por outro lado, passou de 36 comparações para apenas 10.881 no teste com 1.000 elementos, apresentando um crescimento muito menor.

---

### g) Como o comportamento experimental do Quick Sort se diferenciou dos demais algoritmos?

O Quick Sort apresentou um crescimento muito menor na quantidade de operações conforme o tamanho do vetor aumentou.

Com 1.000 elementos, foram realizadas **10.881 comparações e 3.057 movimentações**, valores muito inferiores aos apresentados pelo Bubble Sort, Insertion Sort e Selection Sort.

Enquanto os algoritmos quadráticos chegaram a centenas de milhares de operações, o Quick Sort permaneceu na casa dos milhares.

Esse comportamento está relacionado à sua complexidade média **O(n log n)**, que tende a ser mais eficiente para grandes conjuntos de dados.

---

### h) Os resultados encontrados são coerentes com as complexidades teóricas estudadas?

Sim. Os resultados são coerentes com as complexidades teóricas estudadas.

Bubble Sort, Insertion Sort e Selection Sort apresentaram um crescimento muito grande no número de operações quando o vetor aumentou para 1.000 elementos, comportamento esperado para algoritmos de complexidade O(n²) em situações típicas.

O Quick Sort apresentou crescimento significativamente menor, mantendo-se com milhares de operações em vez de centenas de milhares, o que é compatível com seu comportamento médio O(n log n).

Os resultados experimentais demonstram, na prática, a diferença esperada entre os algoritmos.

---

### i) Se você fosse responsável pelo sistema da central de distribuição e precisasse ordenar milhares de pedidos, qual dos quatro algoritmos escolheria?

Eu escolheria o **Quick Sort**.

Nos testes realizados, ele apresentou uma quantidade de operações muito menor para vetores grandes. Com 1.000 elementos, realizou apenas **10.881 comparações e 3.057 movimentações**, enquanto os demais algoritmos chegaram a centenas de milhares de comparações.

Além disso, sua complexidade média é **O(n log n)**, sendo mais adequada para trabalhar com grandes volumes de dados.

Por isso, para uma central de distribuição que precisa ordenar milhares de pedidos, o Quick Sort seria a escolha mais eficiente entre os quatro algoritmos analisados.

---

## 4. Conclusão

Os experimentos permitiram comparar quatro algoritmos de ordenação utilizando os mesmos conjuntos de dados.

Os resultados mostraram que o comportamento dos algoritmos varia conforme o tamanho do vetor. Para pequenos conjuntos de dados, as diferenças entre eles são menores, mas quando o número de elementos aumenta, as diferenças de desempenho se tornam muito mais evidentes.

Bubble Sort, Insertion Sort e Selection Sort apresentaram comportamentos compatíveis com a complexidade O(n²), embora tenham realizado quantidades diferentes de comparações e trocas ou movimentações.

O Quick Sort apresentou o melhor comportamento no teste com 1.000 elementos, realizando apenas 10.881 comparações e 3.057 movimentações.

Dessa forma, os resultados experimentais confirmaram a importância de analisar a complexidade dos algoritmos antes de escolher uma solução para sistemas que precisam processar grandes quantidades de dados.

Para o cenário da central de distribuição de pedidos, o **Quick Sort** se mostrou a alternativa mais adequada entre os algoritmos estudados.
