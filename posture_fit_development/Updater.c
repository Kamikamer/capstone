#include <curl/curl.h>
#include <execinfo.h>
#include <json-c/json.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#ifdef _WIN32
#include <windows.h>
#else
#include <signal.h>
#endif

void downloadExe();
size_t write_cb(char *ptr, size_t size, size_t nmemb, void *data);

struct memory {
    char *response;
    size_t size;
};

int main(int argc, char** argv) {
	if (argc <= 1) {
		printf("ABORTING: PID not given\n");
		return -1;
	}
    else if (argc <= 2) {
        printf("ABORTING: PID || Runtime_Type not given\n");
        return -1;
    }

	const long int pid = strtol(argv[1], NULL, 10);
    char exe_path[260]; 
    char s[260];
    strcpy(exe_path, argv[2]);

	printf("PID-c: %ld\n", pid); 
	printf("Current Directory: %s\n", exe_path); 

    chdir(exe_path);
    downloadExe();

	#ifdef _WIN32
            const auto explorer = OpenProcess(PROCESS_TERMINATE, false, pid);
            TerminateProcess(explorer, 1);
            CloseHandle(explorer);
	#else
		kill(pid, 9);
	#endif
	return 0;
}

void downloadExe() {
    curl_global_init(CURL_GLOBAL_ALL);

    CURL *curl = curl_easy_init();
    struct memory chunk = {0};

    if (!curl) {
        fprintf(stderr, "Failed to initialize libcurl\n");
    }
    
    curl_easy_setopt(curl, CURLOPT_DEFAULT_PROTOCOL, "https");
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_cb);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)&chunk);
    curl_easy_setopt(curl, CURLOPT_URL, "https://api.github.com/repos/kamikamer/capstone/releases/latest");

    CURLcode res = curl_easy_perform(curl);
    
    if (res != CURLE_OK) {
 //       fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
        printf("MEOW NO CURL GOOD");
        return;
    }
    
    curl_easy_cleanup(curl);

    const char *response_data = chunk.response;

    struct json_object *root = json_tokener_parse(chunk.response);

    if (!root) {
        fprintf(stderr, "Error parsing JSON\n");
        free(chunk.response);
        return;
    }


    struct json_object *assets;
    // if (!json_object_object_get_ex(root, "assets", &assets) || !json_object_is_type(assets, json_type_array)) {
       // fprintf(stderr, "No assets found in JSON\n");
    //    json_object_put(root);
      //  free(chunk.response);
        //return;
//    }
    



//    printf("The json string:\n\n%s\n\n", json_object_to_json_string(root));
}

size_t write_cb(char *ptr, size_t size, size_t nmemb, void *userdata) {
    FILE *output = (FILE *)userdata;
    return fwrite(ptr, size, nmemb, output);
}
