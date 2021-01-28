/*
ID: junehah1
TASK: transform
LANG: C++
*/
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int N;
    cin >> N;
    char original[10][10]={};
    char transform[10][10]={};
    for (int i=0; i<N; i++)
    {
        for (int j=0; j<N; j++)
        {
            cin >> original[i][j];
        }
    }
    for (int i=0; i<N; i++)
    {
        for (int j=0; j<N; j++)
        {
            cin >> transform[i][j];
        }
    }
    // check 90°
    for (int i=0; i<N; i++)
    {
        for (int j=0; j<N; j++)
        {
            if (original[i][j]==transform[j][N-1-i])
            {
                
            }
        }
    }
    // check 180°
    // check 270°
    // check reflection
    // check combination
    // no change
    // not possible
}