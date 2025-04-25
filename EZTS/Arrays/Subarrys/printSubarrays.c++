#include <cstddef>
#include <iostream>
#include <vector>
using namespace std;

// void printAllSubarrays(const vector<int>& arr) {
//     int n = arr.size();
//     for (int start = 0; start < n; ++start) {
//         for (int end = start; end < n; ++end) {
//             cout << "[ ";
//             for (int i = start; i <= end; ++i) {
//                 cout << arr[i] << " ";
//             }
//             cout << "]\n";
//         }
//     }
// }

//TODO : Backtacking Logic
void backtrack(size_t start ,vector<int>&arr,vector<int>&curr,vector<vector<int>>&res){
    if(!curr.empty()){
        res.push_back(curr);
    }
    if(curr.size() == arr.size()) return;


    // for(size_t i = start;i<arr.size();i++){
        curr.push_back(arr[start]);
        backtrack(start+1,arr,curr,res);
        curr.pop_back();
    // }

};

//?? Generate Logic Helper
void generateSubarryas(vector<int>&arr,vector<vector<int>>&res){
    // for(size_t start=0;start < arr.size();start++){
        vector<int> curr;
        backtrack(0, arr, curr, res);
    // }
}



int main() {
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> res;
    // printAllSubarrays(nums);
    generateSubarryas(nums, res);
    for(auto &code:res){
        for(auto &val:code){
            cout<< val << " ";
        }
        cout << endl;
    }
    return 0;
}
