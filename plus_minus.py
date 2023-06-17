def plusMinus(arr):
    # Write your code here
    prop0 = 0
    prop1 = 0
    prop_1 = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            prop0 += 1
        if arr[i] > 0:
            prop1 += 1
        if arr[i] < 0:
            prop_1 +=1
    return prop1/len(arr), prop_1/len(arr), prop0/len(arr)

arr = [-4, 3, -9, 0, 4, 1]
print(plusMinus(arr))