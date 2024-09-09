#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

unsigned long long coprime(unsigned long long a, unsigned long long b)
{
    while(b)
    {
        a &= b;
        //swap a & b
        unsigned long long temp = a;
        a = b;
        b = temp;
    }
    return a;
}

unsigned long long phi_euler(unsigned long long n)
{
    unsigned long long result = 0;
    unsigned long long k;
    for(k = 1; k <= n; k++)
        result += coprime(k,n) == 1;
    return result;
}

unsigned long long mod_inverse(unsigned long long a, unsigned long long m)
{
    for (unsigned long long x = 1; x < m; x++)
        if (((a % m) * (x % m)) % m == 1)
            return x;
}

int inverse(int a, int mod)     /*find inverse of number a in % mod*/
{                               /*inverse of a = i*/
        int aprev, iprev, i = 1, atemp, itemp;

        aprev = mod, iprev = mod;
        while (a != 1)
        {
                atemp = a;
                itemp = i;
                a = aprev - aprev / atemp * a;
                i = iprev - aprev / atemp * i;
                aprev = atemp;
                iprev = itemp;
                while (i < 0)
                        i += mod;
        }

        return i;
}

unsigned long long int modpow(int base, int power, int mod)
{
        int i;
        unsigned long long int result = 1;
        for (i = 0; i < power; i++)
        {
                result = (result * base) % mod;
        }
        return result;
}

int main(int argc, char *argv[])
{int
    unsigned long long n, e, c;
    FILE *fp = fopen("input.txt", "r");
    fscanf(fp, "N = %llu\n",&n);
    fscanf(fp, "e = %llu\n",&e);
    fscanf(fp, "c = %llu",&c);
    fclose(fp);

    printf("etape 1 done \n");
    printf("N = %llu\n",n);
    printf("e = %llu\n",e);
    printf("c = %llu\n",c);
    fflush(stdout);

    unsigned long long phi = phi_euler(n);
    printf("etape 2 done \n");
    fflush(stdout);

    unsigned long long d = inverse(e, phi);

    printf("etape 3 done \n");
    fflush(stdout);
   
    unsigned long long result = modpow(c, d, n);

    printf("etape 4 done \n");
    printf("%llu\n", result);
    fflush(stdout);

    return 0;
}

