class Solution:
    import random
    def __init__(self, w: List[int]):
        
        self.w = w

    def pickIndex(self) -> int:

        return random.choices(range(len(self.w)), self.w)[0]