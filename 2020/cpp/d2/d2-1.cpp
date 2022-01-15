#include <memory>
#include <iostream>
#include <vector>
#include <fstream>
#include "password.h"

int main(int argc, char *argv[]) {
  std::string line;
  std::ifstream input("../../d2/d2.txt");
  unsigned int count = 0;
  if (input.is_open()) {
    while (getline(input, line)) {
      bool is_valid = false;
      Password *pass = new Password(line);
      int char_count = 0;
      for(auto val : pass->_password) {
        if(val == pass->_letter)
          char_count++;
      }

      if(char_count >= pass->_first && char_count <= pass->_second)
        is_valid = true;

      if(is_valid)
        count++;
    }
  } else {
    std::cerr << "Input file not open" << std::endl;
    return -1;
  }
  input.close();

  std::cout << "Total Valid Passwords: " << count << std::endl;
  return 0;
}