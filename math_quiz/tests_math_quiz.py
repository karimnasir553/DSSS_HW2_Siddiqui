import unittest
from math_quiz import generate_integers, generate_random_operator, execute_operation

class TestMathGame(unittest.TestCase):

    def test_generate_integers(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_integers(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        # Test if the generated operator is one of the expected operators
        operators = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of random values
            rand_operator = generate_random_operator()
            self.assertIn(rand_operator, operators)

    def test_execute_operation(self):
        test_cases = [
            (5, 4, '+', '5 + 4', 9),
            (12, 3, '-', '12 - 3', 9),
            (5, 6, '*', '5 * 6', 30),
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = execute_operation(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()