# Python program to count full 
# nodes in a Binary Tree 
class newNode(): 

	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
		
		
# Function to get the count of 
# full Nodes in a binary tree 
def getfullCount(root): 
  
    if (root == None): 
        return -1
      
    if (root.left == None and root.right == None): 
        return 0
    else:
        return  1 + (getfullCount(root.left) + getfullCount(root.right))


# def BST_size(root):
#     if root is None:
#         return -1
#     if root is not None:
#         count = 1
#         if root.left is not None:
#             return count += BST_size(root.left)
#         if root.right is not None:
#             return count += BST_size(root.right)
		
# Driver code 
if __name__ == '__main__': 
	""" 2 
	/ \ 
	7 5 
	\ \ 
	6 9 
	/ \ / 
	1 11 4 
	Let us create Binary Tree as shown 
	"""
	
	root = newNode(2) 
	root.left = newNode(7) 
	root.right = newNode(5) 
	root.left.right = newNode(6) 
	root.left.right.left = newNode(1) 
	root.left.right.right = newNode(11) 
	root.right.right = newNode(9) 
	root.right.right.left = newNode(4) 
	root.right.right.right = newNode(14) 
	
	print(getfullCount(root)) 

# This code is contributed by SHUBHAMSINGH10 
