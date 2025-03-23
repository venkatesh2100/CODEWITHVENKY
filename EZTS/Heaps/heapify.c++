#include <algorithm>
#include <iostream>
/*#include <queue>*/
#include <vector>
using namespace std;

// INFO: Helps to Exchange the New value to Correct pos.
void heapifu(int arr[], int n, int i) {
  int largest = i;
  int l = 2 * i + 1;
  int r = 2 * i + 2;
  if (l<n & arr[l]> arr[largest]) {
    largest = l;
  }
  if (r<n & arr[r]> arr[largest]) {
    largest = r;
  }
  if (largest != i) {
    swap(arr[i], arr[largest]);
    heapifu(arr, n, largest);
  }
}

void heapsort(int arr[], int n) {

  for (int i = n / 2 - 1; i >= 0; i--) {
    heapifu(arr, n, i);
  }

  for (int i = n - 1; i > 0; i--) {
    swap(arr[0], arr[i]);
    heapifu(arr, i, 0);
  }
}
void printHeap(int arr[], int n) {

  for (int i = 0; i < n; i++) {
    cout  <<' ' << arr[i];
  }
  cout << endl;
}


//HACK: Main funciton to Call the Heapsort.
int main() {
  int arr[] = {10, 20, 1000, 30, 0, 1200};
  int n = sizeof(arr) / sizeof(arr[0]);
  cout << "Before sort" << endl;
  printHeap(arr, n);

  cout <<"Heapify"<<endl;
  heapsort(arr, n);

  printHeap(arr, n);
  return 0;
}
