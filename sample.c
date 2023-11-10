#include <stdio.h>

int main() {
    int a = 5;
    int b = 10;
    int sum = a + b;

    if (sum > 15) {
        // Print the following string if sum is greater than 15
        printf("Sum is greater than 15\n");
    } else {
        // Print the followinng string if sum is less than or equal to 15
        printf("Sum is not greater than 15\n");
    }

    return 0;
}
