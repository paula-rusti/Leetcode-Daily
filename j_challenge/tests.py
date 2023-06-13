import unittest

from j_challenge.solution import min_spanning_subnet, parse_addresses_to_matrix


class TestLongestCommonPrefix(unittest.TestCase):

    def test_longest_common_prefix(self):
        ip_set = [
            '192.168.0.1',
            '192.168.0.10',
            '192.168.0.100',
            '192.168.1.1',
        ]
        parsed = parse_addresses_to_matrix(ip_set)
        self.assertEqual(min_spanning_subnet(parsed), '192.168')

        ip_set = [
            '10.0.0.1',
            '10.0.0.2',
            '10.0.0.3',
            '10.0.0.4',
        ]
        parsed = parse_addresses_to_matrix(ip_set)
        self.assertEqual(min_spanning_subnet(parsed), '10.0.0')


        ip_set = [
            '123.456.789',
            '987.654.321',
            '789.123.456',
        ]
        parsed = parse_addresses_to_matrix(ip_set)
        self.assertEqual(min_spanning_subnet(parsed), '')


if __name__ == '__main__':
    unittest.main()
