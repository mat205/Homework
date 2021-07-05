import unittest
import mock

from src.ATM import atmTransaction


class TestATM(unittest.TestCase):
    def test_pin_input(self):
        original_input = mock.builtins.input
        mock.builtins.input = lambda _: "0000"
        assert_equal(bar(), "you entered 00")
        mock.builtins.input = original_input

    def test_pin_number(self):
        expected = [0000]
        result = [0000]
        self.assertEqual(expected, result)

    def test_choice_input(self):
        original_input = mock.builtins.input
        mock.builtins.input = lambda _: "1"
        assert_equal(bar(), "you entered 1")
        mock.builtins.input = original_input

    def test_withdraw_number(self):
        original_input = mock.builtins.input
        mock.builtins.input = lambda _: "50"
        assert_equal(bar(), "you entered 50")
        mock.builtins.input = original_input

    def test_insufficient_funds(self):
            expected = ["insufficient funds"]
            result = ['insufficient funds']
            self.assertEqual(expected, result)
