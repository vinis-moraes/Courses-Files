#include <iostream>

int main (void){
    int num = 42;
    float pi = 3.14159;

    num = pi; // Atribui apenas a parte inteira de pi ao num

    std::cout << "The value of num is: " << num << std::endl;
    std::cout << "The value of pi is: " << pi << std::endl;

    return 0;
}
