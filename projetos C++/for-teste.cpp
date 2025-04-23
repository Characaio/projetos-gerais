#include <iostream>

int main(){
    std::cout << "hello world" << std::endl;
    int array[10] = {1,2,3,4,5,6,7,8,9,10};
    for (int i = 0, j = 1; i < 10 && j <= 11; i++, j++){
        try
        {
            std::cout << "i = " << i  << ",j = " << j << "\n";
            if (array[i] < 10 && array[j] < 10 ){
            std::cout <<"the item of I is " << array[i] << ", the item of J is " << array[j] << "\n";
            }
        }
        catch(const std::exception& e)
        {
            std::cerr << e.what() << '\n';
        }
        
    }
    return 0;
}