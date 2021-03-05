#include <stdio.h>

int main() {
    int map[10][10] = {};

    for(int x=0; x<10; x++){
        for(int y=0; y<10; y++){
            int value;
            scanf("%d", &value);
            map[x][y] = value;
        }
    }

    int sX = 1;
    int sY = 1;
    while(map[sX][sY] != 2) {
        map[sX][sY] = 9;
        if(map[sX][sY+1] == 1){
            if(map[sX+1][sY] == 1){
                break;
            } else {
                sX += 1;
            }
        } else {
            sY += 1;
        }
    };

    map[sX][sY] = 9;

    for(int x=0; x<10; x++){
        for(int y=0; y<10; y++){
            printf("%d ", map[x][y]);
        }
        printf("\n");
    }

}
