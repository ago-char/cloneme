// install library
// sudo apt-get install libmicrohttpd-dev
#include <microhttpd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define PORT 80

static int request_handler(void *cls, struct MHD_Connection *connection,
                           const char *url, const char *method,
                           const char *version, const char *upload_data,
                           size_t *upload_data_size, void **con_cls) {
    if (strcmp(method, "POST") == 0 && strcmp(url, "/log") == 0) {
        struct MHD_PostProcessor *pp;
        const char *data;
        size_t size;

        pp = MHD_create_post_processor(connection, 1024,
                                       &MHD_post_data_iterator, NULL);
        if (!pp) return MHD_NO;

        MHD_get_connection_values(connection, MHD_GET_ARGUMENT_KIND,
                                  &print_out_key, NULL);
        MHD_destroy_post_processor(pp);

        return MHD_YES;
    }

    // Respond with a simple message for other URLs or methods
    const char *page =
        "<html><body>Server is running. This endpoint supports POST requests "
        "to /log.</body></html>";
    struct MHD_Response *response = MHD_create_response_from_buffer(
        strlen(page), (void *)page, MHD_RESPMEM_PERSISTENT);
    int ret = MHD_queue_response(connection, MHD_HTTP_OK, response);
    MHD_destroy_response(response);
    return ret;
}

int main() {
    struct MHD_Daemon *daemon;

    daemon = MHD_start_daemon(MHD_USE_SELECT_INTERNALLY, PORT, NULL, NULL,
                              &request_handler, NULL, MHD_OPTION_END);
    if (!daemon) {
        fprintf(stderr, "Failed to start server.\n");
        return 1;
    }

    printf("Server running on port %d...\n", PORT);
    getchar();  // Press Enter to stop the server

    MHD_stop_daemon(daemon);
    return 0;
}

// create exe and start the server
