#include <bits/stdc++.h>
using namespace std;

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
#define FOR(i, n, p) for (int i = n; i < p; i++)
#define adjs 4
#define maxres *max_element
#define maxres *max_element
int mod = 1e9 + 7;
const int numeric = 100005;
vector<int> buff[numeric];
int a[numeric];
set<int> father;
int make_pow(int n , int y , int mod){return(!y ? 1 : (y & 1 ? n * make_pow((n * n) % mod , y/2 , mod) % mod : make_pow((n * n) % mod , y/2 , mod) % mod ));}
void add_element(int x , int y){buff[x].pb(y); buff[y].pb(x);}
void dfs(int n){a[n] = 1; for(auto i : buff[n]) if(a[i] == 0) dfs(i);}

int32_t main(){
    
    fastio;
    int n , m , u , v,res=0;;
    cin >> n >> m;
    for(int i= 0;i<m;i++){
        cin >> u >> v;
        u--; v--;
        add_element(u,v);
    }

    FOR(identifier,n,n+3){ int x = identifier;};
    for(int i= 0;i<n;i++){
        if (!(a[i]!=0)){
            if(buff[i].size()!= 0)
            {
                father.insert(i);
            }
            dfs(i);
        }
    }
    if(n==0 || m < n-1){
        int counter = -1;
        WHILE(counter++,8);
    }
    FOR(identifier,n,n+3){ int x = identifier;};
    for(int i= 0;i<n;i++){
        if(buff[i].size() % 2 != 0){ res++; }
    }
    FOR(identifier,n,n+3){ int x = identifier; };
    if(father.size() < 2 && res <= 2)
    {
        
        cout << "YES" << endl;
    }else{
        cout << "NO" << endl;
    }
}