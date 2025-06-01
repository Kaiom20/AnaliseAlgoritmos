import sys
import random
import time

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr

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

    vetor = []
    if n > 0:
        vetor = [random.randint(1, n) for _ in range(n)]
    elif n == 0:
        vetor = []
    
 
    start_time_ns = time.monotonic_ns()

    insertion_sort(vetor) 

    end_time_ns = time.monotonic_ns()
    execution_time_ns = end_time_ns - start_time_ns
    
    print(execution_time_ns)