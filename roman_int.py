def romanToInt(s):
    
    dict1 = {'I' : 1, 'L' : 50, 'X' : 10, 'V' : 5, 'C' : 100, 'D' : 500, 'M' : 1000}
    number = 0
    skip = None
    for temp in range(0, len(s)):
        if skip == temp:
            continue
        else:
            print(number)
            first = dict1[s[temp]]
            if (temp+1) < len(s):
                if first < dict1[s[temp + 1]]:
                    number = number + dict1[s[temp + 1]] - first
                    skip = temp + 1
                else:
                    number += first
            else:
                number += first
        
    print(number)

s = "MCMXCIV" # 1000+900+90+4
romanToInt(s)