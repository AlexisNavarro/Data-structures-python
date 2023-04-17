class Node: 
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    ''''''
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

if __name__ == '__main__':
    main()