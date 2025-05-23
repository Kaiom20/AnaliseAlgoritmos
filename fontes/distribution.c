#include <stdio.h>
#include <stdlib.h>
#include <limits.h> // Para INT_MIN e INT_MAX

// Função para encontrar o mínimo elemento em um array
int min(int v[], int n) {
    int min_val = INT_MAX;
    for (int i = 0; i < n; i++) {
        if (v[i] < min_val) {
            min_val = v[i];
        }
    }
    return min_val;
}

// Função para encontrar o máximo elemento em um array
int max(int v[], int n) {
    int max_val = INT_MIN;
    for (int i = 0; i < n; i++) {
        if (v[i] > max_val) {
            max_val = v[i];
        }
    }
    return max_val;
}

// Função de ordenação por distribuição (Counting Sort)
void distribution_sort(int v[], int n) {
    if (n <= 0) {
        return;
    }

    int s = min(v, n);
    int b = max(v, n);
    int range = b - s + 1;

    // Aloca memória para o array de contagem c
    int *c = (int *)malloc(range * sizeof(int));
    if (c == NULL) {
        fprintf(stderr, "Erro na alocação de memória para o array de contagem\n");
        exit(EXIT_FAILURE);
    }

    // Inicializa o array de contagem com zeros
    for (int i = 0; i < range; i++) {
        c[i] = 0;
    }

    // Conta a frequência de cada elemento
    for (int i = 0; i < n; i++) {
        c[v[i] - s]++;
    }

    // Calcula as posições finais dos elementos
    for (int i = 1; i < range; i++) {
        c[i] += c[i - 1];
    }

    // Aloca memória para o array de saída w
    int *w = (int *)malloc(n * sizeof(int));
    if (w == NULL) {
        fprintf(stderr, "Erro na alocação de memória para o array de saída\n");
        free(c); // Libera a memória alocada para c
        exit(EXIT_FAILURE);
    }

    // Coloca os elementos na sua posição ordenada no array w
    for (int i = 0; i < n; i++) {
        int index = v[i] - s;
        w[c[index] - 1] = v[i];
        c[index]--;
    }

    // Copia os elementos ordenados de w de volta para v
    for (int i = 0; i < n; i++) {
        v[i] = w[i];
    }

    // Libera a memória alocada para c e w
    free(c);
    free(w);
}

int main() {
    int vetor[] = {5, 2, 8, 1, 9, 4, 7, 3, 6, 2, 14, 12, 11};
    int n = sizeof(vetor) / sizeof(vetor[0]);

    printf("Vetor antes da ordenação: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");

    distribution_sort(vetor, n);

    printf("Vetor depois da ordenação: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");

    return 0;
}