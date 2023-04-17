#Purpose of this binary tree implementation is to show my profienciency in creating and using a binary tree
#NO IMPORTS WILL BE USED IN THIS IMPLEMENTATION

#creating an object node to be used in the binary tree
class Node: 
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    #Method to insert a node into a binary tree
    #TIME COMPLEXITY  O(log n)
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
    
    #method to search for a specific node in the binary tree
    def search_node(self, root, value):

        #made a try and except, exception occurs when the value is not found.
        try:
            if root is None or root.data == value:
                return "found the value" , root.data
        except AttributeError as E:
                return "value was not found", E
       
        if value > root.data: #traverse to the right subtree if the value is greater than the current node data
           return self.search_node(root.right, value)
        if value < root.data: #traverse to the left subtree if the value is less than the current node data
            return self.search_node(root.left, value)
       

    #method to find the smallest value in the binary tree
    def find_min(self, root):
        if root.left is None:
            return root.data
        return self.find_min(root.left)
    

    #method to find the largest value in the binary tree
    def find_max(self, root):
        if root.right is None:
            return root.data
        return self.find_max(root.right)

    #method to calculate the total sum of the entire tree
    def calculate_sum(self, root):
        sum = 0

        if root is not None:
            sum=root.data
            sum+=self.calculate_sum(root.left)
            sum+=self.calculate_sum(root.right)
        return sum
    

    #method to print the binary tree
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
    
    print("printing tree!!!!")
    print("-------------------")
    root.print_binary_tree()
    print("-------------------")

    print("In order traversal: ",root.in_order_traversal(root))
    print("Pre order traversal:  ",root.pre_order_traversal(root))
    print("Post order traversal: ",root.post_order_traversal(root))

    print(root.search_node(root, 20))
    print("minimum value in the tree is: ", root.find_min(root))
    print("maximum value in the tree is: ",root.find_max(root))

    print("sum of all nodes is: ", root.calculate_sum(root))

if __name__ == '__main__':
    main()