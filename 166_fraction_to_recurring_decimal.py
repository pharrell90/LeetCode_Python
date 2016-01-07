'''
 Given two integers representing the numerator and denominator of a fraction,
 return the fraction in string format.

 If the fractional part is repeating, enclose the repeating part
 in parentheses.

 For example,

 Given numerator = 1, denominator = 2, return "0.5".
 Given numerator = 2, denominator = 1, return "2".
 Given numerator = 2, denominator = 3, return "0.(6)".
 runtime: 40ms
'''

class Solution:

    def fraction_to_decimal(self, numerator, denominator):
        self.num_list = []
        self.loop_dict = {}
        self.loop_str = None
        neg_flag = numerator * denominator < 0
        count = 0
        numerator = abs(numerator)
        denominator = abs(denominator)

        while True:
            self.num_list.append(str(numerator // denominator))
            count += 1
            numerator = 10 * (numerator % denominator)
            if numerator == 0:
                break
            loc = self.loop_dict.get(numerator)
            if loc:
                self.loop_str = ''.join(self.num_list[loc:count])
                break
            self.loop_dict[numerator] = count

        result = self.num_list[0]
        if len(self.num_list) > 1:
            result += '.'

        if self.loop_str:
            result += ''.join(self.num_list[1:len(self.num_list)- \
                    (len(self.loop_str))]) + '(' + self.loop_str + ')'
        else:
            result += ''.join(self.num_list[1:])

        if neg_flag:
            result = '-' + result

        return result

if __name__ == '__main__':
    s = Solution()
    result = s.fraction_to_decimal(19, 7)
    print(result)
