import sys
import random
import time

def distribution_sort(v): # Renomeei para clareza, você pode manter o nome original
    n = len(v)
    if n <= 0:
        return v

    s_val = min(v)
    b_val = max(v)
    
    range_val = b_val - s_val + 1
    counts = [0] * range_val

    for x in v:
        counts[x - s_val] += 1

    # 'counts' agora armazena as posições finais (1-baseadas)
    for i in range(1, range_val):
        counts[i] += counts[i-1]

    output_w = [0] * n

    # ALTERAÇÃO PRINCIPAL PARA ESTABILIDADE:
    # Percorre o array de entrada 'v' em ORDEM INVERSA.
    # Você pode fazer isso de algumas formas em Python:
    # Opção 1: Usando reversed() - mais Pythonic se você só precisa dos elementos
    for x in reversed(v):
        index_in_counts = x - s_val
        position_in_w = counts[index_in_counts] - 1
        output_w[position_in_w] = x
        counts[index_in_counts] -= 1
    
    # Opção 2: Usando um laço com índices de n-1 até 0 (se precisar do índice original i)
    # for i in range(n - 1, -1, -1):
    #     x = v[i] # Pega o elemento atual
    #     index_in_counts = x - s_val
    #     position_in_w = counts[index_in_counts] - 1
    #     output_w[position_in_w] = x
    #     counts[index_in_counts] -= 1

    # Copia os elementos ordenados de output_w de volta para v
    for i in range(n):
        v[i] = output_w[i]
    
    return v


# Bloco principal adaptado para medição de tempo e entrada via linha de comando
if __name__ == "__main__":
    # 1. Verifica e processa argumentos da linha de comando
    if len(sys.argv) != 2:
        print(f"Uso: python {sys.argv[0]} <tamanho_do_array>", file=sys.stderr)
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 0:
            print("O tamanho do array não pode ser negativo.", file=sys.stderr)
            sys.exit(1)
    except ValueError:
        print("O tamanho do array deve ser um número inteiro.", file=sys.stderr)
        sys.exit(1)

    # 2. Cria e preenche o array com números aleatórios
    if n == 0:
        v = []
    else:
        # GERAÇÃO DE NÚMEROS ALEATÓRIOS - ATENÇÃO PARA DISTRIBUTION SORT:
        # O Distribution Sort (Counting Sort) é sensível à AMPLITUDE (k = max_val - min_val + 1)
        # dos valores no array. Se a amplitude 'k' for muito grande (ex: números de 0 a 2^31 - 1),
        # o array 'counts' se tornará gigantesco, consumindo muita memória e tempo para
        # inicializar e iterar, o que pode anular os benefícios de O(N+k).
        # Para uma comparação justa com outros algoritmos que não têm essa sensibilidade a 'k',
        # você pode manter este range amplo. Mas para mostrar o Counting Sort em seu melhor cenário
        # (onde k é da ordem de N ou não muito maior), você consideraria um range menor,
        # por exemplo: random.randint(0, n * C) onde C é uma constante pequena.
        #
        # Por ora, para consistência com os testes dos outros algoritmos, usaremos o mesmo range amplo:
        min_rand_val = 0
        max_rand_val = n * 2  # Isso fará k ser aproximadamente 2*N
        # Adicionando uma pequena salvaguarda para n=0 ou casos onde n*2 pode ser < 0 (improvável aqui)
        if n > 0 and max_rand_val < min_rand_val:
             max_rand_val = min_rand_val # ou min_rand_val + n, para garantir uma faixa
        
        if n > 0:
            v = [random.randint(min_rand_val, max_rand_val) for _ in range(n)]
        else: # n == 0
            v = []
        
    # 3. Mede o tempo de execução da ordenação
    start_time_ns = time.monotonic_ns()

    # Chama a função distribution_sort
    # Ela lida com n=0 internamente
    distribution_sort(v)

    end_time_ns = time.monotonic_ns()
    
    # Calcula o tempo de execução
    execution_time_ns = end_time_ns - start_time_ns
    
    # 4. Imprime APENAS o tempo de execução (para o iterate.sh)
    print(execution_time_ns)