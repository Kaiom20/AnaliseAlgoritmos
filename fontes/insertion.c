#include <stdio.h>

void insertion_sort(int v[], int n) {
    int e, i, temp;
    for (e = 1; e < n; e++) {
        i = e;
        while (i > 0 && v[i - 1] > v[i]) {
            temp = v[i];
            v[i] = v[i - 1];
            v[i - 1] = temp;
            i = i - 1;
        }
    }
}

int main() {
    int vetor[] = {5, 2, 8, 1, 9, 4};
    int n = sizeof(vetor) / sizeof(vetor[0]);

    printf("Vetor antes da ordenação: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");

    insertion_sort(vetor, n);

    printf("Vetor depois da ordenação: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");

    return 0;
}