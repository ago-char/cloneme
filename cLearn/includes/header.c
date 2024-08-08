#include <stdio.h>
#include <string.h>

#define FIRSTNULL -2
#define EMPTYLINE -3
#define WRONGPARM -4

int myreadline(char* buffer, size_t size) {
    if (!buffer || size < 1) return WRONGPARM;

    size_t i = 0;
    int c, nextchar;
    while (i < size - 1 && (c = fgetc(stdin)) != EOF) {
        // NULL at the beginning of the line (uncommon)
        if (i == 0 && c == '\0') return FIRSTNULL;

        // newline at the beginning of the line (uncommon)
        if (i == 0 && c == '\n') return EMPTYLINE;

        /* myreadline do not intend to put newline in buffer however it reads*/
        if (c != '\n') {
            buffer[i++] = c;
            continue;
        }

        /*if newline is reached after reading break*/
        if (c == '\n') break;
    }
    /*if index is still 0 meaning nothing read it is for sure End Of File or
     * EOF*/
    if (i == 0) return EOF;  //-1

    /*read extra characters which are unwanted from stdin*/
    if (i == size - 1 && c != '\n') {
        while ((c = fgetc(stdin)) != EOF && c != '\n') {
            // do nothing
        }
        // add null terminator as it is last index and return
        buffer[i] = '\0';
        return i;
    }

    /*fill all remaining buffer will NULL terminator*/
    while (i < size) buffer[i++] = '\0';

    return i - 1;  // return final index
}

/*this function reads the whole line and return number of characters written
 * (including newline It writes newline only if it is found
 * at the beginning if buffer has enough space to terminate with NULL else it
 * writes NULl character at first index) in buffer in success and negative value
 * in ERROR or EOF*/
int mygetline(char* buffer, size_t size, FILE* stream) {
    if (!buffer || !stream || size < 1) return WRONGPARM;
    int c;
    size_t i = 0, numofcharRead = 0;
    while ((c = fgetc(stream)) != EOF && c != '\n') {
        /*if first character is NULL then return -3*/
        if (i == 0 && c == '\0') {
            return FIRSTNULL;
        }
        /*if buffer not full availabe put char in buffer*/
        if (i < size - 1) buffer[i++] = c;
    }
    // first character is EOF
    if (i == 0 && c == EOF) return EOF;
    // first character is newline
    if (i == 0 && c == '\n') {
        /*if size is just 1 means new line can not be stored and it must be the
         * null terminator*/
        if (size == 1) {
            buffer[i++] = '\0';
            return i;
        }
        /*if it has enough room then include newline*/
        buffer[i++] = '\n';
    }

    // 'i' characters were read
    numofcharRead = i;

    // add null terminator till the end of buffer
    while (i < size) buffer[i++] = '\0';
    return numofcharRead;
}