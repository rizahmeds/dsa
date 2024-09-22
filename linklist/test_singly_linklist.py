import unittest

from singly_linklist import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList(4)

    def test_append(self):
        self.linked_list.append(5)
        self.linked_list.append(6)
        self.assertEqual(self.linked_list.tail.value, 6)
        self.assertEqual(self.linked_list.length, 3)
        self.assertEqual(self.linked_list.head.next.next.value, 6)

    def test_pop(self):
        self.linked_list.append(5)
        self.linked_list.append(6)
        self.linked_list.pop()
        self.assertEqual(self.linked_list.tail.value, 5)
        self.assertEqual(self.linked_list.length, 2)
        self.linked_list.pop()
        self.linked_list.pop()
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)
        self.assertEqual(self.linked_list.length, 0)

    def test_pop_empty(self):
        empty_list = LinkedList(0)
        empty_list.pop()
        empty_list.pop()
        self.assertIsNone(empty_list.head)
        self.assertIsNone(empty_list.tail)
        self.assertEqual(empty_list.length, 0)

    def test_prepend(self):
        self.linked_list.prepend(3)
        self.assertEqual(self.linked_list.head.value, 3)
        self.assertEqual(self.linked_list.head.next.value, 4)
        self.assertEqual(self.linked_list.length, 2)
        self.linked_list.prepend(2)
        self.assertEqual(self.linked_list.head.value, 2)
        self.assertEqual(self.linked_list.length, 3)

    def test_pop_first(self):
        self.linked_list.append(5)
        self.linked_list.append(6)
        self.linked_list.pop_first()
        self.assertEqual(self.linked_list.head.value, 5)
        self.assertEqual(self.linked_list.length, 2)
        self.linked_list.pop_first()
        self.linked_list.pop_first()
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)
        self.assertEqual(self.linked_list.length, 0)

    def test_pop_first_empty(self):
        empty_list = LinkedList(0)
        empty_list.pop_first()
        empty_list.pop_first()
        self.assertIsNone(empty_list.head)
        self.assertIsNone(empty_list.tail)
        self.assertEqual(empty_list.length, 0)
    
    def test_get_value(self):
        self.linked_list.append(5)
        self.linked_list.append(6)
        self.assertEqual(self.linked_list.get_value(0).value, 4)
        self.assertEqual(self.linked_list.get_value(2).value, 6)
        self.assertIsNone(self.linked_list.get_value(7), None)
    
    def test_set_value(self):
        self.linked_list.set_value(0, 5)
        self.assertEqual(self.linked_list.head.value, 5)
    
    def test_insert_value(self):
        self.linked_list.append(5)
        self.linked_list.append(6)
        self.linked_list.append(8)
        
        self.linked_list.insert_value(3, 7)
        self.assertEqual(self.linked_list.get_value(3).value, 7)

        self.linked_list.insert_value(0, 3)
        self.assertEqual(self.linked_list.get_value(0).value, 3)

    def test_reverse(self):
        self.linked_list.append(5)
        self.linked_list.append(6)
        self.linked_list.append(8)

        self.linked_list.reverse()
        self.assertEqual(self.linked_list.head.value, 8)
        self.assertEqual(self.linked_list.tail.value, 4)
        self.assertEqual(self.linked_list.head.next.value, 6)
        self.assertEqual(self.linked_list.get_value(1).value, 6)



if __name__ == '__main__':
    unittest.main()