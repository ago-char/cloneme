#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>  //exit

void* func(void* arg) {
    printf("Inside func Thread !!\n");
    return NULL;
}

int main(void) {
    pthread_t th_id;
    int ret;
    // what if thread is not created (it will return non zero)
    if (ret = pthread_create(&th_id, NULL, func, NULL)) {
        perror("Thread can't be created !\n");
        printf("Error Code : %d\n", ret);
        exit(EXIT_FAILURE);
    }
    // if thread is created what to do in main thread
    printf("Regards from main thread %d!\n", ret);

    // wait for created thread to terminate
    pthread_join(th_id, NULL);

    // last part of main thread
    printf("Created Thread Completed...Main Thread Exiting.......... \n");
    return 0;
}