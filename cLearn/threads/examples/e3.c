#include <pthread.h>
#include <stdio.h>
#include <unistd.h>

#define BILLION 1000000000

pthread_mutex_t lock;
int shared_data;
// Usually shared data is more complex than just an int.

void *counter_billion(void *arg) {
    int i;
    for (i = 1; i <= BILLION; ++i) {
        // Access the shared data here.
        // pthread_mutex_lock(&lock);
        shared_data++;
        // pthread_mutex_unlock(&lock);
    }
    return NULL;
}

int main(void) {
    pthread_t threadID;
    void *thread_result;
    int i;

    // Initialize the mutex before trying to use it.
    pthread_mutex_init(&lock, NULL);
    pthread_create(&threadID, NULL, counter_billion, NULL);

    // Try to use the shared data.
    while (shared_data != BILLION) {
        // sleep(1);
        // pthread_mutex_lock(&lock);
        printf("\rCounter Reached = %d\n", shared_data);
        // pthread_mutex_unlock(&lock);
    }

    // printf("\n");
    pthread_join(threadID, &thread_result);
    printf("Counter finally = %d\n", BILLION);

    // Clean up the mutex when we are finished with it.
    pthread_mutex_destroy(&lock);

    return 0;
}
