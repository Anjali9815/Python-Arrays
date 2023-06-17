def longestCommonPrefix(strs):
    s = ""

    for i, j in enumerate(strs):
        s = j[i]
        print(j)
    print(s)
a = ["flower","flow","flight"]
longestCommonPrefix(a)