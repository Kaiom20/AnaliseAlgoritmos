import sys
import random
import time

def partition(v, inicio, fim):
    pivot = v[fim]  
    i = inicio - 1  

    for j in range(inicio, fim): 
        if v[j] <= pivot:
            i += 1
            v[i], v[j] = v[j], v[i]
    
    v[i + 1], v[fim] = v[fim], v[i + 1]
    return i + 1 

def quick_sort(v, inicio, fim):
    if inicio < fim:
        p = partition(v, inicio, fim)
        
        quick_sort(v, inicio, p - 1)
        quick_sort(v, p + 1, fim)

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

    try:
        sys.setrecursionlimit(n + 200) 
    except Exception as e:
        print(f"Aviso: Falha ao tentar aumentar o limite de recursão para N={n}. Limite atual: {sys.getrecursionlimit()}. Erro: {e}", file=sys.stderr)

    vetor = []
    if n > 0:
        vetor = list(range(1, n + 1)) 
    elif n == 0:
        vetor = []
   
    start_time_ns = time.monotonic_ns()
    quick_sort(vetor, 0, n - 1)
    end_time_ns = time.monotonic_ns()
    execution_time_ns = end_time_ns - start_time_ns
    
    # 4. Imprime APENAS o tempo de execução
    print(execution_time_ns)