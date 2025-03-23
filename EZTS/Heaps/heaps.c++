#include <algorithm>
#include <cstdlib>
#include <functional>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

// TODO: Implementation of Heaps ALGO.

void NormalQueueApproach() {
  priority_queue<int> maxheap;
  vector<int> arr;
  for (int i = 0; i < 10; i++) {
    arr.push_back(i + 1);
  }
  maxheap.push(-(100));
  maxheap.push(-(50));
  maxheap.push(-(20));
  maxheap.push(-(-20));

  while (!maxheap.empty()) {
    cout << -(maxheap.top()) << endl;
    maxheap.pop();
  }
  std::cout << "Hello to Clangd" << endl;
}
//INFO: <minheap> 
void GreaterQueue() {
  priority_queue<int, vector<int>, greater<int>> minheap;
  for (int i = 0; i < 4; i++) {
    int random = rand();
    minheap.push(random);
  }

  while (!minheap.empty()) {
    cout << minheap.top() << endl;
    minheap.pop();
  }
}

//INFO: <maxheap>
void SmallerQUeues(){
  priority_queue<int , vector<int> , less<int>> maxheap;
  for(int i =0;i<5;i++){
    int random = rand();
    maxheap.push(random);
  }

  while (!maxheap.empty()) {
    std::cout << maxheap.top() <<endl;
    maxheap.pop();
  }
}

int main(){
  /*GreaterQueue();*/
  SmallerQUeues();
}
