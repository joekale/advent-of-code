#include <memory>
#include <iostream>
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
      if(pass->_password[pass->_first -1] == pass->_letter){
        if(pass->_password[pass->_second -1] != pass->_letter) {
          is_valid = true;
        }
      } else if (pass->_password[pass->_second -1] == pass->_letter) {
        is_valid = true;
      } 
      std::cout << pass->to_string() << ", Valid = " << is_valid << std::endl;
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