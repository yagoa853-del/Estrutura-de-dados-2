# PARTE 1 – PESQUISA: BUBBLE SORT E QUICK SORT

## 1. Introdução

Os algoritmos de ordenação são utilizados para organizar elementos de uma estrutura de dados de acordo com determinado critério, como ordem crescente ou decrescente. A escolha do algoritmo pode influenciar diretamente a quantidade de operações necessárias e, consequentemente, o desempenho de um programa.

Nesta pesquisa serão analisados dois algoritmos de ordenação: **Bubble Sort** e **Quick Sort**. Embora ambos possam produzir o mesmo resultado final, suas estratégias de funcionamento e suas complexidades computacionais são diferentes.

---

# 2. Bubble Sort

## 2.1 Como o algoritmo funciona

O **Bubble Sort** é um algoritmo de ordenação baseado na comparação de elementos vizinhos.

O algoritmo percorre a estrutura comparando cada elemento com o elemento imediatamente seguinte. Quando os elementos estão na ordem incorreta, eles são trocados.

Esse processo é repetido várias vezes até que todos os elementos estejam ordenados.

O nome "Bubble Sort" está relacionado à ideia de que os maiores elementos vão sendo deslocados gradualmente para o final da estrutura durante as sucessivas passagens.

Por exemplo, considerando o array:

```text
[5, 2, 8, 1]
```

Na primeira comparação:

```text
5 > 2
```

Os elementos são trocados:

```text
[2, 5, 8, 1]
```

Depois:

```text
5 < 8
```

Não ocorre troca.

Em seguida:

```text
8 > 1
```

Os elementos são trocados:

```text
[2, 5, 1, 8]
```

Após novas passagens, o array finalmente ficará:

```text
[1, 2, 5, 8]
```

## 2.2 Lógica de ordenação

A lógica do Bubble Sort pode ser resumida da seguinte maneira:

1. Percorrer o array.
2. Comparar dois elementos consecutivos.
3. Verificar se estão na ordem correta.
4. Caso estejam fora de ordem, realizar uma troca.
5. Continuar o percurso até o final do array.
6. Repetir o processo até que os elementos estejam ordenados.

A cada passagem, um dos maiores elementos da parte ainda não ordenada é colocado em sua posição definitiva.

## 2.3 Complexidade

### Melhor caso

O melhor caso ocorre quando os elementos já estão ordenados.

Em uma implementação otimizada, capaz de detectar que nenhuma troca foi realizada durante uma passagem, a complexidade pode ser:

**O(n)**

Porém, em uma implementação sem essa otimização, o algoritmo continua realizando as comparações das passagens e pode apresentar:

**O(n²)**

### Caso médio

No caso médio, o Bubble Sort apresenta complexidade:

**O(n²)**

Isso acontece porque, em geral, são necessárias diversas passagens e comparações para organizar os elementos.

### Pior caso

O pior caso ocorre quando os elementos estão organizados em ordem inversa.

Nesse cenário, uma grande quantidade de comparações e trocas será necessária.

A complexidade é:

**O(n²)**

---

## 2.4 Vantagens

As principais vantagens do Bubble Sort são:

* É simples de compreender.
* Possui implementação relativamente fácil.
* É útil para fins educacionais.
* Utiliza pouca memória adicional.
* Pode ser utilizado em conjuntos muito pequenos de dados.
* Permite visualizar facilmente o processo de ordenação.

## 2.5 Limitações

As principais limitações são:

* Possui baixo desempenho para grandes quantidades de elementos.
* Realiza muitas comparações.
* Pode realizar uma grande quantidade de trocas.
* Sua complexidade média e de pior caso é O(n²).
* Existem algoritmos mais eficientes para grandes conjuntos de dados.

## 2.6 Situações em que seu uso é adequado

O Bubble Sort pode ser adequado:

* Para fins didáticos.
* Para demonstrar conceitos de ordenação.
* Para arrays muito pequenos.
* Quando a simplicidade da implementação é mais importante que o desempenho.
* Em situações em que a quantidade de dados é pequena.

## 2.7 Situações em que seu uso não é recomendado

O Bubble Sort não é recomendado:

* Para grandes conjuntos de dados.
* Em sistemas que exigem alto desempenho.
* Quando a quantidade de operações precisa ser reduzida.
* Em aplicações em que existem algoritmos mais eficientes disponíveis.

---

# 3. Quick Sort

## 3.1 Como o algoritmo funciona

O **Quick Sort** é um algoritmo de ordenação baseado na estratégia de **dividir para conquistar**.

O algoritmo seleciona um elemento do array como **pivô** e reorganiza os demais elementos de acordo com esse pivô.

Os elementos menores que o pivô são posicionados de um lado, enquanto os elementos maiores são posicionados do outro.

Depois disso, o mesmo processo é aplicado às partes menores do array.

Esse processo continua até que todas as partes estejam ordenadas.

## 3.2 Lógica de ordenação

A lógica básica do Quick Sort pode ser descrita da seguinte maneira:

1. Escolher um elemento como pivô.
2. Percorrer os elementos da estrutura.
3. Separar os elementos menores que o pivô dos elementos maiores.
4. Colocar o pivô entre essas duas partes.
5. Aplicar novamente o processo à parte esquerda.
6. Aplicar novamente o processo à parte direita.
7. Continuar até que as partes estejam suficientemente pequenas para serem consideradas ordenadas.

Por exemplo:

```text
[8, 3, 7, 4, 2, 9]
```

Supondo que o pivô escolhido seja:

```text
7
```

Podemos dividir os elementos em:

```text
Menores que 7: [3, 4, 2]

Pivô: [7]

Maiores que 7: [8, 9]
```

O algoritmo então continua ordenando as partes menores.

Ao final:

```text
[2, 3, 4, 7, 8, 9]
```

## 3.3 Complexidade

### Melhor caso

O melhor caso ocorre quando o pivô divide o array em partes aproximadamente iguais.

Nesse cenário, a complexidade é:

**O(n log n)**

### Caso médio

No caso médio, o Quick Sort apresenta:

**O(n log n)**

Por isso, geralmente apresenta desempenho significativamente melhor que o Bubble Sort para grandes conjuntos de dados.

### Pior caso

O pior caso ocorre quando as divisões geradas pelo pivô são muito desequilibradas.

Por exemplo, se o pivô escolhido for repetidamente o menor ou o maior elemento da parte analisada, uma das partes ficará praticamente vazia e a outra conterá quase todos os elementos.

Nesse cenário, a complexidade pode chegar a:

**O(n²)**

---

## 3.4 Vantagens

As principais vantagens do Quick Sort são:

* Apresenta excelente desempenho médio.
* Possui complexidade média O(n log n).
* É geralmente mais eficiente que o Bubble Sort para grandes conjuntos de dados.
* Utiliza a estratégia de dividir para conquistar.
* É bastante utilizado como referência no estudo de algoritmos de ordenação.

## 3.5 Limitações

As principais limitações são:

* Pode apresentar complexidade O(n²) no pior caso.
* O desempenho depende da escolha do pivô.
* Sua implementação é mais complexa que a do Bubble Sort.
* A implementação normalmente utiliza recursão.
* Uma escolha inadequada do pivô pode gerar divisões muito desequilibradas.

## 3.6 Situações em que seu uso é adequado

O Quick Sort pode ser adequado:

* Para grandes conjuntos de dados.
* Quando é necessário realizar uma ordenação de forma eficiente.
* Quando o desempenho médio é importante.
* Em aplicações que trabalham com arrays ou listas grandes.
* Em situações em que a estratégia de dividir para conquistar é vantajosa.

## 3.7 Situações em que seu uso não é recomendado

O Quick Sort pode não ser a melhor escolha:

* Quando é necessário garantir O(n log n) no pior caso.
* Quando a implementação precisa ser extremamente simples.
* Quando a quantidade de elementos é muito pequena e a simplicidade de um algoritmo como o Bubble Sort é suficiente.
* Quando a estratégia de escolha do pivô não for adequada ao conjunto de dados.

---

# 4. Tabela Comparativa

| Característica                 | Bubble Sort                                                               | Quick Sort                                                                                      |
| ------------------------------ | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Princípio de funcionamento** | Compara elementos adjacentes e realiza trocas quando estão fora de ordem. | Escolhe um pivô e divide os elementos em partes menores e maiores, ordenando-as recursivamente. |
| **Melhor caso**                | O(n) com otimização; O(n²) sem otimização de parada.                      | O(n log n)                                                                                      |
| **Caso médio**                 | O(n²)                                                                     | O(n log n)                                                                                      |
| **Pior caso**                  | O(n²)                                                                     | O(n²)                                                                                           |
| **Uso de memória**             | O(1) de memória auxiliar em implementação iterativa.                      | O(log n) de espaço de pilha no caso médio, podendo chegar a O(n) no pior caso.                  |
| **Vantagem principal**         | Simplicidade de implementação e compreensão.                              | Maior eficiência média para grandes conjuntos de dados.                                         |
| **Limitação principal**        | Baixo desempenho para grandes quantidades de elementos.                   | Pode atingir O(n²) dependendo da escolha do pivô.                                               |
| **Aplicação recomendada**      | Pequenos conjuntos de dados e situações educacionais.                     | Grandes conjuntos de dados e aplicações que exigem maior eficiência.                            |
| **Aplicação não recomendada**  | Grandes volumes de dados e sistemas que exigem alto desempenho.           | Situações que exigem garantia de O(n log n) no pior caso sem estratégias adicionais.            |

---

# 5. Comparação Geral

Embora os dois algoritmos tenham o mesmo objetivo — ordenar os elementos —, eles utilizam estratégias diferentes.

O Bubble Sort compara elementos vizinhos e realiza trocas sucessivas. Já o Quick Sort utiliza um pivô para dividir o problema em partes menores.

Essa diferença faz com que o crescimento da quantidade de operações seja bastante diferente entre os dois algoritmos.

Enquanto o Bubble Sort apresenta complexidade O(n²) no caso médio, o Quick Sort apresenta O(n log n) no caso médio.

Portanto, conforme o tamanho da entrada aumenta, a diferença de eficiência tende a ficar cada vez mais significativa.

---

# 6. Conclusão da Parte 1

O Bubble Sort e o Quick Sort são algoritmos capazes de ordenar uma estrutura de dados, mas apresentam diferenças importantes em relação à quantidade de operações necessárias.

O Bubble Sort possui uma lógica simples e fácil de compreender, porém apresenta complexidade O(n²) no caso médio e no pior caso. Isso faz com que sua eficiência diminua significativamente conforme o número de elementos aumenta.

O Quick Sort utiliza a estratégia de dividir para conquistar e apresenta complexidade média O(n log n), sendo normalmente mais eficiente para grandes conjuntos de dados. Entretanto, seu pior caso pode chegar a O(n²), principalmente quando a escolha do pivô produz divisões muito desequilibradas.

Assim, a escolha do algoritmo deve considerar o tamanho dos dados, o desempenho esperado e as características do problema. Nas próximas etapas da atividade, essa diferença será investigada experimentalmente utilizando arrays com diferentes quantidades de elementos e contabilizando as operações realizadas pelos algoritmos.
