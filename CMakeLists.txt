cmake_minimum_required(VERSION 3.10)

project(SampleProject)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
set(CONAN_CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR})
conan_basic_setup()

if (MSVC)
    add_compile_options(/W4 /permissive-)
else()
    add_compile_options(-Wall -Wpedantic -Wextra -Wconversion)
endif()

enable_testing()
find_package(GTest)

add_subdirectory(src)
add_subdirectory(app)
add_subdirectory(test)

