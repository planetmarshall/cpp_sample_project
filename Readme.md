Sample C++ Project
==================

![diagnostics status](https://github.com/planetmarshall/cpp_sample_project/actions/workflows/diagnostics.yml/badge.svg)
![build status](https://github.com/planetmarshall/cpp_sample_project/actions/workflows/build.yml/badge.svg)
![docs status](https://github.com/planetmarshall/cpp_sample_project/actions/workflows/docs.yml/badge.svg)

A sample startup project based on modern C++ guidelines. The example code 
implements a solution to the first problem on 
[Project Euler](https://projecteuler.net/about)

Automatically generated [documentation](https://planetmarshall.github.io/cpp_sample_project/)

Quick Start
-----------

1. Checkout the project:
   ```
   $ git clone https://github.com/planetmarshall/cpp_sample_project.git
   $ cd cpp_sample_project
   ```
2. Install conan
   ``` 
   pip install conan --upgrade
   ```
3. Install dependencies. The preset name should match the preset you will use 
   with CMake. Check the `CMakePresets.json` file for the available presets
   or add your own.
   ```
   $ conan install . -if build/<preset> -of build/<preset> --build missing
   ```
4. Configure with CMake
   ```
   $ cmake --preset <preset>
   ```
5. Build
   ```
   $ cmake --build build/<preset>
   ```
6. Run tests
   ```
   $ ctest -vvv build/<preset>
   ```

Continuous Integration
------------------------

The Github Workflow builds and tests the project using the following compilers
and platforms, across both Debug and Release builds using both Shared and Static
libraries.

Compiler warnings are set at a high level (`-Wall -Wpedantic -Wextra -Wconversion -Wconditional-uninitialized` for
GCC and Clang, `/W4 /fpermissive-` for MSVC) and warnings are treated as errors.

### Linux

 * GCC
 * Clang with LLVM libc++

### Windows

 * Visual Studio
 * Visual Studio with Clang-CL

### MacOS

 * Apple Clang on ARM64

In addition, `clang-tidy` is run on any changed files, and documentation is
generated by Sphinx and uploaded to [Github Pages](https://planetmarshall.github.io/cpp_sample_project/)


References
----------

 * [An introduction to modern CMake](https://cliutils.gitlab.io/modern-cmake/)
 * [Effective Modern CMake](https://gist.github.com/mbinna/c61dbb39bca0e4fb7d1f73b0d66a4fd1)
 * [Jason Turner's](https://github.com/lefticus) [C++ Best Practices](https://leanpub.com/cppbestpractices)
