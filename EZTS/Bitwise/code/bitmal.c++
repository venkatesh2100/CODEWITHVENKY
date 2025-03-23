#include <iostream>
#include <bitset>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

//TODO: Converting Integer to Binary .

void intToBinary(int num){
  vector<int> arr;
  
  while (num > 0) {

    arr.push_back(num%2);
    num/=2;
  }
  reverse(arr.begin(),arr.end());
  std::cout << "Binary" <<endl;


  for(int i =0;i<arr.size();i++){
    std::cout << arr[i];
  }
  std::cout << endl;
}

//INFO: Now Converting Bin to Integer:

int  BinarytoInt(vector <int> arr){
  int count  =0; 

  for(int i =0 ; i <arr.size();i++){
    count+= arr[i] * pow(2 ,i);
  }

  return count;
  
}


int main(){
    int num = 7;
    cout << num;
    vector<int> arr = {1,1,1};
    cout << " Binary value :" <<bitset<4>(num) << endl;
  //INFO: Now Implement of function Int to Binary. 
  intToBinary(num);
  int val  = BinarytoInt(arr);
  std::cout <<"Intval: "  <<val<<endl;
}
