#include <bits/stdc++.h> 
using namespace std;
int main() {
	int number_of_divisibility_test, dividend;
	cin >> number_of_divisibility_test >> dividend;
	int count_of_divisible_number = 0;

	for (int i = 0; i < number_of_divisibility_test; i++) {
		int divisor;
		cin >> divisor;
		
		if (divisor % dividend == 0) {
			count_of_divisible_number++;
		}		
	}

	
	cout << count_of_divisible_number << "\n";	
		
	return 0;
}
