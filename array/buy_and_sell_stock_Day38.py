def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        max_profit=0
        for price in prices:
            profit=price-min_price
            if price<min_price:
                min_price=price
            elif profit>max_profit:
                max_profit=profit
        return max_profit
        