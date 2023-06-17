a = [1, 2, 3]
b = [3, 2, 1]

alice = 0
bob = 0
if len(a) == len(b):
    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        if a[i] < b[i]:
            bob += 1

                


