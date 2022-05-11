using System.Diagnostics;

int MaxProfit(int[] prices) {
    var maxProfit = 0;
    var buyPrice = int.MaxValue;
    for (var i = 0; i < prices.Length; i++)
    {
            buyPrice = buyPrice < prices[i] ? buyPrice : prices[i];
        if (maxProfit < prices[i] - buyPrice) {
            maxProfit = prices[i] - buyPrice;
        }
    }
    return maxProfit;
}

int SumOfLetters(string letters)
{
    letters = letters.ToUpper();
    var sum = 0;
    for (var i = 0; i < letters.Length; i++)
    {
        int letterAsNo = letters[i] - 65;
        sum += Fib(letterAsNo, new Dictionary<int, int>());
    }

    int Fib(int n, Dictionary<int, int> memo) 
    {
        if (memo.TryGetValue(n, out var val))
        {
            return val;
        }
        if (n < 1)
        {
            return 1;
        }
        memo[n] = Fib(n - 1, memo) + Fib(n - 2, memo);
        return memo[n];
    }
    return sum;
}

int CooKooSequence(int n)
{
    if (n == 1)
    {
        return 0;
    }
    if (n == 2)
    {
        return 1;
    }
    return CooKooSequence(n - 1) + 2 * CooKooSequence(n - 2) + 3;
}

int LCM(int a, int b) // LCM
{
    var lcm = (a * b) / GCD(a, b);
    return lcm;
}

int GCD(int a, int b) // HCF
{
    while (b != 0)
    {
        var tmp = a;
        a = b;
        b = tmp % b;
    }
    return a;
}