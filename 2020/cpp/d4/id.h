#include <vector>
#include <string>
#include <map>
#include <iostream>

static std::vector<std::string> required_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}; // and "cid" for people outside NP

class Passport {
    private:
        std::map<std::string, std::string> _info;
    
        void push_key_val(std::string substr);
        friend std::ostream& operator<< (std::ostream &out, const Passport &p);

    public:
        Passport(std::vector<std::string> id_lines);
        bool contains(std::string key);
};
