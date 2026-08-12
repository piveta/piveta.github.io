#include <iostream>
#include <vector>

int main() {
    int size = 10;
    std::vector<int> v(size);
    for (int i = 0; i < size; i++)
        v[i] = i;
    for (int i = 0; i < size; i++)
        std::cout << "v[" << i << "] = " << v[i] << '\n';
}
