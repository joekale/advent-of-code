#include "id.h"

void Passport::push_key_val(std::string substr){
    int col_pos = substr.find(":");
    std::string key = substr.substr(0, col_pos);
    std::string val = substr.substr(col_pos + 1, substr.size() - col_pos);
    _info.insert({key, val});
}

Passport::Passport(std::vector<std::string> id_lines) {
    for(auto line : id_lines) {
        int pos = line.find(" ");
        int pos_last = 0;
        std::string info;
        while(pos < line.size()) {
            info = line.substr(pos_last, pos - pos_last);
            push_key_val(info);
            pos_last = pos +1;
            pos = line.find(" ", pos + 1);
        }
        pos = line.rfind(" "); // get last bit
        info = line.substr(pos+1, line.size() - pos);
        push_key_val(info);
    }
}


std::ostream& operator<< (std::ostream &out, const Passport &p)
{
    out << "Passport {" << std::endl;
    for(auto pair : p._info){
        out << "\t" << pair.first << ": " << pair.second << std::endl;
    }
    out << "}" << std::endl;
 
    return out;
}

bool Passport::contains(std::string key) {
    return _info.contains(key);
}