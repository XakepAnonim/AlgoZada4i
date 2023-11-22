from main import positive_or_negative, even_num, count, sum_list, sum_numbers
import pytest
import unittest
import random


@pytest.mark.parametrize('x, exp_res', [(25, 'positive'),
                                        (25.6, 'positive'),
                                        (0.000000001, 'positive'),
                                        (-25, 'negative'),
                                        (-25.6, 'negative'),
                                        (-0.000000001, 'negative'),
                                        (0, 'zero')])
def test_pon(x, exp_res):
    assert positive_or_negative(x) == exp_res


@pytest.mark.parametrize('number, exp_res', [(4, True),
                                             (5, False),
                                             (0, True),
                                             (-2, True),
                                             (-3, False)])
def test_even(number, exp_res):
    assert even_num(number) == exp_res


@pytest.mark.parametrize('num, exp_res', [(123, 3),
                                          (0, 1),
                                          (-987654321, 9),
                                          (1000000000, 10)])
def test_count(num, exp_res):
    assert count(num) == exp_res


@pytest.mark.parametrize("lst, exp_res", [([1, 2, 3, 4, 5], 15),
                                          ([0, 0, 0, 0, 0], 0),
                                          ([-1, 1, -2, 2], 0),
                                          ([], 0)])
def test_sum_list(lst, exp_res):
    assert sum_list(lst) == exp_res


@pytest.mark.parametrize('numbers, exp_res', [('12, 34, 56', 102),
                                              ('1, 2, 3, 4, 5', 15),
                                              ('10, 20, 30, 40, 50', 150),
                                              ('', 0)])  # тут ошибку выдает
def test_sum_numbers(numbers, exp_res):
    assert sum_numbers(numbers) == exp_res


# ==============================================================================


class TestTasks(unittest.TestCase):

    def test_1(self):
        date = '2025-12-31'
        expected_result = ('31', '12', '2025')
        result = tuple(date.split('-')[::-1])
        self.assertEqual(result, expected_result)

    def test_2(self):
        numbers = ['1', '2', '3', '4', '5']
        expected_result = 15
        result = sum(map(int, numbers))
        self.assertEqual(result, expected_result)

    def test_3(self):
        numbers = [1, 2, 3, 4, 5, 6]
        first_half_sum = sum(numbers[:len(numbers) // 2])
        second_half_sum = sum(numbers[len(numbers) // 2:])
        expected_result = first_half_sum / second_half_sum
        result = first_half_sum / second_half_sum
        self.assertEqual(result, expected_result)

    def test_4(self):
        dct1 = {
            'a': 1,
            'b': 2,
        }
        dct2 = {
            'c': 3,
            'd': 4,
        }
        expected_result = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
        }
        result = {**dct1, **dct2}
        self.assertEqual(result, expected_result)

    def test_5(self):
        dct = {
            1: {
                1: 11,
                2: 12,
                3: 13,
            },
            2: {
                1: 21,
                2: 22,
                3: 23,
            },
            3: {
                1: 24,
                2: 25,
                3: 26,
            },
        }
        expected_result = sum(sum(subdict.values()) for subdict in dct.values())
        result = sum(sum(subdict.values()) for subdict in dct.values())
        self.assertEqual(result, expected_result)

    def test_6(self):
        def get_min_max(numbers):
            return {
                'min': min(numbers),
                'max': max(numbers)
            }

        numbers = [1, 2, 3, 4, 5, 9]
        expected_result = {'min': 1, 'max': 9}
        result = get_min_max(numbers)
        self.assertEqual(result, expected_result)

    def test_7(self):
        def get_divisors(numbers):
            result = []
            for num in numbers:
                divisors = []
                for i in range(1, num + 1):
                    if num % i == 0:
                        divisors.append(i)
                result.append(divisors)
            return result

        numbers = [1, 2, 3, 4, 5, 6]
        expected_result = [[1], [1, 2], [1, 3], [1, 2, 4], [1, 5], [1, 2, 3, 6]]
        result = get_divisors(numbers)
        self.assertEqual(result, expected_result)

    def test_8(self):
        pass

    def test_9(self):
        def random_color(colors):
            return random.choice(colors)

        colors = ['red', 'blue', 'green', 'yellow', 'orange']
        result = random_color(colors)
        self.assertIn(result, colors)

    def test_10(self):
        pass

    def test_11(self):
        def shuffle_list(lst):
            random.shuffle(lst)
            return lst

        lst = [1, 2, 3, 4, 5]
        result = shuffle_list(lst)
        self.assertEqual(len(result), len(lst))
        self.assertNotEqual(result, sorted(lst))

    if __name__ == '__main__':
        unittest.main()