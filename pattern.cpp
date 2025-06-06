#include <iostream>
using namespace std;

int main(){

    for(int i = 0; i < 5; i++){
        for(int j = i; j < 5; j++){
            cout << "*";
        }
        cout << endl;
    }

    for(int i = 0; i < 5; i++){
        for(int s = 0; s < i; s++){
            cout << " ";
        }
        for(int j = 0; j < 5 - i; j++){
            cout << "*";
        }
        cout << endl;
    }


    for(int i = 5; i >= 0; i--){
        for(int j = 0; j <= 5 - i; j++){
            cout << "*";
        }
        cout << endl;
    }

    for(int i = 5; i >= 0; i--){
        for(int s = i; s > 0; s--){
            cout << " ";
        }
        for(int j = 0; j <= 5 - i; j++){
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}