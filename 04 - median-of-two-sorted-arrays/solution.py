def stop_idx_finder(nums1, nums2):
    num_elements = len(nums1) + len(nums2)
    stop_idx = num_elements // 2
    parity = 'odd' if num_elements % 2 else 'even'
    return stop_idx, parity, len(nums1), len(nums2)

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
       