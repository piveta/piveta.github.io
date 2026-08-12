#include <stdio.h>
#include <stdlib.h>

int main() {
    constexpr int lines = 10;
    constexpr int columns = 10;

    int **m = malloc(lines * sizeof(*m));
    if (m == NULL)
        return 1;

    for (int i = 0; i < lines; i++) {
        m[i] = malloc(columns * sizeof(*m[i]));
        if (m[i] == NULL) {
            for (int j = 0; j < i; ++j)
                free(m[j]);
            free(m);
            return 1;
        }
    }

    for (int i = 0; i < lines; i++)
        for (int j = 0; j < columns; j++)
            m[i][j] = i * columns + j;

    for (int i = 0; i < lines; i++)
        for (int j = 0; j < columns; j++)
            printf("m[%d][%d] = %d\n", i, j, m[i][j]);

    for (int i = 0; i < lines; i++)
        free(m[i]);

    free(m);
}
