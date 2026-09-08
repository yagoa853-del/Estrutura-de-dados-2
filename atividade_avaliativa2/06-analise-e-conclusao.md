# PARTE 6 – ANÁLISE E CONCLUSÃO

## 1. Resultados do experimento de ordenação

Os testes foram realizados utilizando os algoritmos Bubble Sort e Quick Sort sobre os mesmos conjuntos de dados.

Foram utilizados arrays com 10, 20 e 1.000 elementos, contendo valores inteiros gerados aleatoriamente entre 1 e 47.

Os resultados obtidos devem ser registrados na tabela abaixo após a execução do programa `02-experimento-ordenacao.py`.

| Tamanho do array | Bubble Comparações | Bubble Trocas | Quick Comparações | Quick Movimentações |
|---:|---:|---:|---:|---:|
| 10 | PREENCHER | PREENCHER | PREENCHER | PREENCHER |
| 20 | PREENCHER | PREENCHER | PREENCHER | PREENCHER |
| 1.000 | PREENCHER | PREENCHER | PREENCHER | PREENCHER |

> Os valores da tabela devem ser preenchidos com os resultados reais apresentados pelo programa.

### Análise

O Bubble Sort realiza uma quantidade elevada de comparações porque percorre repetidamente o array, comparando elementos vizinhos.

O Quick Sort utiliza uma estratégia baseada na escolha de um pivô e na divisão do problema em partes menores.

Nos arrays menores, como 10 e 20 elementos, a diferença entre os algoritmos pode ser menos significativa. Entretanto, com 1.000 elementos, a diferença na quantidade de operações tende a ficar muito mais evidente.

O crescimento teórico do Bubble Sort é O(n²) no caso médio e no pior caso. O Quick Sort apresenta complexidade média de O(n log n), embora seu pior caso possa chegar a O(n²).

---

## 2. Tabela da busca em matrizes

A busca sequencial foi realizada utilizando matrizes de 2×2, 10×10 e 100×100.

Foram testadas três situações:

- valor localizado no início da matriz;
- valor localizado próximo ao final da matriz;
- valor inexistente.

Os resultados foram:

| Matriz | Quantidade de elementos | Início | Próximo ao final | Inexistente |
|---|---:|---:|---:|---:|
| 2×2 | 4 | 1 | 3 | 4 |
| 10×10 | 100 | 1 | 99 | 100 |
| 100×100 | 10.000 | 1 | 9.999 | 10.000 |

### Análise

Quando o valor está no início da matriz, a busca encontra o elemento na primeira comparação.

Quando o valor está próximo ao final, praticamente toda a matriz precisa ser percorrida antes que o elemento seja encontrado.

Quando o valor não existe, todos os elementos da matriz precisam ser comparados.

Portanto, no pior caso, uma matriz com m linhas e n colunas exige até m × n comparações.

A complexidade da busca sequencial em uma matriz é:

**O(m × n)**

---

## 3. Influência do tamanho da estrutura

Os experimentos demonstraram que o tamanho da entrada influencia diretamente a quantidade de operações realizadas.

No Bubble Sort, o crescimento das operações ocorre de maneira aproximadamente quadrática.

No Quick Sort, o crescimento médio é O(n log n), fazendo com que o algoritmo seja geralmente mais adequado para conjuntos maiores de dados.

Na busca sequencial em matrizes, o número máximo de comparações corresponde à quantidade total de posições da matriz.

Assim, uma matriz 100×100 possui 10.000 posições e pode exigir até 10.000 comparações em uma busca sequencial.

---

## 4. Comparação entre Bubble Sort e Quick Sort

Os dois algoritmos são capazes de ordenar os mesmos dados e produzir o mesmo resultado final.

A principal diferença está na estratégia utilizada.

O Bubble Sort compara elementos adjacentes e realiza trocas sucessivas.

O Quick Sort escolhe um pivô e divide o array em partes menores para realizar a ordenação.

| Característica | Bubble Sort | Quick Sort |
|---|---|---|
| Princípio | Comparação e troca de elementos vizinhos | Divisão utilizando um pivô |
| Melhor caso | O(n), com otimização | O(n log n) |
| Caso médio | O(n²) | O(n log n) |
| Pior caso | O(n²) | O(n²) |
| Memória | O(1) auxiliar | O(log n) em média |
| Principal vantagem | Simplicidade | Maior eficiência média |
| Principal limitação | Baixa eficiência em grandes arrays | Pode atingir O(n²) em determinadas situações |

---

## 5. Por que o resultado final não é suficiente?

Observar apenas o resultado final não é suficiente para avaliar um algoritmo.

Dois algoritmos podem receber exatamente os mesmos dados e produzir exatamente a mesma saída, mas realizar quantidades diferentes de comparações, trocas e movimentações.

Por isso, a análise de algoritmos deve considerar também a quantidade de operações necessárias para produzir o resultado.

Essa análise permite compreender melhor o desempenho e a eficiência de cada algoritmo.

---

## 6. Hands On 1 – Array de temperaturas

O programa `04-array-temperaturas.py` utiliza um array para armazenar 10 valores de temperatura.

O programa realiza as seguintes operações:

- recebe 10 temperaturas;
- armazena os valores;
- exibe todas as temperaturas;
- calcula a média;
- identifica a maior temperatura;
- identifica a menor temperatura;
- identifica os índices dos valores maior e menor;
- conta quantas temperaturas estão acima da média.

O percurso do array é realizado utilizando estruturas de repetição.

A complexidade das operações de percurso é O(n), pois o número de operações cresce proporcionalmente à quantidade de temperaturas armazenadas.

---

## 7. Hands On 2 – Monitoramento de sensores

O programa `05-monitoramento-sensores.py` utiliza uma matriz para representar cinco sensores durante 24 horas.

A estrutura possui:

**5 × 24 = 120 posições**

O primeiro índice representa o sensor e o segundo representa o horário.

Por exemplo:

- `[0][0]` representa o sensor 0 na hora 0;
- `[2][10]` representa o sensor 2 na hora 10;
- `[4][23]` representa o sensor 4 na hora 23.

O programa calcula:

- média de cada sensor;
- maior temperatura registrada;
- sensor responsável pela maior temperatura;
- horário da maior temperatura;
- média geral;
- quantidade de leituras acima de um limite informado.

Como são utilizadas duas dimensões, são necessários loops aninhados para percorrer todos os elementos.

A complexidade dos percursos é O(m × n).

---

## 8. Conclusão

Os experimentos permitiram observar na prática a relação entre o tamanho da entrada, a quantidade de operações e a complexidade dos algoritmos.

O Bubble Sort apresentou uma implementação simples e fácil de compreender, porém seu crescimento quadrático de operações faz com que seja pouco adequado para grandes conjuntos de dados.

O Quick Sort apresentou uma estratégia mais eficiente em média, principalmente para conjuntos maiores, devido à sua complexidade média O(n log n).

A busca sequencial em matrizes demonstrou que a posição do elemento influencia diretamente a quantidade de comparações. Quando o elemento está no início, poucas comparações são necessárias. Quando está próximo do final ou não existe, praticamente toda a matriz precisa ser percorrida.

Os Hands On também demonstraram a aplicação prática de arrays e matrizes. O array de temperaturas permitiu trabalhar com armazenamento, média, valores máximo e mínimo e índices. Já a matriz de sensores mostrou como estruturas bidimensionais podem representar informações organizadas em linhas e colunas.

Conclui-se que o tamanho da entrada possui influência significativa no desempenho dos algoritmos. Por isso, não é suficiente verificar apenas se um programa produz o resultado correto. Também é importante analisar a quantidade de operações realizadas e como essa quantidade cresce conforme o volume de dados aumenta.
