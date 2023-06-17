digit  = "2"

phone_dict = {'2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl', '6' : 'mno', '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz'}

if len(digit) > 1:
    print(len(digit))

if len(digit) == 1:
    print(phone_dict[digit])
