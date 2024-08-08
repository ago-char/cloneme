#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct _2int {
    int a, b;
} _2ints;

void* sum(void* nums) {
    _2ints numbers = *(_2ints*)nums;
    int* result = (int*)malloc(sizeof(int) * 1);
    result[0] = numbers.a + numbers.b;
    return result;
}

int main(void) {
    pthread_t th_id;
    int* result;
    int a, b;
    printf("Gibme 2 nums to add : \n");
    scanf("%d%d", &a, &b);
    _2ints numbers = {a, b};
    if (pthread_create(&th_id, NULL, sum, &numbers)) {
        perror("Error Creating Thread\n");
        exit(EXIT_FAILURE);
    }
    /* the second arg of pthread_join is actually for storing result of start
     * routine func in this case it is sum func*/
    pthread_join(th_id, (void**)&result);
    printf("result = %d\n", *result);
    return 0;
}