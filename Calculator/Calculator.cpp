#include <iostream>
#include <stdio.h>
#include <cstdlib>
#include <math.h>

using namespace std;

int main(){
    float num1, num2;
    float num3;
    cout << "Enter num1:";
    cin >> num1;
    cout << "Enter num2:";
    cin >> num2;

    char selection;
    cout << "Enter selection from +,-,*,/,%,^ :";
    cin >> selection;
    
    switch (selection){       
        
        case '+':
            cout << num1 + num2;
            break;
         
        
        case '-':
            cout << num1 - num2;
            break;
         
        
        case '*':
            cout << num1 * num2;
            break;
         
        
        case '/':
            cout << num1 / num2;
            break;

        case '%':
        num3 = num1/num2;
            if (num3<0){
                num3 = -num3;
            }
            cout << num3;
            break;
        case '^':
            cout << pow(num1,num2);
            break;
        
        default:
            cout << "Error! operator is not correct";
            
    }
    
    return 0;
}
