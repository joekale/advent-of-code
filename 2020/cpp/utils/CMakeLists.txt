project("advent-of-code-2020-utils")
file(
  GLOB_RECURSE src_files
  RELATIVE "${CMAKE_CURRENT_SOURCE_DIR}" "*.cpp" "*.c"
)
add_library(${PROJECT_NAME} STATIC ${src_files})

target_include_directories(
  ${PROJECT_NAME}
  PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}
)
