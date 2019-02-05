cmake_minimum_required (VERSION 3.1)

project (mclib)

set(SRC MonteCarloPi_lib.cpp)

add_library(mclib SHARED ${SRC})
