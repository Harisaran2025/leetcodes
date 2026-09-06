class Solution:
    def isPalindrome(self, x: int) -> bool:  #create a funtion
        # Negative numbers are not palindromes
        if x < 0:   if #if given number is less than 0 return false
            return False
        original = x    #store x value in var
        reversed_num = 0   #temporary var
        while x > 0:  
            digit = x % 10
            reversed_num = reversed_num * 10 + digit  #reversed num * 10 + digit var
            x //= 10  
        return original == reversed_num
        
