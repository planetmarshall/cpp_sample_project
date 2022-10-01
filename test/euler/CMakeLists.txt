include(GoogleTest)
add_executable(test_euler
    test_problem_1.cpp)

target_link_libraries(test_euler
    PRIVATE
    Catch2::Catch2WithMain
    Euler::Euler
)

include(CTest)
include(Catch)

message(STATUS "CMAKE_SYSTEM_PROCESSOR: ${CMAKE_SYSTEM_PROCESSOR}")
message(STATUS "CMAKE_HOST_SYSTEM_PROCESSOR: ${CMAKE_HOST_SYSTEM_PROCESSOR}")
message(STATUS "CMAKE_CROSSCOMPILING: ${CMAKE_CROSSCOMPILING}")

if (${CMAKE_SYSTEM_PROCESSOR} STREQUAL ${CMAKE_HOST_SYSTEM_PROCESSOR})
	catch_discover_tests(test_euler)
endif()
