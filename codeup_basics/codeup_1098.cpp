#include <stdio.h>

int main() {
    int xSize, ySize, numOfStick;
    int board[100][100] = {};

    scanf("%d %d", &xSize, &ySize);
    scanf("%d", &numOfStick);

    for(int j=0; j< numOfStick; j++){
        int len, dim, x, y;
        scanf("%d %d %d %d", &len, &dim, &x, &y);
        for(int i=0; i<len; i++){
            if(dim == 0){
                board[x-1][y-1+i] = 1;          
            } else {
                board[x-1+i][y-1] = 1; 
            }
        }
    }

    for(int x=0; x<xSize; x++){
        for(int y=0; y<ySize; y++) {
            printf("%d ", board[x][y]);
        }
        printf("\n");
    }

}