# Atividade de Participação: Manipulação de Listas e Representação na Memória

## 👥 Integrantes da Dupla
*   **Yago Alves De Carvalho**
*   **Pedro Henrique Monteiro**

---

## 💻 Código Python Desenvolvido

O script abaixo analisa o comportamento de uma lista dinâmica à medida que realizamos operações de inserção, remoção e alteração, inspecionando o endereço de memória (`id()`) do contêiner (lista) e dos elementos internos (inteiros).

```python
lista = [10, 20, 30]
print("Lista inicial")
print(f"Estado atual da lista: {lista} | ID da Lista: {id(lista)}")
for i, item in enumerate(lista):
    print(f"Índice {i}: valor = {item} | id = {id(item)}")
print("-" * 50)

# Adicionar um elemento ao final com append()
lista.append(50)
print(f"Após append: {lista} | ID da Lista: {id(lista)}")
for i, item in enumerate(lista):
    print(f"Índice {i}: valor = {item} | id = {id(item)}")
print("-" * 50)

# Inserir um elemento em uma posição específica com insert()
lista.insert(2, 12)
print(f"Após insert: {lista} | ID da Lista: {id(lista)}")
for i, item in enumerate(lista):
    print(f"Índice {i}: valor = {item} | id = {id(item)}")
print("-" * 50)

# Remover um elemento pelo valor utilizando remove()
lista.remove(12)
print(f"Após remove: {lista} | ID da Lista: {id(lista)}")
for i, item in enumerate(lista):
    print(f"Índice {i}: valor = {item} | id = {id(item)}")
print("-" * 50)

# Remover um elemento pela posição utilizando pop()
lista.pop(0)
print(f"Após pop: {lista} | ID da Lista: {id(lista)}")
for i, item in enumerate(lista):
    print(f"Índice {i}: valor = {item} | id = {id(item)}")
print("-" * 50)

# Alterar o valor de um elemento existente
lista[1] = 7
print(f"Após alteração: {lista} | ID da Lista: {id(lista)}")
for i, item in enumerate(lista):
    print(f"Índice {i}: valor = {item} | id = {id(item)}")
print("-" * 50)

# Limpar os elementos utilizando clear()
lista.clear()
print(f"Após clear: {lista} | ID da Lista: {id(lista)}")
for i, item in enumerate(lista):
    print(f"Índice {i}: valor = {item} | id = {id(item)}")
print("-" * 50)
```

---

## 📸 Evidências da Execução (Resultados Obtidos)

```text
Lista inicial
Estado atual da lista: [10, 20, 30] | ID da Lista: 126594003954816
Índice 0: valor = 10 | id = 94240188489560
Índice 1: valor = 20 | id = 94240188489880
Índice 2: valor = 30 | id = 94240188490200
--------------------------------------------------
Após append: [10, 20, 30, 50] | ID da Lista: 126594003954816
Índice 0: valor = 10 | id = 94240188489560
Índice 1: valor = 20 | id = 94240188489880
Índice 2: valor = 30 | id = 94240188490200
Índice 3: valor = 50 | id = 94240188490840
--------------------------------------------------
Após insert: [10, 20, 12, 30, 50] | ID da Lista: 126594003954816
Índice 0: valor = 10 | id = 94240188489560
Índice 1: valor = 20 | id = 94240188489880
Índice 2: valor = 12 | id = 94240188489624
Índice 3: valor = 30 | id = 94240188490200
Índice 4: valor = 50 | id = 94240188490840
--------------------------------------------------
Após remove: [10, 20, 30, 50] | ID da Lista: 126594003954816
Índice 0: valor = 10 | id = 94240188489560
Índice 1: valor = 20 | id = 94240188489880
Índice 2: valor = 30 | id = 94240188490200
Índice 3: valor = 50 | id = 94240188490840
--------------------------------------------------
Após pop: [20, 30, 50] | ID da Lista: 126594003954816
Índice 0: valor = 20 | id = 94240188489880
Índice 1: valor = 30 | id = 94240188490200
Índice 2: valor = 50 | id = 94240188490840
--------------------------------------------------
Após alteração: [20, 7, 50] | ID da Lista: 126594003954816
Índice 0: valor = 20 | id = 94240188489880
Índice 1: valor = 7 | id = 94240188489464
Índice 2: valor = 50 | id = 94240188490840
--------------------------------------------------
Após clear: [] | ID da Lista: 126594003954816
--------------------------------------------------
```

---

## 🧠 Respostas da Atividade

### a) O id() da lista mudou durante as operações? O que isso indica?
Não, significa que é uma lista mutável.

### b) O que aconteceu com os elementos quando novos valores foram adicionados?
Os antigos mantiveram seus id e os atuais ganharam novos.

### c) O que acontece com a referência de um elemento quando ele é removido da lista?
Ele é excluído junto com o elemento.

### d) Ao alterar um elemento da lista, o id() desse elemento permaneceu igual? Explique o resultado observado.
Não, o id foi alterado porque no Python, você não altera o valor que está dentro de um número, você simplesmente faz a lista apontar para um número diferente.

### e) Por que dizemos que uma lista em Python é um objeto mutável?
Porque é possível fazer alterações como append(), remove().

### f) Qual é a diferença entre alterar o conteúdo de uma lista e criar uma nova lista?
Alterar um elemento de uma lista faz com que ela possua o mesmo id, enquanto uma lista nova terá um novo id.
