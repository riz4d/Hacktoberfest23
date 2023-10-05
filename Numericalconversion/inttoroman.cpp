#include<stdio.h>
#include<iostream>
#include <bits/stdc++.h>
using namespace std;

string intToRoman(int num) {
    string m[] = { "", "M", "MM", "MMM" };
    string c[] = { "",  "C",  "CC",  "CCC",  "CD",
                   "D", "DC", "DCC", "DCCC", "CM" };
    string x[] = { "",  "X",  "XX",  "XXX",  "XL",
                   "L", "LX", "LXX", "LXXX", "XC" };
    string i[] = { "",  "I",  "II",  "III",  "IV",
                   "V", "VI", "VII", "VIII", "IX" };
 
    string thousands = m[num / 1000];
    string hundreds = c[(num % 1000) / 100];
    string tens = x[(num % 100) / 10];
    string ones = i[num % 10];
 
    string ans = thousands + hundreds + tens + ones;
 
    return ans;
    }
int main() {
    int n;
    cin>>n;
    int ar[n];
    for(int i=0;i<n;i++){
    	cin>>ar[i];
		string z=intToRoman(ar[i]);
		cout<<"\""<<z<<"\""<<" ";
	}
}