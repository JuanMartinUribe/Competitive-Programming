class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(set)

        for city_a,city_b in roads:
            road = (city_a,city_b) if city_a<city_b else (city_b,city_a)
            graph[city_a].add(road)
            graph[city_b].add(road)
        ans = 0
        for city_a in range(n):
            for city_b in range(city_a+1,n):
                roads = len(graph[city_a]|graph[city_b])
                ans = max(ans,roads)
        return ans