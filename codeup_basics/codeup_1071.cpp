#include <stdio.h>

int main() {
    int a;
reload:
    scanf("%d", &a);
    
    if(a != 0){
        printf("%d\n", a);
        goto reload;
    } 
    
}