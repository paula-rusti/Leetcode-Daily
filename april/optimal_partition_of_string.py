# 4 aprilie 2023
"""
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique.
That is, no letter appears in a single substring more than once.
Return the minimum number of substrings in such a partition.
"""


class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        partitions = []
        current_partition = ""
        for char in s:
            if char not in current_partition:
                current_partition += char
            else:
                partitions.append(current_partition)
                current_partition = "" + char
        partitions.append(current_partition)
        return len(partitions)


if __name__ == "__main__":
    # s = "abacaba" => ("a", "ba", "cab", "a") and ("ab", "a", "ca", "ba") ==> 4
    sol = Solution()
    print(sol.partitionString("abacaba"))
