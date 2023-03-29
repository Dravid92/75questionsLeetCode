def maxProfit(prices):
	lowest_buy = prices[0]
	max_sell = 0
	for i in range(len(prices)):
            if prices[i] < lowest_buy:
                lowest_buy = prices[i]
            elif i > 0:
                current_sell = prices[i] - lowest_buy
                if current_sell > max_sell:
                    max_sell = current_sell
        if max_sell <= 0:
            return 0
        else:
            return max_sell

prices = [7,1,5,3,6,4]
output = 5

maxProfit(prices)

