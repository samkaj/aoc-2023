#include "../lib/reader.h"
#include <string>
#include <unordered_map>

int find_num(std::string line,
             std::unordered_map<std::string, std::string> patterns);

int main() {
  auto lines = get_lines("/home/samkaj/code/aoc-2023/src/dec01/in.txt");
  std::unordered_map<std::string, std::string> nums;
  // Part one
  nums.insert({"1", "1"});
  nums.insert({"2", "2"});
  nums.insert({"3", "3"});
  nums.insert({"4", "4"});
  nums.insert({"5", "5"});
  nums.insert({"6", "6"});
  nums.insert({"7", "7"});
  nums.insert({"8", "8"});
  nums.insert({"9", "9"});
  int tot = 0;
  for (auto line : lines) {
    tot += find_num(line, nums);
  }
  printf("Part one: %d\n", tot);

  // Part two
  nums.insert({"one", "1"});
  nums.insert({"two", "2"});
  nums.insert({"three", "3"});
  nums.insert({"four", "4"});
  nums.insert({"five", "5"});
  nums.insert({"six", "6"});
  nums.insert({"seven", "7"});
  nums.insert({"eight", "8"});
  nums.insert({"nine", "9"});

  tot = 0;
  for (auto line : lines) {
    tot += find_num(line, nums);
  }
  printf("Part two: %d\n", tot);

  return 0;
}

int find_num(std::string line,
             std::unordered_map<std::string, std::string> patterns) {
  std::string first_digit;
  int i;
  int min = line.length() + 1; 
  for (const auto &pair : patterns) {
    i = line.find(pair.first);
    if (i < min && i != std::string::npos) {
      min = i;
      first_digit = pair.second;
    }
  }

  std::string second_digit;
  int max = -1;
  for (const auto &pair : patterns) {
    i = line.rfind(pair.first);
    if (i > max && i != std::string::npos) {
      max = i;
      second_digit = pair.second;
    }
  }
  std::string digits = first_digit + second_digit;
  return std::stoi(digits);
}
