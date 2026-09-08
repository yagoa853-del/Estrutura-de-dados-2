# Bubble Sort

## Como o algoritmo funciona
Bubble Sort (ordenamento por bolha) percorre repetidamente a lista, comparando pares adjacentes de elementos e trocando-os se estiverem na ordem errada. Em cada passagem, o maior (ou menor, dependendo da ordem) "borbulha" até sua posição final. O processo se repete até que uma passagem completa não faça trocas, indicando que a lista está ordenada.

## Lógica de ordenação (resumida)
- Percorra o array várias vezes.
- Em cada passagem, compare elemento i com i+1.
- Se estiverem fora de ordem, troque-os.
- Reduza o intervalo útil (últimos elementos já ordenados) a cada passagem.

## Complexidade
- Melhor caso: O(n) (quando o algoritmo detecta que nenhuma troca foi feita e interrompe antecipadamente).
- Caso médio: O(n^2)
- Pior caso: O(n^2)

## Uso de memória
- Espaço extra: O(1) (algoritmo in-place).

## Vantagens
- Simplicidade de implementação e compreensão.
- Estável (preserva a ordem relativa de elementos iguais).
- Bom para listas muito pequenas ou quase ordenadas se implementado com detecção de parada antecipada.

## Limitações
- Muito ineficiente para listas grandes devido à complexidade quadrática.
- Pouco prático em aplicações reais onde existem alternativas muito mais rápidas.

## Situações em que seu uso é adequado
- Ensino e demonstração de conceitos de ordenação.
- Arrays muito pequenos (por exemplo, <= 10) ou quase ordenados.
- Quando a simplicidade é prioridade sobre desempenho.

## Situações em que não é recomendado
- Grandes coleções de dados.
- Quando desempenho e escalabilidade são importantes.
