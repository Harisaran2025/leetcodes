class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = set()  #set for storing result
        left = 0   #notes the first position
        max_len = 0

        for right in range(len(s)):      #for loop
            while s[right] in result:
                result.remove(s[left]) #it removes first element from result
                left = left + 1   #moves to next element
            result.add(s[right])  #adds element in result
            max_len =  max(max_len , right - left + 1)
        return max_len
        
        
