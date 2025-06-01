# Análise Comparativa de Algoritmos de Ordenação - Guia de Uso

**Autor:** Kaio Márcio Araújo Cavalcante Lira

## 1. Visão Geral do Projeto

Este projeto implementa e analisa o desempenho de cinco algoritmos de ordenação clássicos: Selection Sort, Insertion Sort, Merge Sort, Quick Sort e Distribution Sort. As implementações são feitas em Python.

O processo envolve:
1.  Executar scripts Python que ordenam arrays de diferentes tamanhos e medem o tempo de execução.
2.  Utilizar um script shell (`iterate.sh`) para automatizar múltiplas execuções e coletar dados estatísticos (média, mínimo, máximo).
3.  Usar scripts Gnuplot (`.gp`) para gerar gráficos de desempenho (Tempo vs. Tamanho da Entrada N) a partir dos dados coletados.

O relatório final (não incluído aqui) utilizará esses dados e gráficos para comparar os algoritmos.

---
## 2. Pré-requisitos e Configuração Inicial

Antes de começar, certifique-se de que você tem os seguintes softwares instalados no seu sistema:

* **Python 3:** Versão 3.6 ou superior é recomendada.
    * Para verificar: `python3 --version`
* **Gnuplot:** Necessário para gerar os gráficos.
    * Para verificar: `gnuplot --version`
* **Um ambiente shell compatível com `sh`:**
    * **Linux/macOS:** O terminal padrão (Bash, Zsh, etc.) geralmente já é compatível.
    * **Windows:** Recomenda-se usar Git Bash, WSL (Windows Subsystem for Linux)

Nenhuma biblioteca Python externa é necessária além das padrão (`sys`, `random`, `time`). Assume-se que todos os scripts (`.py`, `.sh`, `.gp`) estão no mesmo diretório para os comandos de exemplo.

---
## 3. Tutorial: Gerando os Dados de Desempenho

Os dados de tempo de execução são a base para os seus gráficos e análises.

### 3.1. Tornando o Script `iterate.sh` Executável

Você pode precisar dar permissão de execução ao script `iterate.sh` uma vez:
```bash
chmod +x iterate.sh
```
### 3.2. Entendendo e Usando o iterate.sh
O script iterate.sh automatiza a execução de um script Python várias vezes para diferentes tamanhos de entrada (N) e calcula estatísticas de tempo.

- Sintaxe Geral:

Bash

./iterate.sh <execucoes> <N_inicial> <passo_N> <N_final> "<comando_python_com_script>" <nome_base_arquivo_saida>
<execucoes>: Quantas vezes o script Python roda para cada valor de N (ex: 10).
<N_inicial>: Primeiro valor de N a ser testado (ex: 1000).
<passo_N>: Quanto N aumenta a cada rodada (ex: 1000).
<N_final>: Último valor de N a ser testado (ex: 10000).
<comando_python_com_script>: O comando exato para rodar seu script Python, entre aspas. Deve incluir python3 e o nome do arquivo .py (ex: "python3 selection_sort.py").
<nome_base_arquivo_saida>: Um nome base. O iterate.sh criará um arquivo chamado <nome_base_arquivo_saida>.txt.
3.3. Comandos para Gerar Dados de Cada Algoritmo
Abaixo estão os comandos para gerar os dados para cada algoritmo e seus respectivos casos. Ajuste os parâmetros de N (N_inicial, passo_N, N_final) e execucoes conforme sua necessidade. Os exemplos usam 10 execuções, N de 1000 a 10000, com passo de 1000.

A. Selection Sort
Gera dados para o comportamento $O(N^2)$.
Bash

./iterate.sh 10 1000 1000 10000 "python3 selection_sort.py" selection_desempenho
(Gera selection_desempenho.txt)
B. Insertion Sort
Melhor Caso (entrada ordenada):

Script Python: insertion_sort_melhor.py (configurado para gerar um array ordenado).
Bash

./iterate.sh 10 1000 1000 10000 "python3 insertion_sort_melhor.py" insertion_melhor_desempenho
(Gera insertion_melhor_desempenho.txt)

Caso Médio (entrada aleatória [1,N]):

Script Python: insertion_sort.py (configurado para gerar um array aleatório [1,N])
Bash

./iterate.sh 10 1000 1000 10000 "python3 insertion_sort.py" insertion_medio_desempenho
(Gera insertion_medio_desempenho.txt)

Pior Caso (entrada em ordem inversa):

Script Python: insertion_sort_pior.py (configurado para gerar um array em ordem inversa).
Bash

./iterate.sh 10 1000 1000 10000 "python3 insertion_sort_pior.py" insertion_pior_desempenho
(Gera insertion_pior_desempenho.txt)

C. Merge Sort
Gera dados para o comportamento $O(N \log N)$.
Script Python: merge_sort.py (com entrada aleatória, pois seu comportamento é consistente).
Bash

./iterate.sh 10 1000 1000 10000 "python3 merge_sort.py" merge_desempenho
(Gera merge_desempenho.txt)
D. Quick Sort
Caso Médio (entrada aleatória [1,N]):

Script Python: quick_sort.py (com entrada aleatória [1,N] e partição de Lomuto).
Bash

./iterate.sh 10 1000 1000 10000 "python3 quick_sort.py" quick_medio_desempenho
(Gera quick_medio_desempenho.txt)

Pior Caso (entrada ordenada para Lomuto):

Script Python: quick_sort_pior_caso.py (configurado para gerar um array ordenado e tentar aumentar o limite de recursão sys.setrecursionlimit()).
Bash

./iterate.sh 10 1000 1000 10000 "python3 quick_sort_pior_caso.py" quick_pior_desempenho
(Gera quick_pior_desempenho.txt)

E. Distribution Sort (Counting Sort)
Gera dados para o comportamento $O(N+k)$, onde $k \approx O(N)$ (entrada aleatória, por exemplo, [0, 2*N]).
Script Python: distribution_sort.py (configurado para gerar dados com amplitude k controlada para evitar MemoryError).
Bash

./iterate.sh 10 1000 1000 10000 "python3 distribution_sort.py" distribution_desempenho
(Gera distribution_desempenho.txt)
3.4. Arquivos de Dados Gerados
Após executar os comandos acima, você terá vários arquivos .txt (ex: selection_desempenho.txt, insertion_melhor_desempenho.txt, etc.). Cada um contém dados com colunas, sendo as principais para plotagem:

Coluna 1: N (Tamanho da entrada)
Coluna 2: Tempo Médio de execução (nanossegundos)
4. Tutorial: Gerando os Gráficos
Com os arquivos de dados .txt prontos, use o Gnuplot para criar os gráficos.

4.1. Entendendo os Scripts Gnuplot (.gp)
Os arquivos com extensão .gp contêm comandos para o Gnuplot. Eles especificam:

Títulos do gráfico e dos eixos.
Quais arquivos de dados (.txt) usar.
Quais colunas de dados plotar (tipicamente coluna 1 para N e coluna 2 para Tempo Médio).
Estilos de linha, cores e legendas.
O nome do arquivo de imagem de saída (ex: .png).
Importante: Antes de executar um script .gp, abra-o em um editor de texto e verifique se os nomes dos arquivos .txt dentro do comando plot correspondem exatamente aos nomes dos arquivos de dados que você gerou na seção 3.3.

4.2. Executando o Gnuplot
No terminal, no mesmo diretório onde estão seus arquivos .gp e os arquivos de dados .txt, execute:

Bash

gnuplot nome_do_script.gp
Exemplo para plotar o comparativo de todos os algoritmos (casos médios):

Bash

gnuplot plot_todos_algoritmos.gp
Isso gerará um arquivo de imagem (ex: comparativo_todos_algoritmos.png). Faça o mesmo para outros scripts .gp que você tenha (ex: plot_insertion_todos.gp, plot_quick_comparativo.gp).

5. Visão Geral dos Scripts Principais
Scripts Python (*.py):
selection_sort.py, insertion_sort.py, merge_sort.py, quick_sort.py, distribution_sort.py: Implementações dos algoritmos com a lógica de benchmark para gerar o tempo de execução para um dado N.
insertion_sort_melhor.py, insertion_sort_pior.py, quick_sort_pior_caso.py: Variações dos scripts acima, configuradas para gerar tipos específicos de entrada (ordenada, inversa) para análise de melhor/pior caso.
iterate.sh: Script Shell para automatizar a execução múltipla dos scripts Python e coletar dados estatísticos de tempo.
Scripts Gnuplot (*.gp): Arquivos de comando para o Gnuplot gerar os gráficos a partir dos dados .txt.
6. Considerações Importantes
Distribution Sort (Counting Sort): Lembre-se que este algoritmo é eficiente ($O(N+k)$) quando k (amplitude dos valores: max-min+1) é da ordem de N. O script distribution_sort.py foi configurado para gerar números aleatórios numa faixa como [0, 2*N] para manter k gerenciável.
Quick Sort (Pior Caso): A implementação recursiva simples pode atingir o limite de profundidade de recursão do Python no pior caso ($O(N)$ de profundidade de pilha) para valores grandes de N. O script quick_sort_pior_caso.py tenta aumentar este limite com sys.setrecursionlimit().
Parâmetros do iterate.sh: Os valores de N_inicial, passo_N, N_final e execucoes podem ser ajustados para obter resultados mais detalhados ou para testes mais rápidos.