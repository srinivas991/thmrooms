#include<stdio.h>
#include<time.h>
#include <stdlib.h>

int main(void) {
    int t=time(0);
    srand(t);
    printf("%d",rand());
    return 0;
}

// ./exp | /srv/time-turner/swagger