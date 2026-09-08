# ATIVIDADE AVALIATIVA – ESTRUTURAS DE DADOS 2

Este diretório contém a solução fracionada da atividade avaliativa sobre arrays, matrizes, algoritmos de ordenação e busca.

Estrutura do diretório (cada item será adicionado em commits separados conforme a evolução):

1. pesquisa/
   - bubble_sort.md        # pesquisa e explicação do Bubble Sort
   - quick_sort.md         # pesquisa e explicação do Quick Sort
   - comparacao.md         # tabela comparativa

2. ordenacao/
   - bubble_sort.c         # implementação do Bubble Sort + contador de operações
   - quick_sort.c          # implementação do Quick Sort + contador de operações
   - testes_ordenação/     # scripts e arquivos de entrada para testes (10, 20, 1000)

3. busca_matriz/
   - busca_matriz.c        # busca sequencial em matriz com contagem de comparações
   - testes_busca/         # arquivos de entrada para as matrizes

4. hands_on/
   - handson1_array.c      # array de 10 temperaturas
   - handson2_sensores.c   # matriz 5x24 com relatórios

5. docs/
   - tabelas_resultados.md # tabelas e análises dos experimentos
   - conclusao.md         # análise e conclusão final

6. README.md              # este arquivo

Plano de commits (sugestões):
- commit 1: chore: add atividade-avaliativa README (este commit)
- commit 2: feat(pesquisa): adicionar pesquisas Bubble e Quick + comparação
- commit 3: feat(ordenacao): adicionar implementações Bubble e Quick (10,20,1000)
- commit 4: feat(busca): adicionar busca em matriz e testes 2x2,10x10,100x100
- commit 5: feat(handson): adicionar handson1 (array de temperaturas)
- commit 6: feat(handson): adicionar handson2 (sensores 5x24)
- commit 7: docs: adicionar tabelas de resultados e conclusão

Instruções para quem for commitar localmente (opcional):
- Para criar a pasta localmente e commitar:
  mkdir atividade-avaliativa && cd atividade-avaliativa
  git init
  git remote add origin <url-do-repo>
  # copie os arquivos e faça os commits conforme o plano

Observação importante:
- Antes de eu gerar os códigos fracionados, me diga qual linguagem de programação você prefere (C, C++, Java, Python ou outra). Vou gerar os códigos prontos para você copiar/colar e commitar etapa a etapa.

---

Feito: adicionei o README inicial com o plano de trabalho.
Próximo passo: aguardo sua resposta sobre a linguagem a ser usada para gerar os códigos fracionados (padrão: C se você não especificar).