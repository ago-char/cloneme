#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int* arr = (int*)malloc(5);
    for (int i = 0; i < 5; i++) printf("%d\n", arr[i]);
    printf("\n..................\n");
    arr = (int*)calloc(sizeof(int), 5);
    for (int i = 0; i < 5; i++) printf("%d\n", arr[i]);
    return 0;
}