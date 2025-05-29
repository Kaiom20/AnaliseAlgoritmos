# Análise de Algoritmos de Ordenação - Guia Rápido

**Autor:** Kaio Márcio Araújo Cavalcante Lira

## 1. Visão Geral

Este projeto implementa e analisa cinco algoritmos de ordenação (Selection, Insertion, Merge, Quick, Distribution Sort) em Python 3, com o objetivo de coletar dados de tempo de execução e gerar gráficos comparativos.

## 2. Pré-requisitos

* **Python 3.x:** Verifique com `python3 --version`.
* **Gnuplot:** Verifique com `gnuplot --version`.
* **Shell (sh-compatível):** Como Bash (padrão no Linux/macOS) ou Git Bash/WSL (no Windows).

## 3. Tutorial Básico de Uso

Este guia assume que todos os scripts (`.py`, `.sh`, `.gp`) estão no mesmo diretório.

### 3.1. Preparação Inicial (Linux/macOS)

Pode ser necessário dar permissão de execução ao script `iterate.sh`, cole esse comando no terminal:
```bash
chmod +x iterate.sh
```

### 3.2. Gerando Dados de Desempenho
Utilize o script iterate.sh para executar os algoritmos e coletar dados de tempo.
```bash
./iterate.sh 10 1000 100 10000 "python3 insertionB.py" insertionB_desempenho
```

Sintaxe:

Bash

./iterate.sh <execucoes> <N_inicial> <passo_N> <N_final> "<comando_python_com_script>" <nome_base_saida>
<execucoes>: Nº de repetições por N (ex: 10).
<N_inicial>, <passo_N>, <N_final>: Faixa e incremento de N (ex: 1000 1000 10000).
<comando_python_com_script>: Comando para rodar o script Python (ex: "python3 selection_sort.py").
<nome_base_saida>: Nome base para o arquivo de dados .txt gerado (ex: selection_data).
Exemplo de Uso (para Selection Sort):

Bash

./iterate.sh 10 1000 1000 10000 "python3 selection_sort.py" selection_data
Isso criará um arquivo selection_data.txt.

Para outros algoritmos e casos:

Adapte o <comando_python_com_script> para o arquivo .py desejado (ex: insertion_sort.py, merge_sort.py, quick_sort.py, quick_sort_pior_caso.py, distribution_sort.py, etc.).
Use um <nome_base_saida> diferente para cada conjunto de dados.
Considerações Importantes ao Gerar Dados:

Distribution Sort (distribution_sort.py): Este script está configurado para gerar números aleatórios numa faixa controlada (ex: [0, 2*N]) para que a amplitude k dos valores seja gerenciável e evite MemoryError.
Quick Sort (Pior Caso - quick_sort_pior_caso.py): Este script gera entrada ordenada. Para valores de N grandes (ex: >1000), ele pode atingir o limite de recursão do Python. O script tenta aumentar esse limite (sys.setrecursionlimit()), mas esteja ciente.
3.3. Gerando os Gráficos
Os gráficos são criados com Gnuplot a partir dos arquivos de dados .txt.

Para gerar um gráfico:

Edite o script .gp: Abra o arquivo Gnuplot (ex: plot_todos_algoritmos.gp) em um editor de texto. Certifique-se de que os nomes dos arquivos .txt dentro do comando plot correspondem aos nomes dos arquivos de dados que você gerou.
Execute o Gnuplot:
Bash

gnuplot nome_do_seu_script.gp
Exemplo:
Bash

gnuplot plot_todos_algoritmos.gp
Isso normalmente salva um arquivo de imagem (ex: .png) no mesmo diretório.
3.4. Scripts Principais Envolvidos
*.py (Ex: selection_sort.py, merge_sort.py, etc.): Implementações dos algoritmos de ordenação, preparadas para benchmarking (leem N da linha de comando, geram dados, medem tempo).
iterate.sh: Script Shell para automatizar as execuções e coletar estatísticas de tempo.
*.gp (Ex: plot_todos_algoritmos.gp): Scripts Gnuplot para visualizar os dados de desempenho.
Este tutorial básico deve ser suficiente para começar a gerar os dados e os gráficos. Consulte os comentários nos scripts para mais detalhes específicos de cada um.

