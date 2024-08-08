#include <stdio.h>
#include <stdlib.h>
// #include <unistd.h>

int main(void) {
    FILE *original = fopen("cool.webp", "rb");
    if (!original) {
        fprintf(stderr, "Error Opening Original File!\n");
        exit(EXIT_FAILURE);
    }
    FILE *copy = fopen("cool_copy.webp", "wb");
    if (!copy) {
        fprintf(stderr, "Could Not Open Copy File!\n");
        exit(EXIT_FAILURE);
    }

    // fgetc
    // fgets
    // fscanf
    // fread

    int c = 0, i = 0, N = 1024, w_times = 0;
    char buffer_chunk[N];
    for (int i = 0; i < 1024; i++) buffer_chunk[i] = 0;
    while (1) {
        c = fgetc(original);
        // if content in file
        if (c != EOF) {
            if (i == N) {
                // if buffer full write in file
                fwrite(buffer_chunk, sizeof(char), i, copy);
                // reset buffer pointer to 0th pos
                i = 0;
                // clean the buffer
                for (int i = 0; i < 1024; i++) buffer_chunk[i] = 0;
            }
            // fill buffer with current char
            buffer_chunk[i++] = c;
        }

        // if pointer is end of reading file, write existing content and get out
        if (feof(original)) {
            if (i) {
                fwrite(buffer_chunk, sizeof(char), i, copy);
            }
            fclose(original);
            fclose(copy);
            break;
        }
    }
    return 0;
}