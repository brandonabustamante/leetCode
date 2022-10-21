


def lengthOfLongestSubstring(s):
    
    if s == "":
        return 0

    start = 0 

    end = 0 

    cur_max_length = 0

    unique_chars = set()

    while end < len(s):
        if s[end] not in unique_chars:
            unique_chars.add(s[end])
            end += 1
            cur_max_length = max(cur_max_length, len(unique_chars))
        else:
            unique_chars.remove(s[start])
            start += 1
    
    return cur_max_length


s = "abcabcbb"

print(lengthOfLongestSubstring(s))