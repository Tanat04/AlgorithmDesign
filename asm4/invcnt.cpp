#include <iostream>
using namespace std;

typedef long long siz;

long long countinv = 0;

void count_invertion_merge_it(long long lis1[], long long lis2[], long long lis[], siz n1, siz n2)
{
    siz p = 0, q = 0, r = 0, counter = 0;
    while (p < n1 && q < n2)
    {
        if (lis1[p] <= lis2[q])
        {
            countinv += counter;
            lis[r++] = lis1[p++];
        }
        else
        {
            counter++;
            lis[r++] = lis2[q++];
        }
    }
    while (p < n1)
    {
        countinv += counter;
        lis[r++] = lis1[p++];
    }
    while (q < n2)
    {
        lis[r++] = lis2[q++];
    }
}

void merge_sort(long long lis[], siz n)
{
    if (n > 1)
    {
        siz pos = n / 2;
        siz k = 0;
        long long lis1[pos], lis2[n - pos];
        for (siz i = 0; i < pos; ++i)
        {
            lis1[i] = lis[k++];
        }
        for (siz i = 0; i < n - pos; ++i)
        {
            lis2[i] = lis[k++];
        }
        merge_sort(lis1, pos);
        merge_sort(lis2, n - pos);
        count_invertion_merge_it(lis1, lis2, lis, pos, n - pos);
    }
}

int main()
{
    siz n, t;
    cin >> t;
    while (t--)
    {
        cin >> n;
        countinv = 0;
        long long Ar[n];
        for (siz i = 0; i < n; ++i)
        {
            cin >> Ar[i];
        }
        merge_sort(Ar, n);
        cout << countinv << endl;
    }
    return 0;
}
