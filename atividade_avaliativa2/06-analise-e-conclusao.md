## 1. Resultados do experimento de ordenação

Os testes foram realizados utilizando os algoritmos Bubble Sort e Quick Sort sobre os mesmos conjuntos de dados.

Foram utilizados arrays com 10, 20 e 1.000 elementos, contendo valores inteiros gerados aleatoriamente entre 1 e 47.

Os resultados obtidos foram:

| Tamanho do array | Bubble Comparações | Bubble Trocas | Quick Comparações | Quick Movimentações |
|---:|---:|---:|---:|---:|
| 10 | 45 | 26 | 32 | 24 |
| 20 | 190 | 85 | 88 | 51 |
| 1.000 | 499.500 | 245.620 | 11.802 | 9.066 |

### Análise dos resultados

No array com 10 elementos, o Bubble Sort realizou 45 comparações e 26 trocas, enquanto o Quick Sort realizou 32 comparações e 24 movimentações.

Com 20 elementos, o Bubble Sort realizou 190 comparações e 85 trocas. O Quick Sort realizou 88 comparações e 51 movimentações.

A diferença torna-se muito mais significativa no teste com 1.000 elementos. O Bubble Sort realizou 499.500 comparações e 245.620 trocas, enquanto o Quick Sort realizou apenas 11.802 comparações e 9.066 movimentações.

Os resultados demonstram que o Quick Sort apresentou melhor desempenho em quantidade de operações nos três testes realizados.

No caso do Bubble Sort, o número de comparações aumentou de 45, com 10 elementos, para 190, com 20 elementos, e chegou a 499.500 com 1.000 elementos. Esse crescimento demonstra o comportamento quadrático do algoritmo.

O Quick Sort também apresentou aumento na quantidade de operações conforme o tamanho do array aumentou, porém esse crescimento foi significativamente menor. Isso está de acordo com sua complexidade média O(n log n).

Os dois algoritmos produziram o mesmo resultado final nos testes, ou seja, os arrays foram corretamente ordenados em ordem crescente.

Portanto, os resultados experimentais são coerentes com a análise teórica das complexidades dos algoritmos. O Bubble Sort apresenta uma implementação mais simples, mas possui desempenho inferior para grandes quantidades de dados. O Quick Sort, por sua vez, apresenta maior eficiência média e é mais adequado para conjuntos maiores.
