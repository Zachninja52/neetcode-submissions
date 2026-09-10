class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 1
        for i in range(len(digits)):
            currVal = digits[-(i+1)]
            newVal = currVal + carry
            if newVal > 9:
                carry = 1
                digits[-(i+1)] = 0
            else:
                digits[-(i+1)] = newVal
                carry = 0
                break
        if carry != 0:
            return [1] + digits
        else:
            return digits