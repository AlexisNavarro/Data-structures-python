class Node: 
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data is not None:

            #if the data that we want to insert is less than the data in the current node then we shift to the left side of the binary tree
            if data < self.data:
                if self.left is None:
                    self.left = Node(data) #create a new node in the left side of the binary tree
                else:
                    self.left.insert(data) #if there is not an empty node in the left side then we use recursion 
            #if the data that we want to insert is greater than the data in the current node then we shift to the right side of the binary tree
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data) #create a new node in the right side of the binary tree
                else:
                    self.right.insert(data) #if there is not an empty node in the right side then we use recursion 
        else:
            self.data = data
    

    #method to traverse the left subtree then the root and then the right subtree
    def in_order_traversal(self, root):
        in_order = []

        if root is not None:
            in_order = self.in_order_traversal(root.left) #first traverse every left node and then append the value to the list
            in_order.append(root.data)
            in_order += self.in_order_traversal(root.right)#traverse every node on the right side and append it to the list
        return in_order
    

    #method to traverse the root, then the left subtree and then the right subtree
    def pre_order_traversal(self,root):
        pre_order = []

        if root is not None:
            pre_order.append(root.data) #append the root node
            pre_order += self.pre_order_traversal(root.left) #add every node value to the left side of the tree from top to bottom 
            pre_order += self.pre_order_traversal(root.right) #add every node value to the right side of the tree from top to bottom 
        return pre_order


    #method to traverse the left subtree, then the right subtree, then the root
    def post_order_traversal(self, root):
        post_order = []

        if root is not None:
            post_order = self.post_order_traversal(root.left) #traverse every left subtree node and add it to the list
            post_order += self.post_order_traversal(root.right)#traverse every right subtree node and add it to the list
            post_order.append(root.data)
        return post_order
    

    def print_binary_tree(self):
        if self.left:
            self.left.print_binary_tree()
        print(self.data)
        if self.right:
            self.right.print_binary_tree()
        
                    
def main ():
    print("creating a binary tree")

    root = Node(15) #top most value of the tree, will NOT have a parent node
    root.insert(10)
    root.insert(9)
    root.insert(11)
    root.insert(19)
    root.insert(18)
    root.insert(20)
    root.insert(21)
    root.print_binary_tree()

    print(root.in_order_traversal(root))
    print(root.pre_order_traversal(root))
    print(root.post_order_traversal(root))

if __name__ == '__main__':
    main()