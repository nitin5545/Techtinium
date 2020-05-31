import unittest
import main
class Test(unittest.TestCase):
    def test(self):
        answer = {'OUTPUT': [{'region': 'New York', 'total_cost': 11000, 'machines': [('8XLarge', 1), ('2XLarge', 1), ('XLarge', 1), ('Large', 1)]}, {'region': 'India', 'total_cost': 10665, 'machines': [('8XLarge', 1), ('2XLarge', 1), ('Large', 3)]}, {'region': 'China', 'total_cost': 9450, 'machines': [('8XLarge', 1), ('XLarge', 3), ('Large', 1)]}]}

        predicted = main.calculateCost(230, 5)

        self.assertEquals(answer, predicted)


if __name__ == '__main__':
    unittest.main()
