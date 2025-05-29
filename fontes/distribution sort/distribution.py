import sys
import random
import time

def distribution_sort(v): 
    n = len(v)
    if n <= 0:
        return v

    s_val = min(v)
    b_val = max(v)
    
    range_val = b_val - s_val + 1
    counts = [0] * range_val

    for x in v:
        counts[x - s_val] += 1

    for i in range(1, range_val):
        counts[i] += counts[i-1]

    output_w = [0] * n

    for x in reversed(v):
        index_in_counts = x - s_val
        position_in_w = counts[index_in_counts] - 1
        output_w[position_in_w] = x
        counts[index_in_counts] -= 1
    
    for i in range(n):
        v[i] = output_w[i]
    
    return v


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
        min_rand_val = 0
        max_rand_val = n * 2  
        if n > 0 and max_rand_val < min_rand_val:
             max_rand_val = min_rand_val 
        
        if n > 0:
            v = [random.randint(min_rand_val, max_rand_val) for _ in range(n)]
        else: 
            v = []
        
    start_time_ns = time.monotonic_ns()

    distribution_sort(v)

    end_time_ns = time.monotonic_ns()
    execution_time_ns = end_time_ns - start_time_ns
    
    print(execution_time_ns)