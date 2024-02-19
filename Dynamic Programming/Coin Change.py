class Solution(object):
    def bruteForce(self, coins, amount):
        
        self.res = []
        self.min = float('inf')
        def BackTracking(index, total, ls):
            
            if total == 0:
                self.res.append(ls[::])
            
            if total < 0:
                return
            
            
            for i in range(index, len(coins)):
                
                ls.append(coins[i])
                res = BackTracking(i, total - coins[i], ls)
                ls.pop()
        
        BackTracking(0, amount, [])
        
        for item in self.res:
            self.min = min(self.min, len(item))
        
        return self.min if self.min != float('inf') else 0
    
    
    def coinChange(self, coins, amount):
        
        res = [float('inf')] * (amount + 1)
        res[0] = 0
        
        for i in range(1, len(res)):
            for coin in coins:
                if i - coin >= 0:
                    res[i] = min(res[i], res[i - coin] + 1)
        
        print(res)
        return res[amount] if res[amount] != float('inf') else -1
        
s = Solution()
s.bruteForce(coins = [1,2,5], amount = 6)
print(s.coinChange(coins = [1,2,5], amount = 11))
print(s.coinChange(coins = [2], amount = 3))
print(s.coinChange(coins = [1], amount = 0))
