#include <stdio.h>
#include <stdlib.h>

double runge(double x)
{
    return 1.0 / (1.0 + 25.0 * x * x);
}

int main()
{
    double x[] = {
                   2.0 * 0.0 / 15.0 - 1.0,
                   2.0 * 3.0 / 15.0 - 1.0,
                   2.0 * 4.0 / 15.0 - 1.0, 
                   2.0 * 6.0 / 15.0 - 1.0,
                   2.0 * 7.0 / 15.0 - 1.0
                 };

    for(int i = 0; i < sizeof(x) / sizeof(x[0]); i++)
        printf("%6.3f %6.3f\n", x[i], runge(x[i]));
}