# Median of Two Sorted Arrays

## Problem Description
<p>Given two sorted arrays <code>nums1</code> and <code>nums2</code> of size <code>m</code> and <code>n</code> respectively, return <strong>the median</strong> of the two sorted arrays.</p>

<p>The overall run time complexity should be <code>O(log (m+n))</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,3], nums2 = [2]
<strong>Output:</strong> 2.00000
<strong>Explanation:</strong> merged array = [1,2,3] and median is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2], nums2 = [3,4]
<strong>Output:</strong> 2.50000
<strong>Explanation:</strong> merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>nums1.length == m</code></li>
	<li><code>nums2.length == n</code></li>
	<li><code>0 &lt;= m &lt;= 1000</code></li>
	<li><code>0 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= m + n &lt;= 2000</code></li>
	<li><code>-10<sup>6</sup> &lt;= nums1[i], nums2[i] &lt;= 10<sup>6</sup></code></li>
</ul>

## My Solution
```
def stop_idx_finder(nums1, nums2):
    num_elements = len(nums1) + len(nums2)
    stop_idx = num_elements // 2
    parity = 'odd' if num_elements % 2 else 'even'
    return stop_idx, parity, len(nums1), len(nums2)

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        stop_idx, parity, len_1, len_2 = stop_idx_finder(nums1, nums2)
        pointer_1, pointer_2 = 0, 0
        comb_list = []

        while len(comb_list) <= stop_idx:
            if pointer_1 < len_1 and (pointer_2 >= len_2 or nums1[pointer_1] <= nums2[pointer_2]):
                comb_list.append(nums1[pointer_1])
                pointer_1 += 1
            else:
                comb_list.append(nums2[pointer_2])
                pointer_2 += 1

        if parity == 'even':
            median = (comb_list[-1] + comb_list[-2]) / 2.0
        else:
            median = comb_list[-1]
        
        return median     
```

## Optimized Solution
```
def findMedianSortedArrays(self, nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1  # Ensure nums1 is the smaller array

    m, n = len(nums1), len(nums2)
    imin, imax, half_len = 0, m, (m + n + 1) // 2

    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i

        if i < m and nums1[i] < nums2[j - 1]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and nums1[i - 1] > nums2[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect
            if i == 0: max_of_left = nums2[j - 1]
            elif j == 0: max_of_left = nums1[i - 1]
            else: max_of_left = max(nums1[i - 1], nums2[j - 1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m: min_of_right = nums2[j]
            elif j == n: min_of_right = nums1[i]
            else: min_of_right = min(nums1[i], nums2[j])

            return (max_of_left + min_of_right) / 2.0

```
## What I Learned
Well, at the moment I'm learning that I want to learn more about binary searches. I'll do some reading and report back. 