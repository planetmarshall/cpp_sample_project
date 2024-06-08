cmake_minimum_required(VERSION 3.24)

project(SampleProject LANGUAGES CXX)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

set(CMAKE_CXX_STANDARD 23)

if (MSVC)
    add_compile_options(/W4 /permissive-)
else()
    add_compile_options(-Wall -Wpedantic -Wextra)
    if (CMAKE_CXX_COMPILER_ID MATCHES "Clang$")
        add_compile_options(-Wconversion -Wconditional-uninitialized)
    endif()
endif()

find_package(CLI11 REQUIRED)
set_property(GLOBAL PROPERTY CTEST_TARGETS_ADDED 1)
enable_testing()
find_package(Catch2 REQUIRED)

add_subdirectory(src)
add_subdirectory(app)
add_subdirectory(test)

