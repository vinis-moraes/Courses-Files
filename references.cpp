#include <iostream>

void swap (int& a, int& b){
    int temp = a;
    a = b;
    b = temp;  
}

int main (void){
    int num = 10;
    int &ref = num;
    std::cout << ref << std::endl;

    ref = 30;
    std::cout << num << std::endl;

    int x = 2;
    int y = 5;

    std::cout << "Números antes da troca: x = " << x << " e y = " << y << std::endl;
    swap(x,y);
    std::cout << "Números depois da troca: x = " << x << " e y = " << y << std::endl;

}