import unittest

from ds.stack import Stack


class TestStack(unittest.TestCase):

    def test_stack_creation(self):
        stack = Stack()
        self.assertTrue(isinstance(stack, Stack))

    def test_stack_push(self):
        stack = Stack()

        stack.push("random string")
        stack.push(1)
        stack.push(387238)
        self.assertEqual(len(stack), 3)

        stack.push(321)
        self.assertEqual(len(stack), 4)

    def test_stack_pop(self):
        stack = Stack()

        stack.push(1)
        stack.push(387238)

        popped_item = stack.pop()
        self.assertEqual(popped_item, 387238)

        popped_item = stack.pop()
        self.assertEqual(popped_item, 1)

        self.assertRaises(IndexError, stack.pop)
