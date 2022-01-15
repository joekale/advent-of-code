#include "cmdline.h"

#include <iostream>

void parse_cmdline(int argc, char *argv[]) {
  std::cout << "command line args";
  for(int i = 1; i < argc; i++){
    std::cout << " " << argv[i];
  }
  std::cout << std::endl;
}