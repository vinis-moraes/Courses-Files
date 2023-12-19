#include <iostream>

void functionExample(){

    // Stack memory is used for automatic storage duration variables, such as local variables and function call data. Stack memory is managed by the compiler, and it’s allocation and deallocation are done automatically
    int x = 10; // x is stored in the stack memory
}

void functionExample2(){

    // Heap memory is used for dynamic storage duration variables, such as objects created using the new keyword. The programmer has control over the allocation and deallocation of heap memory using new and delete operators
    int* p = new int; // dynamically allocated int in heap memory
    *p = 10;
    delete p; // deallocate memory
}

void functionExample3(){

    // The Data segment is composed of two parts: the initialized data segment and the uninitialized data segment. The initialized data segment stores global, static, and constant variables with initial values, whereas the uninitialized segment stores uninitialized global and static variables
    // Initialized data segment
    int globalVar = 10; // global variables
    static int staticVar = 10; // static local variables
    const int constVar = 10; // constant variables with value

    // Uninitialized data segment
    int unglobalVar; // uninitialized global variables
}

void functionExample4() {
    // The machine code for this function is stored in the code segment.
}

int main (void){
    std::cout << "This program has no output. Read its code instead." << std::endl;
}