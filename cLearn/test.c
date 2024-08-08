#include <pthread.h>
#include <stdio.h>

#define NUM_THREADS 3

pthread_barrier_t barrier;  // Declare a barrier variable

void* thread_func(void* thread_id) {
    long tid = (long)thread_id;

    // Perform some work
    printf("Thread %ld is starting...\n", tid);

    // Synchronize at the barrier
    pthread_barrier_wait(&barrier);

    // After synchronization
    printf("Thread %ld continues after barrier\n", tid);

    pthread_exit(NULL);
}

int main() {
    pthread_t threads[NUM_THREADS];
    int rc;
    long t;

    // Initialize barrier with count NUM_THREADS
    pthread_barrier_init(&barrier, NULL, NUM_THREADS);

    // Create threads
    for (t = 0; t < NUM_THREADS; t++) {
        rc = pthread_create(&threads[t], NULL, thread_func, (void*)t);
        if (rc) {
            printf("ERROR; return code from pthread_create() is %d\n", rc);
            return 1;
        }
    }

    // Join threads
    for (t = 0; t < NUM_THREADS; t++) {
        pthread_join(threads[t], NULL);
    }

    // Destroy barrier
    pthread_barrier_destroy(&barrier);

    return 0;
}
