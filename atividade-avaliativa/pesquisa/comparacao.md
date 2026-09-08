# Tabela comparativa: Bubble Sort vs Quick Sort

| Característica             | Bubble Sort                         | Quick Sort                             |
|---------------------------:|:-----------------------------------:|:---------------------------------------:|
| Princípio de funcionamento | Troca adjacente repetida (passagens)| Dividir e conquistar (partição pivô)   |
| Melhor caso               | O(n) (com detecção de parada)       | O(n log n)                             |
| Caso médio                | O(n^2)                              | O(n log n)                             |
| Pior caso                 | O(n^2)                              | O(n^2) (pivô ruim)                     |
| Uso de memória            | O(1) (in-place)                     | O(log n) média (recursão); in-place possível |
| Vantagem principal        | Simplicidade e estabilidade         | Alto desempenho médio e eficiencia de cache |
| Limitação principal       | Escalabilidade (ineficiente)        | Pior caso O(n^2), não estável (padrão) |
| Aplicação recomendada     | Pequenas listas, aprendizado        | Grandes listas, aplicações práticas    |
| Aplicação não recomendada | Grandes entradas com necessidade de performance | Quando estabilidade ou garantia do pior caso é necessária |

---

Observações:
- Experimentalmente, Quick Sort tende a realizar muito menos comparações e movimentações que Bubble Sort em entradas maiores.
- Em entradas muito pequenas (por exemplo, n <= 10), a diferença prática pode ser pequena; às vezes algoritmos simples vencem por menor overhead.
