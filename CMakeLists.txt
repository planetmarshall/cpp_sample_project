cmake_minimum_required(VERSION 3.21)

project(SampleProject)

if (MSVC)
    add_compile_options(/W4 /permissive-)
else()
    add_compile_options(-Wall -Wpedantic -Wextra)
    if (CMAKE_CXX_COMPILER_ID MATCHES "Clang$")
        add_compile_options(-Wconversion -Wconditional-uninitialized)
    endif()
endif()

find_package(Boost REQUIRED COMPONENTS program_options)
find_package(range-v3 REQUIRED)

enable_testing()
find_package(Catch2 REQUIRED)

add_subdirectory(src)
add_subdirectory(app)
add_subdirectory(test)

