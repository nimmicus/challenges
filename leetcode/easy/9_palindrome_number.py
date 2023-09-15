class Solution:
    def isPalindrome(self, x: int) -> bool:
        magnitude_of_most_significant_digit = 0
        # Negative numbers are not considered Palindromes, so return False for negative numbers.
        if x < 0:
            return False
        # Need to be able to isolate the the most significant digit (leftmost) and least significant digit (rightmost) to compare for equality
        # the largest possible input is 2147483647 (i.e. 2^31 -1) which has a order of magnitude of 10^9. 

        for e in range(9,0,-1):
            left_most_digit = x // 10 ** e % 10
            if left_most_digit != 0:
                magnitude_of_most_significant_digit = e
                break

        # iterate from highest possible(9) magnitude down to 1
        while magnitude_of_most_significant_digit >= 0:

            # floor division to isolate the left most digit of x
            left_most_digit = x // 10 ** magnitude_of_most_significant_digit % 10

            # if the left_most_digit is not equal to the right_most_digit, then the x cannot be a palindrome. Return False.
            if (left_most_digit != x % 10):
                return False
                
            # Otherwise shift x to the right by dropping the least significant number
            x = x // 10
            magnitude_of_most_significant_digit -= 2

        return True