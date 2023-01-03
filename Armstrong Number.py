def isArmstrong(n: int) -> bool:
    str_n = str(n)
    digit_sum = 0
    for i in str_n:
        digit_sum += int(i) ** len(str_n)
    return digit_sum == n

n = 123
print(f"Output: {isArmstrong(n)}")