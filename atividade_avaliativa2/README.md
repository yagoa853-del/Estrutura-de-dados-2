# 📚 Atividade Avaliativa – Estruturas de Dados

## 📌 Sobre a atividade

Este repositório contém o desenvolvimento da **Atividade Avaliativa de Estruturas de Dados**, envolvendo arrays, matrizes, algoritmos de ordenação, algoritmos de busca, índices, loops e análise de complexidade computacional.

O principal objetivo da atividade é investigar, de forma prática, como diferentes algoritmos se comportam conforme aumenta o tamanho da quantidade de dados, relacionando:

**Tamanho da entrada → Número de operações → Complexidade → Eficiência**

---

## 🎯 Objetivos

* Compreender o funcionamento do **Bubble Sort**;
* Compreender o funcionamento do **Quick Sort**;
* Comparar diferentes algoritmos de ordenação;
* Contabilizar comparações, trocas e movimentações;
* Analisar o comportamento dos algoritmos com diferentes tamanhos de arrays;
* Implementar busca sequencial em matrizes;
* Investigar a quantidade de comparações realizadas durante uma busca;
* Trabalhar com arrays e matrizes em Python;
* Aplicar loops e índices em estruturas de dados;
* Relacionar os resultados experimentais com a complexidade computacional.

---

## 🧩 Etapas da atividade

### 1️⃣ Pesquisa – Bubble Sort e Quick Sort

Nesta etapa são apresentados:

* Funcionamento do Bubble Sort;
* Funcionamento do Quick Sort;
* Lógica de ordenação;
* Complexidade no melhor caso;
* Complexidade no caso médio;
* Complexidade no pior caso;
* Vantagens;
* Limitações;
* Aplicações recomendadas;
* Situações em que os algoritmos não são recomendados;
* Comparação entre os dois algoritmos.

📄 Arquivo:

`01-pesquisa-bubble-sort-quick-sort.md`

---

### 2️⃣ Experimento de Ordenação

Nesta etapa são realizados experimentos utilizando os algoritmos **Bubble Sort** e **Quick Sort**.

São utilizados arrays contendo:

* 10 elementos;
* 20 elementos;
* 1.000 elementos.

Os números são gerados aleatoriamente no intervalo de **1 a 47**.

Os mesmos dados são utilizados nos dois algoritmos para permitir uma comparação justa.

São contabilizados:

* Comparações;
* Trocas do Bubble Sort;
* Movimentações do Quick Sort.

📄 Arquivo:

`02-experimento-ordenacao.py`

### Resultados obtidos

| Tamanho do array | Bubble Comparações | Bubble Trocas | Quick Comparações | Quick Movimentações |
| ---------------: | -----------------: | ------------: | ----------------: | ------------------: |
|               10 |                 45 |            26 |                32 |                  24 |
|               20 |                190 |            85 |                88 |                  51 |
|            1.000 |            499.500 |       245.620 |            11.802 |               9.066 |

Os resultados mostram que o Quick Sort realizou significativamente menos operações no experimento, principalmente quando o tamanho do array aumentou.

---

### 3️⃣ Investigação de Busca em Matrizes

Nesta etapa é implementado um algoritmo de **busca sequencial em matrizes utilizando loops aninhados**.

São realizados testes com:

* Matriz 2 × 2;
* Matriz 10 × 10;
* Matriz 100 × 100.

Para cada matriz são analisadas três situações:

* Valor localizado no início;
* Valor localizado próximo ao final;
* Valor inexistente.

📄 Arquivo:

`03-busca-matrizes.py`

### Resultados

| Matriz    | Elementos | Início | Próximo ao final | Inexistente |
| --------- | --------: | -----: | ---------------: | ----------: |
| 2 × 2     |         4 |      1 |                3 |           4 |
| 10 × 10   |       100 |      1 |               99 |         100 |
| 100 × 100 |    10.000 |      1 |            9.999 |      10.000 |

A busca sequencial apresenta complexidade **O(m × n)** para uma matriz com `m` linhas e `n` colunas.

---

### 4️⃣ Hands On 1 – Investigação do Array

Nesta etapa é utilizado um array para armazenar **10 temperaturas**.

O programa realiza:

* Entrada das temperaturas;
* Exibição dos elementos;
* Cálculo da média;
* Identificação do maior valor;
* Identificação do menor valor;
* Identificação do índice do maior valor;
* Identificação do índice do menor valor;
* Contagem dos valores acima da média;
* Estimativa das operações de percurso.

📄 Arquivo:

`04-array-temperaturas.py`

A complexidade das operações de percurso é **O(n)**.

---

### 5️⃣ Hands On 2 – Monitoramento de Sensores

Nesta etapa é utilizada uma matriz para representar um sistema com:

* **5 sensores**;
* **24 medições por sensor**;
* **120 medições no total**.

A estrutura utilizada representa:

```text
5 × 24 = 120 posições
```

O programa calcula:

* Média de cada sensor;
* Maior temperatura registrada;
* Sensor responsável pelo maior valor;
* Horário da ocorrência;
* Média geral;
* Quantidade de leituras acima de um limite informado.

📄 Arquivo:

`05-monitoramento-sensores.py`

A matriz é percorrida utilizando loops aninhados e sua complexidade de percurso é **O(m × n)**.

---

### 6️⃣ Análise e Conclusão

Nesta etapa são analisados os resultados obtidos durante os experimentos.

A análise aborda:

* Influência do tamanho da entrada;
* Crescimento do número de operações;
* Comparação entre Bubble Sort e Quick Sort;
* Comportamento da busca sequencial;
* Relação entre arrays, matrizes e complexidade;
* Importância de analisar operações além do resultado final.

📄 Arquivo:

`06-analise-e-conclusao.md`

---

## 📂 Organização do projeto

```text
estruturas-de-dados/
│
├── 01-pesquisa-bubble-sort-quick-sort.md
├── 02-experimento-ordenacao.py
├── 03-busca-matrizes.py
├── 04-array-temperaturas.py
├── 05-monitoramento-sensores.py
└── 06-analise-e-conclusao.md
```

---

## 🛠️ Tecnologias utilizadas

* **Python 3**
* **GitHub**

---

## 📊 Principais conceitos trabalhados

* Arrays;
* Matrizes;
* Índices;
* Loops;
* Loops aninhados;
* Bubble Sort;
* Quick Sort;
* Busca sequencial;
* Comparações;
* Trocas;
* Movimentações;
* Complexidade computacional;
* Análise experimental de algoritmos.

---

## 📈 Conclusão geral

Os experimentos demonstram que algoritmos diferentes podem produzir o mesmo resultado utilizando quantidades muito diferentes de operações.

O Bubble Sort possui uma lógica simples, mas apresenta crescimento quadrático de operações, tornando-se menos adequado para grandes conjuntos de dados.

O Quick Sort apresenta, em média, comportamento **O(n log n)**, mostrando maior eficiência conforme o tamanho dos dados aumenta.

Os experimentos com matrizes também demonstram que a posição do elemento influencia diretamente a quantidade de comparações realizadas pela busca sequencial.

Dessa forma, a atividade permite relacionar a teoria de estruturas de dados com resultados práticos, mostrando a importância de analisar não apenas a corretude dos algoritmos, mas também sua eficiência e seu comportamento conforme o tamanho da entrada aumenta.
