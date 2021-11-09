
import unittest

from bst import Node, BinarySearchTree


class BstTest(unittest.TestCase):
    # setup is the code called before running every test case
    def setUp(self):
        # print("Setup")
        self.tree = BinarySearchTree()
        self.arr = [100, 20, 500, 30, 10, 40]

        for x in self.arr:
            self.tree.iterative_insert(x)

    def test_search(self):
        self.assertTrue(self.tree.search(self.tree.get_root(), 30))
        self.assertFalse(self.tree.search(self.tree.get_root(), 12312))

    def test_size(self):
        self.assertEqual(self.tree.size(self.tree.get_root()), 6)

    def test_depth(self):
        self.assertEqual(self.tree.depth(self.tree.get_root()), 4)

    def test_min(self):
        self.assertEqual(self.tree.get_min(self.tree.get_root()), 10)

    def test_max(self):
        self.assertEqual(self.tree.get_max(self.tree.get_root()), 500)

    def test_display(self):
        print("Inorder Traversal: ")
        self.tree.inorder(self.tree.get_root())
        print("Preorder Traversal: ")
        self.tree.preorder(self.tree.get_root())
        print("Postorder Traversal: ")
        self.tree.postorder(self.tree.get_root())


if __name__ == '__main__':
    unittest.main()
