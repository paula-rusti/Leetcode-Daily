import copy
import operator
from functools import reduce
from typing import List


def longest_common_prefix(addresses: List[str]) -> str:
    # straitforward solution which compares each byte of each address to find the longest common prefix
    # time complexity: O(n*m) where n is the number of addresses and m is the number of bytes in each address
    # we can do much better
    addr_bytes: List[str] = addresses[0].split('.')  # first address bytes
    prefix: List[str] = []

    for i in range(len(addr_bytes)):
        if all(address.split('.')[i] == addr_bytes[i] for address in addresses):
            prefix.append(addr_bytes[i])
        else:
            break

    return '.'.join(prefix)


def parse_addresses_to_matrix(addresses):
    matrix = []

    # Split the addresses into bytes and populate the matrix
    for ip in addresses:
        bytes = [int(x) for x in ip.split('.')]
        matrix.append(bytes)

    # Transpose the matrix to have bytes from each address in separate columns
    transposed_matrix = list(map(list, zip(*matrix)))

    return transposed_matrix


def min_spanning_subnet(matrix):
    # O(n) time complexity
    copied_matrix = copy.deepcopy(matrix)
    prefix = []
    reduced_column = [reduce(operator.xor, column) for column in matrix]
    for index, num in enumerate(reduced_column):
        if num == 0:
            prefix.append(copied_matrix[index][0])
    print(reduced_column)
    return '.'.join(str(num) for num in prefix)


ip_set = [
    '192.168.0.1',
    '192.168.0.10',
    '192.168.0.100',
    '192.168.1.1',
]

# print(parse_addresses_to_matrix(ip_set))
print(min_spanning_subnet(parse_addresses_to_matrix(ip_set)))

prefix = longest_common_prefix(ip_set)
print(f"Longest common prefix: {prefix}")
