# Python program to count leaf nodes in Binary Tree 

# A Binary tree node 
class Node: 
	
	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

# Function to get the count of leaf nodes in binary tree 
def getLeafCount(node): 
	if node is None: 
		return 0
	if(node.left is None and node.right is None): 
		return 1
	else: 
		return getLeafCount(node.left) + getLeafCount(node.right) 


# Driver program to test above function 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5)

print (f'Leaf count of the tree is {getLeafCount(root)}')
