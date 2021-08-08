include(GoogleTest)
add_executable(test_euler
    main.cpp
    test_problem_1.cpp)

target_link_libraries(test_euler
    PRIVATE
    Catch2::Catch2
    Euler::Euler
)

include(CTest)
include(Catch)

catch_discover_tests(test_euler)
