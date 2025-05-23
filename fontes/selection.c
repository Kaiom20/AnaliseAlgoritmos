#include <stdio.h>

void selection_sort(int v[], int n) {
    int i, j, m, temp;
    for (i = 0; i < n - 1; i++) {
        m = i;
        for (j = i + 1; j < n; j++) {
            if (v[m] > v[j]) {
                m = j;
            }
        }
        if (m != i) {
            temp = v[m];
            v[m] = v[i];
            v[i] = temp;
        }
    }
}

int main() {
    int vetor[] = {9,8, 7, 6, 5, 4, 3, 2, 1};
    int n = sizeof(vetor) / sizeof(vetor[0]);

    printf("Vetor antes da ordenação: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");

    selection_sort(vetor, n);

    printf("Vetor depois da ordenação: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");

    return 0;
}