#include <stdio.h>
#include <stdlib.h>

int main() {
    constexpr int size = 10;
    int *v = malloc(size * sizeof(*v));
    if (v == NULL)
        return 1;
    for (int i = 0; i < size; i++)
        v[i] = i;
    for (int i = 0; i < size; i++)
        printf("v[%d] = %d\n", i, v[i]);
    free(v);
}
