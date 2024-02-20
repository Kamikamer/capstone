    cmake_minimum_required(VERSION 3.28)
    project(capstone C)

    set(CMAKE_C_STANDARD 11)
    set(CMAKE_CXX_STANDARD 11)
    set(CMAKE_TOOLCHAIN_FILE "D:/Private/Github/vcpkg/scripts/buildsystems/vcpkg.cmake")


    find_package(CURL REQUIRED)
    find_package(cJSON CONFIG REQUIRED)

    add_executable(Updater ../posture_fit_development/Updater.c)

    target_link_libraries(Updater PRIVATE ${CURL_LIBRARIES} cjson)
    include_directories(${CURL_INCLUDE_DIR})