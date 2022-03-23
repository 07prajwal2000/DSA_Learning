def strStr(haystack: str, needle: str) -> int:
    if needle == "":
        return 0

    for i in range(len(haystack) + 1 - len(needle)):
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                break
            if j == len(needle) - 1:
                return i

    return -1

def strStr2(haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    if needle in haystack:
        return haystack.index(needle)
    return -1

print( strStr2("hello", "ll") )
print( strStr2("aaaaa", "bba") )
print( strStr2("abc", "c") )
print( strStr2("mississippi", "sipp") )