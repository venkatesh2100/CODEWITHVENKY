#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

class Solution {
public:
    int countPaths(int n, vector<vector<int>>& roads) {
        vector<vector<pair<int,int>>> graph(n);

        for(const auto &road : roads) {
            int u = road[0], v = road[1], time = road[2];
            graph[u].emplace_back(v, time);
            graph[v].emplace_back(u, time);
        }

        vector<long long> dist(n, LLONG_MAX);
        vector<int> ways(n, 0);

        dist[0] = 0;
        ways[0] = 1;
        
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
        pq.emplace(0, 0);

        const int MOD = 1e9 + 7;
        
        while(!pq.empty()) {
            auto [d, node] = pq.top();
            pq.pop();

            if(d > dist[node]) continue;

            for(const auto &[nei, time] : graph[node]) {
                if(dist[node] + time < dist[nei]) {  // Fix: Use `<` instead of `>`
                    dist[nei] = dist[node] + time;
                    ways[nei] = ways[node];
                    pq.emplace(dist[nei], nei);
                } else if(dist[node] + time == dist[nei]) {
                    ways[nei] = (ways[nei] + ways[node]) % MOD;  // Fix: Use `%` instead of `&`
                }
            }
        }

        return ways[n-1];
    }
};
