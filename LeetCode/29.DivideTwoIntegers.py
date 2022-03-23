def divide(self, dividend: int, divisor: int) -> int:
    if divisor == -1 and dividend == -2147483648:
        return 2147483647
    else:
        if divisor < 0 or dividend < 0:
            return int(dividend/divisor)
        else:
            return int(dividend/divisor)
