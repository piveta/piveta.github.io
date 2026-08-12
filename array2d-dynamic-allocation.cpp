#include <iostream>
#include <vector>

int main() {
    int lines = 3;
    int columns = 4;
    std::vector<std::vector<int>> v(lines, std::vector<int>(columns));
    for (int i = 0; i < lines; i++)
        for (int j = 0; j < columns; j++)
            v[i][j] = i * columns + j;
    for (int i = 0; i < lines; i++)
        for (int j = 0; j < columns; j++)
            std::cout << "v[" << i << "][" << j << "] = "
                      << v[i][j] << '\n';
}