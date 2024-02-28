# 1208. Get Equal Substrings Within Budget

def equalSubstring(s: str, t: str, maxCost: int) -> int:

    left = cost = ans = 0
    
    for right in range(len(s)):
        cost += abs(ord(s[right]) - ord(t[right]))
        print("\ncost:", cost)

        while cost > maxCost:
            print("while chala bhai")
            cost -= abs(ord(s[left]) - ord(t[left]))
            
            left += 1

        print("right - left + 1:", right - left + 1)
        ans = max(ans, right - left + 1)

    return ans


print(equalSubstring("abcd", "acde", 0))