def LetterComboOfPhoneNo(digits: str):
    phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    arr = []
    def AddToArr(i: int, curStr: str):
        if len(curStr) == len(digits):
            arr.append(curStr)
            return
        for c in phone[digits[i]]:
            AddToArr(i + 1, curStr + c)
    if digits != "":
        AddToArr(0, "")

    return arr

print(LetterComboOfPhoneNo("23"))
# print(LetterComboOfPhoneNo(""))
# print(LetterComboOfPhoneNo("2"))