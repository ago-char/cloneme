#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define TOTAL_SIZE 10

void* func(void* num) {
    static double* answer = NULL;
    static int index = 0;
    if (!answer) answer = (double*)malloc(TOTAL_SIZE * sizeof(double));
    if (index < TOTAL_SIZE) answer[index++] = sqrt(*(double*)num);
    return answer;
}

void* display_result(double* res, int size) {
    if (!res) return NULL;
    int i = 0;
    while (i < size) {
        printf("%.2lf  ", res[i]);
        i++;
    }
    printf("\n");
    return res;
}

int main(void) {
    double* result = NULL;
    for (double num = 1.0; num <= 10.0; num++) {
        result = func(&num);
        if (display_result(result, (int)num))
            ;
    }
    free(result);
    return 0;
}