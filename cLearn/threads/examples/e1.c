#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

void* func(void* num) {
    int count = *(int*)num;
    for (int i = 1; i <= 5; i++) printf("Hello, World (thread %d)\n", count);
    return NULL;
}

int main(void) {
    // i am comment
    pthread_t th_id[10];
    int res;
    for (int i = 0; i < 10; i++) {
        if (res = pthread_create(&th_id[i], NULL, func, &i)) {
            perror("Thread Creation Failed ! Exiting.....\n");
            exit(EXIT_FAILURE);
        }
    }
    for (int i = 0; i < 10; i++) {
        pthread_join(th_id[i], NULL);
        printf("Thread with ID %lu completed\n", th_id[i]);
    }
    return 0;
}