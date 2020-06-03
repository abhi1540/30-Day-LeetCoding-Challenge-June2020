class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        difflist = []
        res = 0
        for i in range(len(costs)):
            difflist.append([costs[i][0] - costs[i][1], i])
        
        count = 0
        for i in sorted(difflist, key=lambda x: x[0]):
            if count < len(costs)//2:
                res += costs[i[1]][0]
            else:
                res += costs[i[1]][1]
            count += 1
            
        
        return res 