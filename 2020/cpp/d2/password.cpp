#include "password.h"
#include <sstream>

Password::Password(std::string passline) {
    int pos = passline.find(" ");
      std::string range = passline.substr(0, pos);
      int dashpos = range.find("-");
      _first = std::stoi(range.substr(0, dashpos));
      _second = std::stoi(range.substr(dashpos + 1, range.size()));

      int lastpos = passline.rfind(" ");
      _password = passline.substr(lastpos +1, passline.size() - lastpos + 1);

      std::string letter = passline.substr(pos + 1, 1); // skip the colon
      _letter = letter[0];
}

std::string Password::to_string(){
    std::ostringstream string_stream;
    string_stream << "First: " << _first << ", Second: " << _second << ", Letter: " << _letter
        << ", Password: " << _password; 
    
    return string_stream.str();
}