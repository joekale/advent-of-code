#include <iostream>
#include <vector>
#include <fstream>

int main(int argc, char *argv[]) {
  //parse_cmdline(argc, argv);

  std::vector<int> vals;
  std::string line;
  std::ifstream input("../../d1/d1.txt");
  if (input.is_open()) {
    while (getline(input, line)) {
      vals.push_back(std::stoi(line));
    }
  } else {
    std::cerr << "Input file not open" << std::endl;
  }
  input.close();

  bool found = false;
  for(int i = 0; i < vals.size(); i++) {
    for(int j = 0; j < vals.size(); j++) {
      if ( i == j)
        continue;

      for (int k = 0; k < vals.size(); k++) {
        if ( i == k || j == k)
          continue;

        int vali = vals.at(i);
        int valj = vals.at(j);
        int valk = vals.at(k);

        if (vali + valj + valk == 2020) {
          std::cout << vali << " x " << valj << " x " << valk << " = " << vali*valj*valk << std::endl;
          found = true;
          break;
        }
      }

      if(found)
        break;
    }

    if(found)
      break;
  }

  return 0;
}