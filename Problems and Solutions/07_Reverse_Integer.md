# Reverse Integer

## Problem Description
<p>Given a signed 32-bit integer <code>x</code>, return <code>x</code><em> with its digits reversed</em>. If reversing <code>x</code> causes the value to go outside the signed 32-bit integer range <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>, then return <code>0</code>.</p>

<p><strong>Assume the environment does not allow you to store 64-bit integers (signed or unsigned).</strong></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 123
<strong>Output:</strong> 321
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = -123
<strong>Output:</strong> -321
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> x = 120
<strong>Output:</strong> 21
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


## My Solution
```
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    sign = 1
    x_str = str(x)
     
    if x < 0:
        sign = -1
        x_str = x_str[1:]
    
    x_rev = x_str[::-1]
    
    x_int = int(x_rev)*sign
    if (x_int >= 2**31-1) or (x_int <= -2**31):
        return 0
    else:
        return x_int
```

## Optimal
```
```

## What I Learned
```
```