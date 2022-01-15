#pragma once
#include <string>

class Password {
  public:
    unsigned int  _first;
    unsigned int  _second;
    char          _letter;
    std::string   _password;
    bool          _is_valid;

    Password(std::string passline);
    std::string to_string();
};