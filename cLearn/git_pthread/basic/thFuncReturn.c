#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

// this thread function will return 5 times of the int value provided
void* th_func(void* val) {
    int* valTimesFive = (int*)malloc(sizeof(int));
    *valTimesFive = *(int*)val * 5;
    return valTimesFive;
}

int main(void) {
    pthread_t th_id;
    int value = 5;
    void* result;
    // if pthread_create returns Non-Zero then it is error creating thread
    if (pthread_create(&th_id, NULL, th_func, &value)) {
        perror("Thread Creation Error!!\n");
        exit(EXIT_FAILURE);
    }

    // do your task until created thread exits
    printf("In the middle of main thread and new thread!!\n");

    // if thread is successfully created you need to wait till the thread
    // returns (use join func), second argument of join func stores the return
    // value of th_func
    pthread_join(th_id, &result);
    // see the result
    printf("See Result before program ends : %d\n", *(int*)result);
    return 0;
}