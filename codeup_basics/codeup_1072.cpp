#include <stdio.h>

int main() {
    int n, a;
    scanf("%d", &n);
reload:
    scanf("%d", &a);
    printf("%d\n", a);
    if(n-- > 1) goto reload;
}