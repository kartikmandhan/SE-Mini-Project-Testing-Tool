
class Node():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree():
    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        return self.root

    def iterative_insert(self, item):
        if self.root is None:
            self.root = Node(item)
        else:
            nd = self.root
            while nd is not None:
                if item < nd.data:
                    if nd.left is None:
                        nd.left = Node(item)
                        return
                    else:
                        nd = nd.left
                elif item > nd.data:
                    if nd.right is None:
                        nd.right = Node(item)
                        return
                    else:
                        nd = nd.right
                else:
                    raise ValueError("Duplicate Entry in Binary Search Tree")

    def search(self, node, item):
        if node is None:
            return False
        else:
            if node.data == item:
                return True
            elif node.data < item:
                return self.search(node.right, item)
            else:
                return self.search(node.left, item)

    def size(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.size(node.left) + self.size(node.right)

    def depth(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.depth(node.left), self.depth(node.right))

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)

    def get_min(self, node):
        if self.root is None:
            return "Tree is empty."
        else:
            if node.left is None:
                return node.data
            else:
                return self.get_min(node.left)

    def get_max(self, node):
        if self.root is None:
            return "Tree is empty."
        else:
            if node.right is None:
                return node.data
            else:
                return self.get_max(node.right)

    def getLeafCount(self, node):
        if node is None:
            return 0
        if(node.left is None and node.right is None):
            return 1
        else:
            return self.getLeafCount(node.left) + self.getLeafCount(node.right)

    def isFullTree(self, node):

        if self.root is None:
            return True

        if node.left is None and node.right is None:
            return True

        if node.left is not None and node.right is not None:
            return (self.isFullTree(node.left) and self.isFullTree(node.right))

        return False

    def findADepth(self, node):
        d = 0
        while (node != None):
            d += 1
            node = node.left
        return d

    def isPerfectRec(self, node, d, level=0):

        if (self.root == None):
            return True

        if (node.left == None and node.right == None):
            return (d == level + 1)

        if (node.left == None or node.right == None):
            return False

        return (self.isPerfectRec(node.left, d, level + 1) and
                self.isPerfectRec(node.right, d, level + 1))

    def isPerfect(self, node):
        d = self.findADepth(node)
        return self.isPerfectRec(node, d)

    def BreadthFirstSearch(self):
        if self.root is None:
            return
        result = ""
        queue = []
        queue.append(self.root)
        while(len(queue) > 0):
            result += str(queue[0].data)+" "
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return result
