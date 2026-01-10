import heapq
from collections import defaultdict

class Solution:
        def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

            stops = [float('inf')] * n

            adj = defaultdict(list)

            for u, v, w in flights:
                adj[u].append((v,w))
            
            # distance, node, steps
            pq = [(0, src, 0)]

            while pq:
                distance, node, steps = heapq.heappop(pq)

                if steps > k + 1 or steps >= stops[node]:
                    continue
                
                stops[node] = steps
                
                if node == dst:
                    return distance
                
                for neighbour,price in adj[node]:
                    heapq.heappush(pq,(distance + price, neighbour, steps + 1))

      
            return -1





        