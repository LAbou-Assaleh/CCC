//============================================================================
// Name        : Surfing.cpp
// Author      : Leonard Abou-Assaleh
//============================================================================

#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
#include <unordered_set>
#include <deque>
using namespace std;
bool bfs(unordered_map < string, vector<string> > dict, string begin, string end){
	unordered_set <string> visited;
	deque <string> queue;
	queue.push_back(begin);
	while (queue.size() > 0){
		string x = queue.front();
		queue.pop_front();
		visited.insert(x);
		for (const auto& link : dict[x]){
			if (not visited.count(link)){
				visited.insert(link);
				queue.push_back(link);
			}
			if (link == end){
				return true;
			}
		}
	}
	return false;
}

int main() {
	unordered_map < string, vector<string> > links;
	int p;
	string x;
	x = "<A HREF=\"";
	int len = x.length();
	cin >> p;
	cin.ignore();
	string temp;
	string temp2;
	vector<string> l;
	for (int i = 0; i < p; i++){
		string base;
		getline(cin, base);
		getline(cin, temp);
		l.clear();
		while (true) {
			if (temp == "</HTML>") {
				break;
			}

			int spot = temp.find(x);
			while (spot != string::npos) {
				int start = spot + len;
				int linkend = temp.find("\">", start);
				if (linkend != string::npos) {
					string link = temp.substr(start, linkend - start);
					l.push_back(link);
					cout << "Link from " << base << " to " << link << endl;
				}
				spot = temp.find(x, linkend + 2);
			}
			getline(cin, temp);
		}
		links[base] = l;
	}
	while (true){
		getline(cin, temp);
		if (temp == "The End"){
			break;
		}else {
			getline(cin, temp2);
			if (bfs(links, temp, temp2)){
				cout << "Can surf from " << temp << " to " << temp2 << "." << endl;
			}else{
				cout << "Can't surf from " << temp << " to " << temp2 << "." << endl;
			}
		}
	}
}


