class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        import math
        import heapq as hq
        
        dict1 = {}
        for i in flights:
            if i[0] not in dict1:
                dict1[i[0]] = [[i[1],i[2]]]              
            else:
                dict1[i[0]].append([i[1],i[2]])
                
                
        #print(dict1)
        q = [(0, src, K+1)]
        dist = [math.inf]*n
        count = 0
        while q:
            #print(q, dist)
            path_len, node, k = hq.heappop(q)
            if  node == dst:
                return path_len
            if k > 0 and node in dict1:
                for i in dict1[node]:
                    dist[i[0]] =  path_len+i[1]
                    hq.heappush(q,(dist[i[0]],i[0],k-1))


        return -1         