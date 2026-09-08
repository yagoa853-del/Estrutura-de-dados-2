# Quick Sort

## Como o algoritmo funciona
Quick Sort é um algoritmo de ordenação por divisão e conquista. Escolhe-se um elemento pivô e particiona-se o array em dois subarrays: elementos menores que o pivô e elementos maiores que o pivô. Em seguida aplica-se recursivamente o mesmo procedimento a cada subarray. No final, a concatenação dos subarrays ordenados resulta no array ordenado.

## Lógica de ordenação (resumida)
- Escolher um pivô (pode ser o primeiro, último, aleatório ou mediana).
- Particionar o array em elementos menores e maiores do pivô.
- Recursivamente ordenar as partições esquerda e direita.
- Combinar (implícito na estrutura in-place) para obter o array final.

## Complexidade
- Melhor caso: O(n log n)
- Caso médio: O(n log n)
- Pior caso: O(n^2) (ocorre quando a partição é muito desequilibrada, por exemplo, pivô sempre mínimo ou máximo)

## Uso de memória
- Espaço extra: O(log n) em média para a pilha de chamadas recursivas; O(n) em pior caso de recursão sem otimizações.

## Vantagens
- Muito eficiente na prática (caso médio O(n log n)).
- Bom uso de cache quando implementado in-place.
- Flexível (variações como escolha aleatória do pivô reduzem chance do pior caso).

## Limitações
- Pior caso O(n^2) se pivô mal escolhido (pode ser mitigado com escolha aleatória/mediana).
- Não é estável na implementação in-place padrão (a ordem de elementos iguais não é garantida).
- Requer chamadas recursivas (possível problema de profundidade de pilha em arrays muito grandes sem otimizações).

## Situações em que seu uso é adequado
- Ordenação de grandes conjuntos de dados em memória.
- Aplicações que exigem boa performance média e uso eficiente de cache.

## Situações em que não é recomendado
- Quando estabilidade é necessária — preferir Merge Sort estável ou variações estáveis.
- Quando se precisa garantir O(n log n) no pior caso (usar Heapsort ou Merge Sort).
