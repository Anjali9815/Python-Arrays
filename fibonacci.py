a  = [1,2,3,4,5]

if len(a) >1 :
    sum = 0
    output = []
    for num in a:
        sum += num
        output.append(sum)
elif len(a) == 1:
    output = a[0]
print(output)
