def AddDigits(num: int):
    sum = 0
    while num != 0:
        q = num % 10
        sum += q
        num = (int)(num / 10 )
    if sum < 10:
        return sum
    return AddDigits(sum)

def AddDigitsOptimized(num: int):
    if num == 0:
        return 0
    elif num%9 == 0:
        return 9
    return num % 9

print(AddDigitsOptimized(38))
print(AddDigitsOptimized(0))

print(38 % 9)