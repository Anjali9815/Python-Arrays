# class Solution:
def reverse(x):
    if x!= 0 and x > 2**31 and x < -2**31:
        if x > 0:
            s = str(x)
            t = s[::-1]
        else:
            s = str(x)
            t = s[1:]
            t = "-" + t[::-1]
    else:
        t = x
    return int(t)

x = 1534236469
print((2 ** 31) - 1)
quit()
print(reverse(x))