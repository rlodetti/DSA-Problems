# Longest Palindromic Substring

## Problem Description
<p>Given a string <code>s</code>, return <em>the longest</em> <span data-keyword="palindromic-string"><em>palindromic</em></span> <span data-keyword="substring-nonempty"><em>substring</em></span> in <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;babad&quot;
<strong>Output:</strong> &quot;bab&quot;
<strong>Explanation:</strong> &quot;aba&quot; is also a valid answer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cbbd&quot;
<strong>Output:</strong> &quot;bb&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consist of only digits and English letters.</li>
</ul>


## My Solution
```
def find_start(s, pointer):
    """
    Finds the starting and ending indices of the first potential palindrome substring.
    
    :param s: The input string.
    :param pointer: The current position in the string to start searching.
    :return: A tuple (start, end) if a potential palindrome is found, otherwise None.
    """
    substring = s[pointer:]
    for substring_start in range(len(substring)):
        # Check for consecutive identical characters
        if (substring_start + 1 < len(substring)) and (substring[substring_start] == substring[substring_start + 1]):
            end = substring_start + 1
            while end + 1 < len(substring) and substring[substring_start] == substring[end + 1]:
                end += 1
            return substring_start + pointer, end + pointer
        
        # Check for characters with one in between
        elif (substring_start + 2 < len(substring)) and (substring[substring_start] == substring[substring_start + 2]):
            return substring_start + pointer, substring_start + 2 + pointer

    return None  # Explicitly return None if no palindrome is found

def longestPalindrome(s):
    """
    Finds the longest palindromic substring in the input string.
    
    :param s: The input string.
    :return: The longest palindromic substring.
    """
    
    longest_string = s[0]
    longest_s_len = 1
    pointer = 0

    while pointer < len(s):
        # Find the starting and ending indices of the next potential palindrome
        result = find_start(s, pointer)
        if result is None:
            pointer += 1
            continue

        start, end = result
        pointer += 1  # Move pointer to the next character for the next iteration

        # Expand around the center to find the longest palindrome
        while (start - 1 >= 0) and (end + 1 < len(s)) and (s[start - 1] == s[end + 1]):
            start -= 1
            end += 1

        # Update the longest palindrome found
        if (end + 1 - start) > longest_s_len:
            longest_string = s[start:end + 1]
            longest_s_len = len(longest_string)

    return longest_string
```

## Optimal Solution 
```
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            left = i
            right = j

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left - 1

        ans = [0, 0]

        for i in range(len(s)):
            odd_length = expand(i, i)
            if odd_length > ans[1] - ans[0] + 1:
                dist = odd_length // 2
                ans = [i - dist, i + dist]

            even_length = expand(i, i + 1)
            if even_length > ans[1] - ans[0] + 1:
                dist = (even_length // 2) - 1
                ans = [i - dist, i + 1 + dist]

        i, j = ans
        return s[i : j + 1]
```

## What I Learned
