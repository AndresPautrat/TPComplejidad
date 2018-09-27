// C++ program to solve Traveling Salesman Problem
// using Branch and Bound.
#include <bits/stdc++.h>
//#include "CPS_MA_150.cpp"
#include "sstream"
#include "fstream"
using namespace std;
const int N = 4;
 
int final_path[N+1];
 
bool visited[N];
 
float final_res = FLT_MAX;
 
void copyToFinal(int curr_path[])
{
    for (int i=0; i<N; i++)
        final_path[i] = curr_path[i];
    final_path[N] = curr_path[0];
} 
float firstMin(float adj[N][N], int i)
{
    float min = FLT_MAX;
    for (int k=0; k<N; k++)
        if (adj[i][k]<min && i != k)
            min = adj[i][k];
    return min;
}
 
float secondMin(float adj[N][N], int i)
{
    float first = FLT_MAX, second = FLT_MAX;
    for (int j=0; j<N; j++)
    {
        if (i == j)
            continue;
 
        if (adj[i][j] <= first)
        {
            second = first;
            first = adj[i][j];
        }
        else if (adj[i][j] <= second &&
                 adj[i][j] != first)
            second = adj[i][j];
    }
    return second;
}

void TSPRec(float adj[N][N], float curr_bound, float curr_weight,
            int level, int curr_path[])
{
    if (level==N)
    {
        if (adj[curr_path[level-1]][curr_path[0]] != 0)
        {
            
            float curr_res = curr_weight +
                    adj[curr_path[level-1]][curr_path[0]];
            if (curr_res < final_res)
            {
                copyToFinal(curr_path);
                final_res = curr_res;
            }
        }
        return;
    }
 
    for (int i=0; i<N; i++)
    {
        if (adj[curr_path[level-1]][i] != 0 &&
            visited[i] == false)
        {
            float temp = curr_bound;
            curr_weight += adj[curr_path[level-1]][i];
 
            if (level==1)
              curr_bound -= ((firstMin(adj, curr_path[level-1]) +
                             firstMin(adj, i))/2);
            else
              curr_bound -= ((secondMin(adj, curr_path[level-1]) +
                             firstMin(adj, i))/2);
 
            if (curr_bound + curr_weight < final_res)
            {
                curr_path[level] = i;
                visited[i] = true;
 
                TSPRec(adj, curr_bound, curr_weight, level+1,
                       curr_path);
            }
 
            curr_weight -= adj[curr_path[level-1]][i];
            curr_bound = temp;
 
            memset(visited, false, sizeof(visited));
            for (int j=0; j<=level-1; j++)
                visited[curr_path[j]] = true;
        }
    }
}
 
void TSP(float adj[N][N])
{
	int curr_path[N+1];
    float curr_bound = 0;
    memset(curr_path, -1, sizeof(curr_path));
    memset(visited, 0, sizeof(curr_path));
 
    // Compute initial bound
    for (int i=0; i<N; i++)
        curr_bound += (firstMin(adj, i) +
                       secondMin(adj, i));
 
    curr_bound/=2;
    
    visited[0] = true;
    curr_path[0] = 0;

    TSPRec(adj, curr_bound, 0, 1, curr_path);
}

// Driver code
int main()
{

    float adj[N][N] = { {0, 10, 15, 20},
        {10, 0, 35, 25},
        {15, 35, 0, 30},
        {20, 25, 30, 0},
    };
 	
    TSP(adj);
    ofstream file;
    file.open("Ruta3.txt",ios::out);
 	ostringstream oss;
 	oss<<setprecision(5);
    printf("Minimum cost : %f\n", final_res);
    printf("Path Taken : ");
    int ruta[N];
    int c=0;
    for (int i=1; i<=N; i++){
    	ruta[c]=final_path[i];
    	c=final_path[i];
        printf("%d ", final_path[i]);
    }
    for(int i=0;i<sizeof(ruta);i++){
    	oss<<ruta[i]<<"\n";
	}
    file<<oss.str();
    file.close();
 	
    return 0;
}
