class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 1  #number of digits
        count = 9  #total count of one digit numbers
        start = 1  #where to start with

        while n > digit * count:  #if n is smaller than digit * count
            n -= digit * count   #removes the digit skipped
            digit += 1   #moves the next digit
            count *= 10  # update count
            start *= 10  #update start

        number = start + (n - 1) // digit
        index = (n - 1) % digit

        return int(str(number)[index])  #converts number into string and returns its index
        
