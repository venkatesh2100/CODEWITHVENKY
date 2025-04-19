#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;
class Solution {
public:
  vector<string> findAllRecipes(vector<string> &recipes,
                                vector<vector<string>> &ingredients,
                                vector<string> &supplies) {

    vector<string> res;
    vector<string> notcreated;
    vector<vector<string>> noting;

    set<string> setsup(supplies.begin(), supplies.end());
    // add the stuff of notcreated.
    for (int i = 0; i < recipes.size(); i++) {
      bool boo = true;
      for (const string &ing : ingredients[i]) {
        if (setsup.find(ing) == setsup.end()) {
          boo = false;
          notcreated.push_back(recipes[i]);
          noting.push_back(ingredients[i]);
          break;
        }
      }
      if (boo == true) {
        res.push_back(recipes[i]);
        setsup.insert(recipes[i]);
      }
    }

    // remain part
    bool breakpoint = true;
    while (breakpoint) {
      vector<int> new_rec;
      for (int i = 0; i < notcreated.size(); i++) {
        bool boo = true;
        for (const string &ing : noting[i]) {
          if (setsup.find(ing) == setsup.end()) {
            boo = false;
            break;
          }
          if (boo == true) {
            res.push_back(notcreated[i]);
            setsup.insert(notcreated[i]);
            new_rec.push_back(i);
          }
        }
        if (new_rec.empty()) {
          breakpoint = false;
          break;
        }
        for (auto it = new_rec.rbegin(); it != new_rec.rend(); it++) {
          notcreated.erase(notcreated.begin() + *it);
          noting.erase(noting.begin() + *it);
        }
      }
    }
    r turn res;
  }
};
