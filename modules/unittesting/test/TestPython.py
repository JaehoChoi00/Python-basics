import unittest

class InspectionChecklist(unittest.TestCase):

    def setUp(self):
        self.state = "Initial State"

    def test_passing_assertion(self):
        self.assertEqual(self.state, "Initial State")

    def test_expected_error_trap(self):
        with self.assertRaises(ZeroDivisionError):
            _ = 1 / 0

if __name__ == '__main__':
    unittest.main()
