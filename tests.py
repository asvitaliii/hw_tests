import unittest
from models import *


class TestChildren(unittest.TestCase):
    def test_child_init(self):
        new_child = Child('Jora', 12)
        self.assertIsInstance(new_child, Child, "new_Child should be Child obj")

    def test_child_info(self):
        new_child = Child('Jora', 12)
        self.assertEqual(new_child.get_name(), 'Jora', 'Name should be Jora')
        self.assertEqual(new_child.get_age(), 12, 'Age should be 12')

    def test_child_set_age(self):
        new_child = Child('Jora', 12)
        new_child.set_age(31)
        self.assertEqual(new_child.get_age(), 31, 'Age should be changed to 31')


class TestParent(unittest.TestCase):
    def test_parent_init(self):
        new_parent = Parent('Kolia', 35, [])
        self.assertIsInstance(new_parent, Parent, "new_parent should be Parent obj")
        new_child = Child('Pasha', 1)
        new_parent2 = Parent('Jenia', 27, [new_child])
        self.assertIn(new_child, new_parent2.get_children(), 'New_parent should have child new_child')
        self.assertIsInstance(new_parent2.get_children()[0], Child, 'New_child should be Child obj')

    def test_children_info(self):
        new_parent = Parent('Kolia', 35, [])
        self.assertEqual(new_parent.get_name(), 'Kolia', 'Name should be Kolia')
        self.assertEqual(new_parent.get_age(), 35, 'Age should be 35')

    def test_children_set_age(self):
        new_parent = Parent('Kolia', 35, [])
        new_parent.set_age(49)
        self.assertEqual(new_parent.get_age(), 49, 'Age should be changed to 49')

    def test_parent_children_changing(self):
        new_parent = Parent('Kolia', 35, [])
        new_child = Child('Jora', 12)
        new_parent.add_children(new_child)
        self.assertIn(new_child, new_parent.get_children(), 'New_parent should have child new_children')
        new_parent.detdom(new_child)
        self.assertNotIn(new_child, new_parent.get_children(), 'New_child should go to detdom')


if __name__ == '__main__':
    unittest.main()
