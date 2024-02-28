    

def reverseOnlyLetters(s: str) -> str:
    s = list(s)
    left = 0
    right = len(s) - 1

    # print(s)
    while left < right:
        print("\nleft:", left)
        print("right:", right)
        if not s[left].isalpha():
            left += 1
            continue

        elif not s[right].isalpha():
            right -= 1
            continue
    
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return "".join(s)

        
# print(reverseOnlyLetters("ab-cd"))
# print(reverseOnlyLetters("a-bC-dEf-ghIj"))
print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))

        