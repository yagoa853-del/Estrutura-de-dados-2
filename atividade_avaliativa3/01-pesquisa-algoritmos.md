# ETAPA 1 – PESQUISA SOBRE ALGORITMOS DE ORDENAÇÃO

## 1. Introdução

Algoritmos de ordenação são utilizados para organizar conjuntos de dados de acordo com determinado critério. Neste trabalho, será considerada a ordenação de códigos numéricos de prioridade de pedidos em ordem crescente.

Serão analisados quatro algoritmos de ordenação:

- Bubble Sort;
- Insertion Sort;
- Selection Sort;
- Quick Sort.

O objetivo é compreender o funcionamento de cada algoritmo, suas complexidades, vantagens e limitações, além de posteriormente comparar seu comportamento experimentalmente.

---

## 2. Bubble Sort

### 2.1 Funcionamento

O Bubble Sort é um algoritmo de ordenação baseado na comparação entre elementos vizinhos.

Durante cada passagem pelo vetor, elementos consecutivos são comparados. Quando estão fora de ordem, eles são trocados de posição.

Após cada passagem, um dos maiores elementos tende a chegar à sua posição correta no final da parte ainda não ordenada do vetor.

O processo é repetido até que todos os elementos estejam ordenados.

### 2.2 Lógica de ordenação

Considerando um vetor em ordem crescente:

1. O algoritmo compara dois elementos vizinhos.
2. Se o elemento da esquerda for maior que o da direita, eles são trocados.
3. O algoritmo continua percorrendo o vetor.
4. Ao final da passagem, o maior elemento da parte não ordenada estará em sua posição.
5. As passagens continuam até que todo o vetor esteja ordenado.

### 2.3 Complexidade

- Melhor caso: O(n), quando implementado com verificação de ausência de trocas.
- Caso médio: O(n²).
- Pior caso: O(n²).

### 2.4 Vantagens

- Implementação simples.
- Fácil compreensão.
- Não necessita de estruturas auxiliares significativas.
- Pode apresentar bom comportamento em vetores pequenos ou quase ordenados quando possui otimização.

### 2.5 Limitações

- Apresenta baixo desempenho para grandes conjuntos de dados.
- Realiza muitas comparações e trocas.
- Não é uma boa escolha para grandes volumes de dados.

### 2.6 Aplicações

Pode ser utilizado principalmente para fins didáticos, testes ou situações em que o conjunto de dados seja pequeno.

---

## 3. Insertion Sort

### 3.1 Funcionamento

O Insertion Sort organiza os elementos gradualmente, considerando uma parte do vetor como ordenada e inserindo cada novo elemento na posição correta.

O algoritmo começa pelo segundo elemento e o compara com os elementos anteriores. Os elementos maiores são deslocados para abrir espaço para o elemento que está sendo inserido.

### 3.2 Lógica de ordenação

Considerando um vetor em ordem crescente:

1. O primeiro elemento é considerado inicialmente ordenado.
2. O próximo elemento é selecionado.
3. Ele é comparado com os elementos da parte ordenada.
4. Os elementos maiores são deslocados uma posição para a direita.
5. O elemento selecionado é inserido na posição correta.
6. O processo continua até o final do vetor.

### 3.3 Complexidade

- Melhor caso: O(n), quando o vetor já está ordenado.
- Caso médio: O(n²).
- Pior caso: O(n²), principalmente quando o vetor está em ordem inversa.

### 3.4 Vantagens

- Implementação simples.
- Bom desempenho para vetores pequenos.
- Apresenta bom comportamento quando os dados já estão ou estão quase ordenados.
- Não necessita de grande quantidade de memória adicional.

### 3.5 Limitações

- Pode realizar muitos deslocamentos em grandes conjuntos de dados.
- Seu caso médio apresenta complexidade O(n²).
- Pode ser ineficiente para grandes volumes de dados desordenados.

### 3.6 Aplicações

É adequado para conjuntos pequenos, dados quase ordenados e situações em que os elementos chegam gradualmente e precisam ser inseridos em uma sequência ordenada.

---

## 4. Selection Sort

### 4.1 Funcionamento

O Selection Sort divide o vetor em duas partes: uma parte já ordenada e outra ainda não ordenada.

A cada etapa, o algoritmo procura o menor elemento da parte não ordenada e o coloca na próxima posição da parte ordenada.

### 4.2 Lógica de ordenação

Considerando um vetor em ordem crescente:

1. O algoritmo procura o menor elemento de todo o vetor.
2. O menor elemento é colocado na primeira posição.
3. A primeira posição passa a fazer parte da região ordenada.
4. O algoritmo procura o menor elemento restante.
5. Esse elemento é colocado na próxima posição.
6. O processo continua até que todo o vetor esteja ordenado.

### 4.3 Complexidade

- Melhor caso: O(n²).
- Caso médio: O(n²).
- Pior caso: O(n²).

Uma característica importante é que o Selection Sort continua realizando muitas comparações mesmo quando os dados já estão ordenados.

### 4.4 Vantagens

- Implementação simples.
- Utiliza pouca memória adicional.
- Realiza poucas trocas em comparação com alguns outros algoritmos de ordenação.

### 4.5 Limitações

- Realiza O(n²) comparações.
- Não aproveita de forma significativa o fato de o vetor já estar ordenado.
- Não é indicado para grandes conjuntos de dados.

### 4.6 Aplicações

Pode ser utilizado em situações com conjuntos pequenos ou em contextos educacionais para demonstrar conceitos de ordenação e seleção de elementos.

---

## 5. Quick Sort

### 5.1 Funcionamento

O Quick Sort utiliza uma estratégia de divisão e conquista.

O algoritmo escolhe um elemento chamado pivô e reorganiza o vetor de forma que os elementos menores que o pivô fiquem de um lado e os maiores fiquem do outro.

Depois disso, o mesmo processo é aplicado às partes menores do vetor.

### 5.2 Lógica de ordenação

Considerando um vetor em ordem crescente:

1. Um elemento é escolhido como pivô.
2. O vetor é dividido em relação ao pivô.
3. Elementos menores ficam à esquerda.
4. Elementos maiores ficam à direita.
5. O processo é repetido nas partes menores.
6. Quando as partes possuem tamanho suficientemente pequeno, a ordenação está concluída.

### 5.3 Complexidade

- Melhor caso: O(n log n).
- Caso médio: O(n log n).
- Pior caso: O(n²).

O pior caso pode ocorrer dependendo da escolha do pivô e da organização dos dados.

### 5.4 Vantagens

- Geralmente apresenta bom desempenho.
- É eficiente para grandes conjuntos de dados.
- Possui complexidade média O(n log n).
- Utiliza a estratégia de divisão e conquista.

### 5.5 Limitações

- Pode apresentar O(n²) no pior caso.
- Seu desempenho depende da escolha do pivô.
- A implementação é mais complexa que a de algoritmos como Bubble Sort, Insertion Sort e Selection Sort.

### 5.6 Aplicações

É adequado para grandes conjuntos de dados e situações em que seja necessário realizar ordenações de forma eficiente.

---

## 6. Comparação entre os algoritmos

| Característica | Bubble Sort | Insertion Sort | Selection Sort | Quick Sort |
|---|---|---|---|---|
| Estratégia | Comparações e trocas | Inserção e deslocamento | Seleção do menor elemento | Divisão e conquista |
| Melhor caso | O(n)¹ | O(n) | O(n²) | O(n log n) |
| Caso médio | O(n²) | O(n²) | O(n²) | O(n log n) |
| Pior caso | O(n²) | O(n²) | O(n²) | O(n²) |
| Memória auxiliar | O(1) | O(1) | O(1) | O(log n) em média |
| Principal vantagem | Simplicidade | Bom para dados quase ordenados | Poucas trocas | Bom desempenho médio |
| Principal limitação | Muitas operações | Muitos deslocamentos | Muitas comparações | Pode atingir O(n²) |

¹ No Bubble Sort, O(n) no melhor caso considera uma implementação otimizada que encerra o algoritmo quando nenhuma troca é realizada.

---

## 7. Comparação geral

Bubble Sort, Insertion Sort e Selection Sort possuem complexidade O(n²) no caso médio, porém isso não significa que eles realizarão exatamente a mesma quantidade de operações.

Cada algoritmo possui uma estratégia diferente.

O Bubble Sort realiza comparações entre elementos vizinhos e pode realizar diversas trocas.

O Insertion Sort utiliza deslocamentos para inserir cada elemento em sua posição correta.

O Selection Sort procura o menor elemento da parte não ordenada e realiza trocas para posicioná-lo.

O Quick Sort utiliza um pivô para dividir o problema em partes menores e apresenta complexidade média O(n log n).

Por esse motivo, espera-se que o Quick Sort apresente melhor desempenho para conjuntos maiores de dados.

Entretanto, os resultados experimentais serão necessários para verificar como cada algoritmo se comportará nos vetores de 10, 20 e 1.000 elementos.

---

## 8. Conclusão da pesquisa

Os quatro algoritmos são capazes de ordenar os mesmos dados, mas utilizam estratégias diferentes.

Os algoritmos Bubble Sort, Insertion Sort e Selection Sort são relativamente simples de implementar, porém apresentam limitações de desempenho quando aplicados a grandes volumes de dados.

O Insertion Sort pode apresentar vantagem quando os dados estão quase ordenados, enquanto o Selection Sort possui como característica a realização de poucas trocas.

O Bubble Sort destaca-se principalmente pela simplicidade de sua lógica.

O Quick Sort apresenta maior eficiência média e tende a ser mais adequado para grandes conjuntos de dados, embora seu pior caso possa apresentar complexidade O(n²).

Na próxima etapa, os quatro algoritmos serão implementados em Python e submetidos aos mesmos conjuntos de dados para que a quantidade de comparações e trocas ou movimentações possa ser analisada experimentalmente.
