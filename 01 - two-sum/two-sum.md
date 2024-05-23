# Two Sum

## Problem Description
<p>Given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than <code>O(n<sup>2</sup>)</code><font face="monospace">&nbsp;</font>time complexity?

## Solution
```
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    result = 0

    sums = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result = [i, j]
            else:
                pass
    if result == 0:
        return "No combinations of numbers add up to target"
    else:
        return result
```


## Optimized Solution
```
def two_sum(nums, target):
    # Create a dictionary to store the difference between the target and each element.
    num_to_index = {}
    
    # Iterate through the list of numbers.
    for index, num in enumerate(nums):

    # Calculate the difference needed to reach the target.
    difference = target - num
    
    # Check if the difference is already in the dictionary.
    if difference in num_to_index:
        # If found, return the indices of the current number and the number that gives the difference.
        return [num_to_index[difference], index]
        
        # If not found, add the current number and its index to the dictionary.
        num_to_index[num] = index

    return []
```

## What I Learned
The optimized solution uses a hash map in the form of a Python dictionary for efficiency. Instead of looping through the list twice, resulting in a time complexity of \(O(n^2)\), this method only requires a single loop, reducing the time complexity to \(O(n)\). What I particularly liked about this solution was the use of the `difference` variable to collect and search for indices. This approach highlights the importance of understanding the relationships between different parts of a problem, reminding me that each binary operation has three interrelated components.

