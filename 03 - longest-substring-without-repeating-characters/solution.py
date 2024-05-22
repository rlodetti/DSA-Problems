def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    current_list = []
    max_len = len(set(s))
    longest_str_len = 0
    for i in s:
        if i in current_list:
            char_idx = current_list.index(i)
            current_list = current_list[char_idx+1:]
        current_list.append(i)
        string_len = len(current_list)
        longest_str_len = max(longest_str_len,string_len)
        if longest_str_len == max_len:
            return longest_str_len
    return longest_str_len