#define _POSIX_C_SOURCE 200112L
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

#define thread_count 2

pthread_barrier_t barr1;

int i, j;

void* func1(void* arg) {
    while (i < __INT_MAX__) {
        i++;
        if (pthread_barrier_wait(&barr1) == PTHREAD_BARRIER_SERIAL_THREAD) {
            printf("In func1 : Barrier Reached. 'i' = %d and 'j' = %d\n", i, j);
            break;
        }
    }
    return NULL;
}

void* func2(void* arg) {
    while (j < __INT_MAX__) {
        j++;
        if (pthread_barrier_wait(&barr1) == PTHREAD_BARRIER_SERIAL_THREAD) {
            printf("In func2 : Barrier Reached. 'i' = %d and 'j' = %d\n", i, j);
            break;
        }
    }
    return NULL;
}

int main() {
    pthread_barrier_init(&barr1, NULL, thread_count);
    pthread_t th_id[2];
    void* (*function)(void*) = func1;
    for (int i = 0; i < 2; i++) {
        if (i == 1) function = func2;
        if (pthread_create(&th_id[i], NULL, function, NULL)) {
            fprintf(stderr, "Error Creation of thread%d.Exiting.....\n", i + 1);
            exit(EXIT_FAILURE);
        }
    }
    printf(
        "In main : Just Before barrier destroy. Value of 'i' = %d and 'j' = "
        "%d\n",
        i, j);
    pthread_barrier_destroy(&barr1);
    printf(
        "In main : Just After barrier destroy and Just before joining 2 "
        "threads. Value of 'i' = %d and 'j' = "
        "%d\n",
        i, j);
    for (int i = 0; i < 2; i++) {
        pthread_join(th_id[i], NULL);
    }
    printf(
        "In main : Just After joining threads and Just before Program ends. "
        "Value of 'i' = %d and 'j' = "
        "%d\n",
        i, j);

    // Your code here
    return 0;
}