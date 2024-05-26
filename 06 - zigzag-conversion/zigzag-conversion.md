# Zigzag Conversion

## Problem Description
<p>The string <code>&quot;PAYPALISHIRING&quot;</code> is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)</p>

<pre>
P   A   H   N
A P L S I I G
Y   I   R
</pre>

<p>And then read line by line: <code>&quot;PAHNAPLSIIGYIR&quot;</code></p>

<p>Write the code that will take a string and make this conversion given a number of rows:</p>

<pre>
string convert(string s, int numRows);
</pre>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;PAYPALISHIRING&quot;, numRows = 3
<strong>Output:</strong> &quot;PAHNAPLSIIGYIR&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;PAYPALISHIRING&quot;, numRows = 4
<strong>Output:</strong> &quot;PINALSIGYAHRPI&quot;
<strong>Explanation:</strong>
P     I    N
A   L S  I G
Y A   H R
P     I
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;A&quot;, numRows = 1
<strong>Output:</strong> &quot;A&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists of English letters (lower-case and upper-case), <code>&#39;,&#39;</code> and <code>&#39;.&#39;</code>.</li>
	<li><code>1 &lt;= numRows &lt;= 1000</code></li>
</ul>


## My Solution
```
def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    # If there is only one row, just return the original string
    if numRows == 1 or numRows >= len(s):
        return s
    
    # Steps between elements in top row
    cycle_len = 2 * numRows - 2
    
    # Create a list of strings for each row
    rows = [''] * numRows
    
    for i, char in enumerate(s):
        mod_idx = i % cycle_len

        # Building the vertical row
        if mod_idx < numRows:
            rows[mod_idx] += char
        
        # Building the zig back up
        else:
            rows[cycle_len - mod_idx] += char
    
    # Concatenate all rows to get the final result
    return ''.join(rows)
```

## Optimized Solution
```
```

## What I Learned
