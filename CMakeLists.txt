cmake_minimum_required(VERSION 3.28)
project(capstone C)

set(CMAKE_C_STANDARD 11)
add_executable(Updater posture_fit_development/Updater.c)

find_library()