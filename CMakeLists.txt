cmake_minimum_required(VERSION 3.10)

project(SampleProject)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
message(STATUS ${CMAKE_BINARY_DIR})
conan_basic_setup()
list(APPEND CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR})

if (MSVC)
    add_compile_options(/W4 /permissive-)
else()
    add_compile_options(-Wall -Wpedantic -Wextra -Wconversion)
endif()

enable_testing()
find_package(Catch2 REQUIRED)
find_package(range-v3 REQUIRED)

add_subdirectory(src)
add_subdirectory(app)
add_subdirectory(test)

