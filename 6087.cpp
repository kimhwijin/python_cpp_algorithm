#include <iostream>
#include <stdio.h>
using namespace std;


char map[101][101];
int w,h;

int main(){
    scanf("%d %d",&w,&h);
    for (int i = 0; i<h; ++i){
        gets(map[i]);
    }
    
    return 0;
}
