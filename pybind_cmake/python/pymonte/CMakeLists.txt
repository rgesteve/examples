find_package(pybind11 CONFIG REQUIRED)

if (pybind11_FOUND)
    message(STATUS "Found pybind... should work ok")
else()
    message(ERROR "Couldn't find pybind")
endif()

message(STATUS "Done!!")
