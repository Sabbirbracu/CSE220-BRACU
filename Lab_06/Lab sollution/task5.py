import sys
sys.setrecursionlimit(10000)

class FinalQ:
    def print(self, array, idx):
        if idx < len(array):
            profit = self.calcProfit(array[idx])
            print(f"{idx + 1}. Investment: {array[idx]}; Profit: {profit}")
            self.print(array, idx + 1)

    def calcProfit(self, investment):
        setup_cost = 25000

        if investment <= 100000:
            return (investment - setup_cost) * 0.045
        else:
            profit = 75000 * 0.045
            remaining_investment = investment - 100000
            profit += remaining_investment * 0.08
            return profit

# Tester
array = [25000, 100000, 250000, 350000]
f = FinalQ()
f.print(array, 0)
