# Longest Substring Without Repeating Characters

## Problem Description
<p>Given a string <code>s</code>, find the length of the <strong>longest</strong> <span data-keyword="substring-nonempty"><strong>substring</strong></span> without repeating characters.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcabcbb&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;abc&quot;, with the length of 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bbbbb&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> The answer is &quot;b&quot;, with the length of 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;pwwkew&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;wke&quot;, with the length of 3.
Notice that the answer must be a substring, &quot;pwke&quot; is a subsequence and not a substring.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists of English letters, digits, symbols and spaces.</li>
</ul>

## Solution
```
class Solution(object):
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
        
```

## Optimized Solution
```
def length_of_longest_substring(s):
    # Dictionary to store the last positions of each character
    char_index = {}
    # Initialize the starting point of the current window and the maximum length
    start = 0
    max_length = 0

    # Loop through the string, character by character
    for i, char in enumerate(s):
        # If the character is already in the dictionary and its last occurrence is within the current window
        if char in char_index and char_index[char] >= start:
            # Move the start to the next position after the last occurrence of the current character
            start = char_index[char] + 1
        
        # Update the last occurrence of the character
        char_index[char] = i
        # Calculate the length of the current window and update max_length if necessary
        max_length = max(max_length, i - start + 1)

    return max_length
```
## What I Learned

1. I included `max_len` in my solution to allow the function to stop early if the maximum substring size is reached. However, I learned that converting the string to a set adds time complexity due to iterating through the entire string, effectively negating any benefit from early termination.

2. The optimized solution iterates through the string, keeping track of the most recent occurrence of each character. It calculates `max_length` by constantly updating the window size (the distance between the starting index and the current index). When a character is repeated, it updates the starting index to the next position after the last occurrence of that character. This method is more efficient than storing all window sizes and finding the maximum at the end.
