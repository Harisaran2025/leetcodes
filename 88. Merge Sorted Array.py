class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1  #m-- num1
        j = n - 1  #n-- num2
        k = m + n - 1   #available values of num1 and num2 -1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:   # if num1 is greater than num2 then it is stored in num1[k]
                nums1[k] = nums1[i]
                i -= 1  #removes numbers that moved
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
