#include <stdio.h>

int main() {
    char a;
    char b = 'a';
    scanf("%c", &a);
    do {
        printf("%c ", b);
    } while(b++ < a);   
}