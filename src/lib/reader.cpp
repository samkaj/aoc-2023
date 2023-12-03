#include "reader.h"
#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>

void print(std::string s) {
  std::cout << s << "\n";
}


std::vector<std::string> get_lines(std::string path) {
  std::vector<std::string> lines;
  std::ifstream file(path);
  if (!file) {
    return lines;
  }

  std::string line;
  while (std::getline(file, line)) {
    lines.push_back(line);
  }
  file.close();

  return lines;
}


void print_lines(std::vector<std::string> lines) {
  std::for_each(lines.begin(), lines.end(), print);
}
