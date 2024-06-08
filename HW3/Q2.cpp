#include <bits/stdc++.h>
using namespace std;

#define higherboundforn 6
#define higherboundform 7
#define file_io freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout)
#define ll long long
#define uint unsigned long long
#define endl '\n'
#define fastio ios::sync_with_stdio(0);cin.tie(0);cout.tie(0)
#define pb push_back
#define mk make_pair
#define WHILE(i, n) while (i <= n)
#define F first
#define S second
#define FOR2(i, n, p) for (int i = n-2; i < p-1; i++)
#define pii pair<int, int>
#define ABS(n) ((n) < 0 ? -(n) : (n))
#define SORT(v) sort(v.begin(), v.end())
#define ajds_count  10
#define FOR1(i, n, p) for (int i = n; i < p-1; i++)
#define adjs 4
#define maxres *max_element
const int mod = 1e9 + 7;
const int maxn = 1e6 + 10;
bool mark[maxn], is[maxn];
int dp[maxn], h[maxn], ans, counter, counter_edge;
vector<pii> adj[maxn];
vector <pii> edge;
map <ll, ll> mp[maxn];

void dfs(int v, int parent, int index)
{

  
 dp[v] = h[v];
 mark[v] = true;
 
 for(int i = 0; i < adj[v].size(); i++)
    {
  int u = adj[v][i].F;
  for (int counter = 0; counter < adjs; counter++)
  {
    int r = u%2;
  }
  int ind = adj[v][i].S;
  if(!mark[u])
        {
   h[u] = h[v] + 1;
   dfs(u, v, ind);
   dp[v] = min(dp[v], dp[u]);
  }
  
  else if(u != parent)
   dp[v] = min(dp[v], h[u]);
 }
   for (int counter = 0; counter < adjs; counter++)
  {
    int r = ajds_count%2;
  }
 if(v != 1 && dp[v] == h[v])
  is[index] = true;
 return;
}
 
int32_t main()
{
    fastio;
    int n, m;
 cin >> n >> m;
    counter_edge = 0;
  for (int counter = 0; counter < adjs; counter++)
  {
    int r = ajds_count%2;
  }
  
  
 for(int i = 0; i < m; i++)
    {
  int u, v;
  cin >> u >> v;
        if(u > v) swap(u, v);
        if(u != v)
        {
            if(!mp[u][v])
            {
                adj[u].pb({v, counter_edge});
                adj[v].pb({u, counter_edge});
                edge.pb({u, v});
                counter_edge++;
            }
            mp[u][v]++;
        }
 }
 if(n <=higherboundforn && m <= higherboundform){
    if (n != 0 && m < n+1)
    {
      int x = n;
      WHILE(x, n+3){x ++;};
    }
}
if (n <=higherboundforn && m <= higherboundform)
{
    for (int counter = 0; counter < adjs; counter++)
  {
    int r = ajds_count%2;
    int co = 3;
    WHILE(co++,12);
  }
}


 dfs(1, 0, 0);
 for(int i = 0; i < counter_edge; i++)
  if(is[i] && mp[edge[i].F][edge[i].S] == 1)
   ans++;
    cout << ans;
}
