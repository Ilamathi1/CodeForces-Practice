#include<bits/stdc++.h>
using namespace std;

string SearchHard(int n ,int arr[]){
	for(int i = 0;i<n;i++){
		if(arr[i]!=0) return "HARD";
	}
	return "EASY";
}

int main() {
	int n;
	cin >> n;
	int arr[n];
	for(int i=0;i<n;i++){
		cin >> arr[i] ;
	}
	cout << SearchHard(n,arr);
	return 0;
}

