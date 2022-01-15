#include <memory>
#include <iostream>
#include <vector>
#include <fstream>

#include "id.h"

bool validate(Passport *pass) {
  bool valid = true;
  for (auto key : required_keys) {
    valid &= pass->contains(key);
  }
  return valid;
}

int main(int argc, char *argv[]) {
  std::string line;
  std::ifstream input("../../d4/d4.txt");
  unsigned int count = 0;
  std::vector<std::string> id;
  std::vector<Passport *> passports;
  if (input.is_open()) {
    while (getline(input, line)) {
      if(line == "") {
        passports.push_back(new Passport(id));
        id.clear();
      } else {
        id.push_back(line);
      }
    }
    passports.push_back(new Passport(id));
  } else {
    std::cerr << "Input file not open" << std::endl;
    return -1;
  }
  input.close();

  for(auto pass : passports) {
    if(validate(pass)) {
      count++;
    }
  }

  std::cout << "Valid IDs: " << count << std::endl;
  return 0;
}