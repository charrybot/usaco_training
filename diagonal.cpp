#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int arr[1005][1005]={};
    int N; 
    cin >> N;
    for (int i=1; i<=N; i++)
    {
        for (int j=1; j<=N; j++)
        {
            cin >> arr[i][j];
        }
    }
    int sumA=0, sumB=0;
    for (int i=1; i<=N; i++) 
    {
        sumA+=arr[i][i];
    }
    for (int i=N; i>=1; i--) 
    {
        sumB+=arr[N-i+1][i];
    }
    cout << abs(sumA-sumB);
}
