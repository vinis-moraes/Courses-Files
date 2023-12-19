#include <iostream>

int main (void){
    int num = 10;
    int &ref = num;
    std::cout << ref << std::endl;

    ref = 30;
    std::cout << num << std::endl;
}