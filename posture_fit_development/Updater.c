#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>
// #include "cjson/cJSON.h" // Include cJSON header

size_t read_callback(char *ptr, size_t size, size_t nitems, void *userdata);
static size_t cb(void *data, size_t size, size_t nmemb, void *clientp);
struct version read_version(char *data);
const char* to_numeric_bool(const int value);

struct memory {
    char *response;
    size_t size;
};

struct version {
    char str[10];
    unsigned int major;
    unsigned int minor;
    unsigned int patch;
    uint64_t serialized;
};
int main(int argc, char *argv[]) {
    curl_global_init(CURL_GLOBAL_ALL);

    CURL *curl = curl_easy_init();
    struct memory chunk = {0};

    if (curl) {
        curl_easy_setopt(curl, CURLOPT_DEFAULT_PROTOCOL, "https");
        curl_easy_setopt(curl, CURLOPT_URL, "https://api.kami.wtf/posture_fit/lts_version");
        // curl_easy_setopt(curl, CURLOPT_READFUNCTION, read_callback);
        // curl_easy_setopt(curl, CURLOPT_READDATA, &this);

        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, cb);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)&chunk);
        /* pass in suitable argument to callback */

        CURLcode result = curl_easy_perform(curl);

        if(result == CURLE_OK) {
            // Print the response data

            // Assuming chunk.response contains the JSON response
            const char *response_data = chunk.response;

            // Parse JSON
            // cJSON *root = cJSON_Parse(response_data);
            if (response_data != NULL) {
                struct version latest_release = read_version(response_data);
                struct version ver = read_version("1.2.9");
                struct version app_ver = read_version("1.0.1");
                int requires_update = ver.serialized >= app_ver.serialized;

                printf("Github Version: %s - %llu\n", latest_release.str, latest_release.serialized);
                printf("Fake Github Version: %s - %llu\n", ver.str, ver.serialized);
                printf("Fake App Version: %s - %llu\n", app_ver.str, app_ver.serialized);

                if (argc <= 1) {
                    (void)system("C:\\Windows\\notepad.exe");
                    printf("Notepad has closed");
                    return;
                } else {
                    printf("Total arguments received: %d\n", argc);
                    for (int i = 0; i < argc; ++i) {
                        printf("%s\n", argv[i]);
                    }
                }

                printf("Requires an update: %s\n", to_numeric_bool(requires_update));
                // Free cJSON root
                // can u make a version w/o response_data rq, i wanna test if it works with say 1.2.7
                // it takes any char array!
            } else {
                printf("Error retrieving data from server: %s\n", response_data);
            }
        } else {
            // Handle request failure
            fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(result));
        }

        free(chunk.response);

        curl_easy_cleanup(curl);
    }
    return 0;
}

size_t read_callback(char *ptr, size_t size, size_t nmemb, void *userdata) {
    FILE *readhere = (FILE *)userdata;
    curl_off_t nread;

    /* copy as much data as possible into the 'ptr' buffer, but no more than
       'size' * 'nmemb' bytes! */
    size_t retcode = fread(ptr, size, nmemb, readhere);

    nread = (curl_off_t)retcode;

    fprintf(stderr, "*** We read %" CURL_FORMAT_CURL_OFF_T
            " bytes from file\n", nread);
    printf("MEOW\n");
    return retcode;
}

static size_t cb(void *data, size_t size, size_t nmemb, void *clientp)
{
    size_t realsize = size * nmemb;
    struct memory *mem = (struct memory *)clientp;

    char *ptr = realloc(mem->response, mem->size + realsize + 1);
    if(!ptr)
        return 0;  /* out of memory! */

    mem->response = ptr;
    memcpy(&(mem->response[mem->size]), data, realsize);
    mem->size += realsize;
    mem->response[mem->size] = 0;

    return realsize;
}

struct version read_version(char *data) {
    char data_copy[10] = {0};
    strcpy_s(data_copy, 10, data);

    char* tokens[3];  // Array to store the tokens
    const char* tok = strtok(data_copy, ".");

    int i = 0;
    while (tok != NULL && i < 3) {
        tokens[i] = tok;
        tok = strtok(NULL, ".");
        i++;
    }

    struct version ver = {
        .major = tokens[0][0] - '0',
        .minor = tokens[1][0] - '0',
        .patch = tokens[2][0] - '0',
        .serialized = ver.major*1000000LL + ver.minor*10000 + ver.patch*100
    };
    strcpy_s(ver.str, 10, data);

    return ver;
}

const char* to_numeric_bool(const int value) {
    return value ? "true" : "false";
}
