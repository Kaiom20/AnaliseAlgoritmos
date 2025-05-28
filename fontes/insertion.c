#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void insertion_sort(int *v, int tamanho);

int main(int argc, char **argv)
{
    struct timespec a, b;
    unsigned long t;
    unsigned int n = atoi(argv[1]);
    int *vetor = (int *)malloc(n * sizeof(int));

    for (int i = 0; i < n; i++)
        vetor[i] = i;

    clock_gettime(CLOCK_MONOTONIC, &b);

    insertion_sort(vetor, n);

    clock_gettime(CLOCK_MONOTONIC, &a);

    t = (a.tv_sec * 1e9 + a.tv_nsec) - (b.tv_sec * 1e9 + b.tv_nsec);
    
    printf("%lu\n", t);
    
    free(vetor);

    return 0;
}

void insertion_sort(int *v, int tamanho)
{
    int i, e;
    int auxiliar;

    for(e = 1; e < tamanho; e++)
    {
        auxiliar = v[e];
        i = e - 1; 

        while(i >= 0 && v[i] > auxiliar)
        {
            v[i + 1] = v[i];
            i = i - 1;
        }

        v[i + 1] = auxiliar;
    }
}


