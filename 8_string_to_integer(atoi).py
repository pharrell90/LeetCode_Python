''' Implement atoi to convert a string to an integer

 runtime: 76ms
'''

class Solution:

    def my_atoi(self, str):
        if len(str) == 0:
            return 0

        MAX_INT = 2147483647
        ptr = 0
        is_neg = False
        str = str.strip()
        if str[ptr] == '-':
            is_neg = True
            ptr += 1
        elif str[ptr] == '+':
            is_neg = False
            ptr += 1

        result = 0
        for ptr in range(ptr, len(str)):
            if not str[ptr].isdigit():
                break
            else:
                result *= 10
                result += int(str[ptr])

        if not is_neg and result > MAX_INT:
            return MAX_INT
        elif is_neg and result > MAX_INT + 1:
            return - (MAX_INT + 1)

        if is_neg:
            return -1 * result
        else:
            return result

if __name__ == '__main__':
    s = Solution()
    result = s.my_atoi('-2147483649')
    print(result)

