#include <stdio.h>
#include <stdlib.h>

// Função auxiliar para trocar dois elementos em um array
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Função de particionamento para o Quick Sort
int partition(int v[], int s, int e) {
    int d = s - 1;
    int pivot = v[e]; // Escolhe o último elemento como pivô
    for (int i = s; i < e; i++) {
        if (v[i] <= pivot) {
            d++;
            swap(&v[d], &v[i]);
        }
    }
    swap(&v[d + 1], &v[e]);
    return (d + 1);
}

// Função principal do Quick Sort (recursiva)
void quick_sort(int v[], int s, int e) {
    if (s < e) {
        int p = partition(v, s, e);
        quick_sort(v, s, p - 1);
        quick_sort(v, p + 1, e);
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

    quick_sort(vetor, 0, n - 1); // Em C, os índices começam em 0

    printf("Vetor depois da ordenação: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");

    return 0;
}