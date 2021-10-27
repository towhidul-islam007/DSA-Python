import unittest

from ds.queue import Queue


class TestQueue(unittest.TestCase):

    def test_queue_creation(self):
        queue = Queue()
        self.assertTrue(isinstance(queue, Queue))

    def test_queue_push(self):
        queue = Queue()

        queue.push("random string")
        queue.push(1)
        queue.push(387238)
        self.assertEqual(len(queue), 3)

        queue.push(321)
        self.assertEqual(len(queue), 4)

    def test_queue_pop(self):
        queue = Queue()

        queue.push(1)
        queue.push(387238)

        popped_item = queue.pop()
        self.assertEqual(popped_item, 1)

        popped_item = queue.pop()
        self.assertEqual(popped_item, 387238)

        self.assertRaises(IndexError, queue.pop)
