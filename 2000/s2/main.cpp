//============================================================================
// Name        : main.cpp
// Author      : Leonard Abou-Assaleh
//============================================================================

#include <iostream>
#include <vector>
using namespace std;
vector<double> river;
void split(int pos, double per){
	river.insert(river.begin() + pos-1, river[pos-1]*(per/100));
	river[pos] *= (100-per)/100;
}
void join(int pos){
	river[pos-1] += river[pos];
	river.erase(river.begin()+pos);
}
int main() {
	int x;
	cin >> x;
	for (int i = 0; i < x; i++){
		double y;
		cin >> y;
		river.push_back(y);
	}
	while (true){
		double in;
		cin >> in;
		if (in == 99){
			int pos;
			cin >> pos;
			double per;
			cin >> per;
			split(pos, per);
		}
		if (in == 88){
			int pos;
			cin >> pos;
			join(pos);
		}
		if (in == 77){
			break;
		}
	}
	for(int i = 0; i < river.size(); i++){
		cout << river[i] << " ";
	}

}
