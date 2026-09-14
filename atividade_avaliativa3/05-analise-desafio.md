# DESAFIO ADICIONAL – INFLUÊNCIA DA ORGANIZAÇÃO DO VETOR

## 1. Objetivo

O desafio adicional tem como objetivo verificar se a organização inicial dos elementos do vetor influencia a quantidade de operações realizadas pelos algoritmos de ordenação.

Foram analisados três cenários:

* Vetor aleatório;
* Vetor já ordenado;
* Vetor inversamente ordenado.

Os testes foram realizados com vetores de 10, 20 e 1.000 elementos.

---

## 2. Resultados

### 10 elementos

| Organização           | Algoritmo      | Comparações | Trocas/Movimentações |
| --------------------- | -------------- | ----------: | -------------------: |
| Aleatório             | Bubble Sort    |          35 |                   20 |
| Aleatório             | Insertion Sort |          27 |                   29 |
| Aleatório             | Selection Sort |          45 |                    8 |
| Aleatório             | Quick Sort     |          50 |                    8 |
| Já ordenado           | Bubble Sort    |           9 |                    0 |
| Já ordenado           | Insertion Sort |           9 |                    9 |
| Já ordenado           | Selection Sort |          45 |                    0 |
| Já ordenado           | Quick Sort     |          31 |                    0 |
| Inversamente ordenado | Bubble Sort    |          45 |                   45 |
| Inversamente ordenado | Insertion Sort |          45 |                   54 |
| Inversamente ordenado | Selection Sort |          45 |                    5 |
| Inversamente ordenado | Quick Sort     |          34 |                    5 |

### 20 elementos

| Organização           | Algoritmo      | Comparações | Trocas/Movimentações |
| --------------------- | -------------- | ----------: | -------------------: |
| Aleatório             | Bubble Sort    |         180 |                   68 |
| Aleatório             | Insertion Sort |          84 |                   87 |
| Aleatório             | Selection Sort |         190 |                   14 |
| Aleatório             | Quick Sort     |          96 |                   17 |
| Já ordenado           | Bubble Sort    |          19 |                    0 |
| Já ordenado           | Insertion Sort |          19 |                   19 |
| Já ordenado           | Selection Sort |         190 |                    0 |
| Já ordenado           | Quick Sort     |          86 |                    3 |
| Inversamente ordenado | Bubble Sort    |         190 |                  187 |
| Inversamente ordenado | Insertion Sort |         190 |                  206 |
| Inversamente ordenado | Selection Sort |         190 |                   11 |
| Inversamente ordenado | Quick Sort     |          88 |                   13 |

### 1.000 elementos

| Organização           | Algoritmo      | Comparações | Trocas/Movimentações |
| --------------------- | -------------- | ----------: | -------------------: |
| Aleatório             | Bubble Sort    |     499.329 |              238.336 |
| Aleatório             | Insertion Sort |     239.334 |              239.335 |
| Aleatório             | Selection Sort |     499.500 |                  968 |
| Aleatório             | Quick Sort     |      11.564 |                3.023 |
| Já ordenado           | Bubble Sort    |         999 |                    0 |
| Já ordenado           | Insertion Sort |         999 |                  999 |
| Já ordenado           | Selection Sort |     499.500 |                    0 |
| Já ordenado           | Quick Sort     |       9.909 |                1.758 |
| Inversamente ordenado | Bubble Sort    |     499.347 |              488.860 |
| Inversamente ordenado | Insertion Sort |     489.813 |              489.859 |
| Inversamente ordenado | Selection Sort |     499.500 |                  668 |
| Inversamente ordenado | Quick Sort     |       9.914 |                2.258 |

---

## 3. Análise

### 3.1 Vetor aleatório

No vetor aleatório, os resultados apresentaram um comportamento intermediário entre os outros dois cenários.

Para 1.000 elementos, o Bubble Sort realizou 499.329 comparações, o Insertion Sort realizou 239.334 e o Selection Sort realizou 499.500.

O Quick Sort apresentou o melhor resultado, com apenas 11.564 comparações e 3.023 movimentações.

---

### 3.2 Vetor já ordenado

O vetor já ordenado beneficiou principalmente o Bubble Sort e o Insertion Sort.

Com 1.000 elementos, o Bubble Sort realizou apenas 999 comparações e nenhuma troca. Isso aconteceu porque o algoritmo possui uma condição que identifica quando não ocorreu nenhuma troca e encerra a execução.

O Insertion Sort também realizou somente 999 comparações, embora tenha contabilizado 999 movimentações referentes à inserção das chaves.

O Selection Sort continuou realizando 499.500 comparações, mesmo com o vetor já ordenado, pois sua estrutura percorre os elementos restantes para procurar o menor valor.

O Quick Sort realizou 9.909 comparações e 1.758 movimentações.

---

### 3.3 Vetor inversamente ordenado

O vetor inversamente ordenado foi um dos cenários mais desfavoráveis para Bubble Sort e Insertion Sort.

Com 1.000 elementos, o Bubble Sort realizou 499.347 comparações e 488.860 trocas.

O Insertion Sort realizou 489.813 comparações e 489.859 movimentações.

O Selection Sort realizou 499.500 comparações, mas apenas 668 trocas.

O Quick Sort continuou apresentando uma quantidade muito menor de operações, com 9.914 comparações e 2.258 movimentações.

---

## 4. A organização inicial influencia todos os algoritmos da mesma forma?

Não.

Os resultados mostram que a organização inicial do vetor influencia os algoritmos de maneiras diferentes.

O Bubble Sort foi bastante beneficiado pelo vetor já ordenado, realizando somente 999 comparações e nenhuma troca com 1.000 elementos. Porém, no vetor inversamente ordenado, realizou 488.860 trocas.

O Insertion Sort apresentou comportamento semelhante: foi muito eficiente com o vetor já ordenado e apresentou grande quantidade de movimentações no vetor inversamente ordenado.

O Selection Sort apresentou uma quantidade de comparações praticamente independente da organização inicial. Nos três cenários com 1.000 elementos, foram realizadas exatamente 499.500 comparações. Entretanto, a quantidade de trocas foi diferente.

O Quick Sort apresentou pequenas diferenças entre os cenários e permaneceu muito mais eficiente que os algoritmos quadráticos nos testes com 1.000 elementos.

---

## 5. Conclusão do desafio

O experimento demonstrou que a organização inicial dos dados pode influenciar significativamente o desempenho de alguns algoritmos de ordenação.

Bubble Sort e Insertion Sort foram os algoritmos que apresentaram maior diferença entre os cenários. Eles tiveram desempenho muito melhor quando o vetor já estava ordenado e apresentaram grande quantidade de operações quando o vetor estava inversamente ordenado.

O Selection Sort manteve praticamente a mesma quantidade de comparações nos diferentes cenários, demonstrando que sua quantidade de comparações depende principalmente do tamanho do vetor.

O Quick Sort apresentou o melhor comportamento geral para os vetores de 1.000 elementos, mantendo uma quantidade de operações muito menor nos três cenários analisados.

Portanto, os resultados confirmam que não basta analisar somente a complexidade teórica de um algoritmo. A organização inicial dos dados também pode influenciar seu comportamento prático, principalmente em algoritmos como Bubble Sort e Insertion Sort.
