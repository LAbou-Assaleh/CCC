//
//  main.cpp
//  s1
//
//  Created by Leonard Abou-Assaleh on 2024-08-17.
//
#include <bits/stdc++.h>
using namespace std;

int first_line(int day1, int last){
    int end_day = 8 - day1;
    cout << "  ";
    for(int a = 1; a < day1; a++){
        cout << "    ";
    }
    cout << 1;
    for(int b = 2; b <= end_day; b++){
        cout << setw(4) << b;
    }
    cout << endl;
    /*cout << setw(3) << end_day + 1;
     for(int i = end_day + 2; i <= end_day + 7; i++){
         cout << setw(4) << i;
     }
     cout << endl;
     end_day += 7;*/
    for(int c = 8 - day1; c <= last; c++){
        cout << setw(3) << end_day + 1;
        if(end_day == last - 1){
            cout << endl;
            return 0;
        }
        for(int i = end_day + 2; i <= end_day + 7; i++){
            cout << setw(4) << i;
            if(i == last){
                cout << endl;
                return 0;
            }
        }
        cout << endl;
        end_day += 7;
    }
    return 0;
}
int main() {
    cout << "Sun Mon Tue Wed Thr Fri Sat" << endl;
    int day = 6;
    int last_day = 0;
    cin >> day;
    cin >> last_day;
    first_line(day, last_day);
    return 0;
}
