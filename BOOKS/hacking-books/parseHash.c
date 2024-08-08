#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* getline(char*buffer,int size,FILE*fp){
    if(buffer&&fp&&size>0){
        int count=0;
        int c=fgetc(fp);
        count++;
        if(c!=EOF)
    }
}

int main(void) {
    // just opened just no check done
    FILE* orginal = fopen("hash.txt", "r");
    FILE* hash = fopen("hash_only.txt", "w");

    char buffer[100];
    memset(buffer, 0, 100);

    char* token = NULL;
    char delm[] = ":";
    int len = 0, wirte_time = 0;

    while (1) {
        if (fgets(buffer, 99, orginal)) {
            // printf("in\n");
            token = strtok(buffer, delm);
            if (token) {
                puts(token);
                token = strtok(NULL, delm);
                len = strlen(token);
                if (token && len > 0) {
                    puts(token);
                    strncpy(buffer, token, len);
                    if (strlen(buffer) == 64) {
                        if (wirte_time == 0) {  // first time writing
                            fprintf(hash, "%s", buffer);
                            wirte_time++;
                        } else
                            fprintf(hash, "\n%s", buffer);
                    }
                }
            }
        }
        if (feof(orginal)) {
            printf("end\n");
            fclose(orginal);
            fclose(hash);
            break;
        };
    }

    return 0;
}