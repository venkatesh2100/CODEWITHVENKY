#include <iostream>
#include <queue>
#include <type_traits>
using namespace std;
class Solution {
public:
    bool canChange(string start, string target) {
        queue<pair<char,int>> sq , tq;

        for(int i=0;i<start.size();i++){
            if(start[i]!='_') sq.push({start[i],i});
            if(target[i]!='_') tq.push({target[i],i});
        }


        if(sq.size()!=tq.size()) return false;

        while (!sq.empty()) {
          auto [sstr , sint] = sq.front();
          auto [tstr ,tint] = tq.front();
          tq.pop();
          sq.pop();
          if(sstr!=tstr || sstr=='L' && sint < tint || sstr =='R' && sint > tint) return false;

        }
        return true;
    }
};
