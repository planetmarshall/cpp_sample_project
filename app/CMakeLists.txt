add_executable(eulerapp main.cpp)

target_link_libraries(eulerapp
        PRIVATE
            Euler::Euler
            CLI11::CLI11
        )

install(TARGETS eulerapp RUNTIME DESTINATION bin)
