import math 
import sys
import random
import time

def merge(v, s, m, e):
    p = s
    q = m + 1
    
    w_size = e - s + 1
    if w_size <= 0: # Caso de segmento vazio ou inválido
        return
    w = [0] * w_size

    for i in range(w_size):
        if q > e:  # Se a segunda sub-lista (direita) acabou
            w[i] = v[p]
            p += 1
        elif p > m: # Se a primeira sub-lista (esquerda) acabou
            w[i] = v[q]
            q += 1
        elif v[p] < v[q]: # Compara elementos de ambas as sub-listas (instável com esta condição)
            w[i] = v[p]
            p += 1
        else:            # v[q] <= v[p]
            w[i] = v[q]
            q += 1
            
    # Copia os elementos de volta para o array original v
    for i in range(w_size):
        v[s + i] = w[i]

def merge_sort(v, s, e):
    if s < e:  
        m = (s + e) // 2
        merge_sort(v, s, m)      # Ordena a metade esquerda
        merge_sort(v, m + 1, e)  # Ordena a metade direita
        merge(v, s, m, e)      # Mescla as duas metades ordenadas

if __name__ == "__main__":
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

    if n == 0:
        v = []
    else:
        v = [random.randint(0, 2**31 - 1) for _ in range(n)]
    
    start_time_ns = time.monotonic_ns()

    merge_sort(v, 0, n - 1)

    end_time_ns = time.monotonic_ns()
    execution_time_ns = end_time_ns - start_time_ns
    
    print(execution_time_ns)