#include <functional>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
class Solution {
private:
  unordered_map<string, bool> can_cook;
  unordered_map<string, int> rec_index;
  vector<vector<string>> ing;

  bool dfs(string r) {
    if (can_cook.count(r)) {
      return can_cook[r];
    }
    can_cook[r] = false;
    if (!rec_index.count(r)) {
      return false;
    }

    for (const string &nei : ing[rec_index[r]]) {
      if (!dfs(nei)) {
        return false;
      }
    }

    can_cook[r] = true;
    return can_cook[r];
  }

public:
  vector<string> findAllRecipes(vector<string> &recipes,
                                vector<vector<string>> &ingredients,
                                vector<string> &supplies) {
    vector<string> result;
    ing = ingredients;

    // TODO: Build a DFS function that helps to iterate over the ing and recp
    for (int i = 0; i < supplies.size(); i++) {
      can_cook[supplies[i]] = true;
    }

    for (int i = 0; i < recipes.size(); i++) {
      rec_index[recipes[i]] = i;
    }

    for (const string &r : recipes) {
      if (dfs(r)) {
        result.push_back(r);
      }
    }

    return result;
  }
};