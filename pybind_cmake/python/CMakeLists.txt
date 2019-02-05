message(STATUS "---- testing from python -----")

add_custom_target(python_wheel DEPENDS mclib)

# add_subdirectory(pymonte)
message(STATUS "---- testing done!! -----")
