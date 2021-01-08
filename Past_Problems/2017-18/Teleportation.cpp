#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main()
{
    ofstream fout ("teleport.out");
    ifstream fin ("teleport.in");
    int a, b, x, y;
    fin >> a >> b >> x >> y;
    if (((abs(x-a)+abs(y-b)) or (abs(y-a)+abs(x-b)))<=abs(a-b))  // if AX +YB or AY +BX <= AB --> use teleport 
    {
        if ((abs(x-a)+abs(y-b)) < (abs(y-a)+abs(x-b)))
        {
            fout << abs(x-a)+abs(y-b) << endl;
        }
        else
        {
            fout << abs(y-a)+abs(x-b) << endl;
        }
    }
    else
    {
        fout << abs(a-b) << endl;
    }
    return 0;
}

/*teleportation
# include <cstdio>
# include <cmath>

int main()
{
    int a, b, t1, t2, p1, p2, t; // p1 = use teleport
    scanf("%d %d %d %d", &a, &b, &t1, &t2);
    if (t1>t2)
    {
        t=t2;
        t2=t1;
        t1=t;
    }
    if (a>b)
    {
        p1=abs(t1-b) + abs(t2-a);
        p2=a-b;
    }
    else 
    {
        p1=abs(t1-a) + abs(t2-b);
        p2=b-a;
    }
    if (p1>p2)
    {
        printf("%d", p2);
    }
    else
    {
        printf("%d", p1);
    }
}
*/
