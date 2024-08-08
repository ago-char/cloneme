#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct str {
    char* s;
    int len;

   public:
    str(char* p) {
        if (p) {
            len = strlen(p);
            s = (char*)malloc(len + 1);
            strcpy(s, p);
            s[len] = '\0';
        }
    }
    int getlen() { return len; }
    char* getstr() { return (char*)s; }
} string;
