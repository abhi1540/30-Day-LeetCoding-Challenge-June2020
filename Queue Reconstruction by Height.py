class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        people1 = sorted(people, key=lambda x: (-x[0], x[1]))
        #print(people1)
        res = []
        for i in range(len(people1)):
            res.insert(people1[i][1], people1[i])
            #print(res) 
        return res