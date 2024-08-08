#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 70

typedef struct fileInfo {
    char* path;
    int lineNum;
} fInfo;

fInfo* create_fInfo(char* file, int line) {
    fInfo* p = (fInfo*)malloc(sizeof(fInfo));
    if (p) {
        p->path = (char*)malloc(sizeof(strlen(file) + 1));
        p->path = file;
        // strcpy(p->path, file);
        if (line < 0)
            p->lineNum = -line;
        else
            p->lineNum = line;
        return p;
    }
    return NULL;
}

void destroy_fInfo(fInfo* p) { free(p); }

void* getContent(void* file_info) {
    fInfo* file = (fInfo*)file_info;
    FILE* fp = fopen(file->path, "r");
    int count = 0;
    char* buff = (char*)malloc(sizeof(char) * SIZE);
    while (fgets(buff, SIZE, fp)) {
        count++;
        if (count == file->lineNum) break;
    }
    fclose(fp);
    if (count == file->lineNum) return buff;
    return NULL;
}

int main(int argc, char const* argv[]) {
    if (argc != 3) {
        printf("Usuage : %s <filePath> <lineNumber>\n", argv[0]);
        exit(EXIT_FAILURE);
    }
    pthread_t th_id;
    char* content = (char*)malloc(sizeof(char) * SIZE);
    int res;
    fInfo* file = create_fInfo((char*)argv[1], atoi(argv[2]));
    if (file) {
        if (res = pthread_create(&th_id, NULL, getContent, file)) {
            printf("Error Creating Thread. Error Reference : %d\n", res);
            exit(EXIT_FAILURE);
        } else {
            pthread_join(th_id, (void**)&content);
            if (content) {
                printf("%s", content);
                free(content);
            } else
                printf("Line No. %d does not exists in '%s'.\n", file->lineNum,
                       file->path);
        }
        destroy_fInfo(file);
    } else {
        perror("Memory Allocation Error to 'fInfo' struct\n");
    }
    return 0;
}