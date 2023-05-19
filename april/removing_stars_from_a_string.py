# 11 Aprilie 2023
"""
https://leetcode.com/problems/removing-stars-from-a-string/
"""
class Solution:
    def find_substring_length(self, start_index, str):
        # returns the ending index of the substring formed out of only letters starting at start_index
        index = start_index
        end_index = start_index
        while index < len(str):
            if str[index] != '*':
                end_index += 1
            else:   # break at first non-star char
                break
            index += 1
        return end_index-1

    def removeStars(self, s: str) -> str:
        reversed_str = "".join(reversed(s))
        temp = ''
        index = 0
        add_char = True
        stars = 0
        while index < len(reversed_str):
            inc = False
            if reversed_str[index] != '*' and add_char:
                temp += reversed_str[index]

            if reversed_str[index] == '*':
                add_char = False
                stars += 1
            else:           # reversed_str[index] != *
                if not add_char:
                    poss_end_index = self.find_substring_length(index, reversed_str)
                    substr_len = poss_end_index - index + 1
                    if substr_len < stars:
                        stars -= substr_len
                        index = poss_end_index + 1
                    else:
                        index += stars
                        stars = 0

                    inc = True
                    if stars == 0:
                        add_char = True

            if not inc:
                index += 1

        return temp[::-1]


if __name__ == '__main__':
    # leet**cod*e ==> lecoe
    s = "leet**cod*e"
    s2 = "erase*****"
    s3 = "abb*cdfg*****x*"
    sol = Solution()
    print(sol.removeStars(s))

    # print(sol.find_substring_length(6, s))
