#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Função auxiliar para realizar o merge de duas sub-arrays ordenadas
void merge(int v[], int s, int m, int e) {
    int p = s;
    int q = m + 1;
    int i;
    int *w; // Array temporário para o merge

    // Aloca memória para o array temporário w
    w = (int *)malloc((e - s + 1) * sizeof(int));
    if (w == NULL) {
        fprintf(stderr, "Erro na alocação de memória para o merge\n");
        exit(EXIT_FAILURE);
    }

    for (i = 0; i < (e - s + 1); i++) {
        if ((q > e) || ((p <= m) && (v[p] < v[q]))) {
            w[i] = v[p];
            p++;
        } else {
            w[i] = v[q];
            q++;
        }
    }

    // Copia os elementos de volta para o array original v
    for (i = 0; i < (e - s + 1); i++) {
        v[s + i] = w[i];
    }

    // Libera a memória alocada para o array temporário w
    free(w);
}

// Função principal do Merge Sort (recursiva)
void merge_sort(int v[], int s, int e) {
    if (s < e) {
        int m = floor((s + e) / 2);
        merge_sort(v, s, m);
        merge_sort(v, m + 1, e);
        merge(v, s, m, e);
    }
}

int main() {
    int vetor[] = {5, 2, 8, 1, 9, 4, 7, 3, 6};
    int n = sizeof(vetor) / sizeof(vetor[0]);

    printf("Vetor antes da ordenação: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");

    merge_sort(vetor, 0, n - 1); // Em C, os índices começam em 0

    printf("Vetor depois da ordenação: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");

    return 0;
}