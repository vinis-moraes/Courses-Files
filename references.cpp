#include <iostream>

int main (void){
    int num = 10;
    int &ref = num;
    std::cout << ref << std::endl;
}