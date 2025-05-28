import sys
import random
import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
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

    if n == 0:
        v = []
    else:
        v = [random.randint(0, 2**31 - 1) for _ in range(n)]
    
    start_time_ns = time.monotonic_ns()

    selection_sort(v)

    end_time_ns = time.monotonic_ns()
    execution_time_ns = end_time_ns - start_time_ns
    
    print(execution_time_ns)