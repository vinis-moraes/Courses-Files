#include <iostream>


int add (int a, int b){
    return a + b;
}


int main (void){
    int (*funcptr) (int, int) = add;

    std::cout << "A soma é: " << funcptr(4,5) << std::endl;
}