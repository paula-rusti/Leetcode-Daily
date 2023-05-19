
# https://leetcode.com/problems/bulb-switcher/description/
def findDivisors(n):
    # List to store the count
    # of divisors
    div = [0 for i in range(n + 1)]

    # For every number from 1 to n
    for i in range(1, n + 1):

        # Increase divisors count for
        # every number divisible by i
        for j in range(1, n + 1):
            if j * i <= n:
                div[i * j] += 1
    return div[1:]


def find_odd_count(arr):
    even_count, odd_count = 0, 0
    for num in arr:
        if num ^ 1 == num + 1:
            even_count += 1
        else:
            odd_count += 1
    return odd_count


# Driver Code
if __name__ == "__main__":
    n = 3
    divs = findDivisors(n)
    print(divs)
    print(find_odd_count(divs))
    # TLE ON THE ABOVE APPROACH
    # SOLUTION IS TO TAKE THE SQUARE ROOT OF N

