#include <memory>
#include <iostream>
#include <fstream>
#include <vector>

std::vector<std::pair<int,int>> slopes = {{1,1}, {3,1}, {5,1}, {7,1}, {1,2}};

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

  std::vector<int> results;
  for(auto slope : slopes) {
    int count = 0;
    int sideways = 0;
    for(int i = 0; i < forest.size(); i += slope.second) {
      if(forest.at(i)[sideways % forest.at(i).size()] == '#')
        count++;
      
      sideways += slope.first;
    }
    results.push_back(count);
  }

  unsigned int result = 1;
  for (int res : results) {
    result *= res;
  }

  std::cout << "Tree Multiplication: " << result << std::endl;
  return 0;
}