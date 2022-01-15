#include <memory>
#include <iostream>
#include <vector>
#include <fstream>

int main(int argc, char *argv[]) {
  std::string line;
  std::ifstream input("../../d3/d3.txt");
  std::vector<std::string> forest;
  if (input.is_open()) {
    while (getline(input, line)) {
      forest.push_back(line);
    }
  } else {
    std::cerr << "Input file not open" << std::endl;
    return -1;
  }
  input.close();

  int count = 0;
  int sideways = 0;
  for(int i = 0; i < forest.size(); i++) {
    if(forest.at(i)[sideways % forest.at(i).size()] == '#')
      count++;
    
    sideways += 3;
  }

  std::cout << "Tree Multiplication: " << count << std::endl;
  return 0;
}