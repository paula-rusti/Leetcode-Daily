import random

# 30 Martie 2023
def generate_string(input_string, n):
    if n == 0:
        return ""
    if n == 1:
        return input_string
    for i in range(2, n + 1):
        s1 = input_string[0:i - 1]
        s2 = input_string[i - 1:n]
        generated1 = generate_string(s1, len(s1))
        generated2 = generate_string(s2, len(s2))
        bool_var = bool(random.getrandbits(1))
        if bool_var:
            result = generated1 + generated2
        else:
            result = generated2 + generated1
        return result

# O(n^4) (memoization) ==> O(n^3)
def is_scrambled(s1, s2, sol_dict):
    if len(s1) != len(s2):
        return False

    n = len(s1)  # strings are equal

    if not sorted(s1) == sorted(s2):    # if they are not ngrams return false
        return False

    key = s1 + "/" + s2
    if s1 == s2:
        sol_dict[key] = True
        return True

    if key in sol_dict:
        return sol_dict[key]

    for i in range(1, n):  # given that len(s1) == len(s2) == n ==> we can partition s1 in n-1 strings
        # check for 4 conditions which are [(true(left, left) and true(left, left)) or (true(left, left') and true(right, right'))]
        # but optimize by early returning true without going for 2 more recursive calls

        # without swap between left and right
        cond1_result = is_scrambled(s1[:i], s2[:i], sol_dict)
        cond2_result = is_scrambled(s1[i:], s2[i:], sol_dict)

        if cond1_result and cond2_result:
            sol_dict[key] = True
            return True

        #  with swap between left and right
        cond3_result = is_scrambled(s1[:i], s2[n - i:], sol_dict)  # s1[:i], s2[n-i:]
        cond4_result = is_scrambled(s1[i:], s2[:n - i], sol_dict)  # s1[i:], s2[:n-i]

        if cond3_result and cond4_result:
            sol_dict[key] = True
            return True

    sol_dict[key] = False
    return False

# for storing already solved problems


if __name__ == '__main__':
    # generated = generate_string("abc", 3)
    # print(generated)
    sol_dict = {}
    res = is_scrambled("great", "rgeat", sol_dict)
    print(res)

