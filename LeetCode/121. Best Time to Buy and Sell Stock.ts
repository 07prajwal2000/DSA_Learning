function BestTimetoBuyandStock(prices: number[]): number {
    let maxProfit = 0;
    let buyPrice = Number.MAX_VALUE;

    for (let i = 0; i < prices.length; i++) {
        buyPrice = buyPrice < prices[i] ? buyPrice : prices[i];
        if (maxProfit < prices[i] - buyPrice) {
            maxProfit = prices[i] - buyPrice;
        }
    }
    return maxProfit;
}

console.log(BestTimetoBuyandStock([7, 1, 5, 3, 6, 4]));
console.log(BestTimetoBuyandStock([7,6,4,3,1]));
