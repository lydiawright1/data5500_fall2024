'''
This code provides programming activities to implement a binary search tree

The file bst_complete.py contains the solutions to the tasks in this file
Please try them yourself before you just look at the answers.


Complete the tasks from top to bottom, then you will be able to uncomment
the code snippets in the main function below

'''


import random
import time
# Python program to demonstrate delete operation
# in binary search tree

from print_tree import * # print_tree.py contains a print pretty version of a bst

# A Binary Tree Node

class Node:

	# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# A utility function to insert a
# new node with given key in BST
def insert(node, key):

	# If the tree is empty, return a new node
	if node is None:
		return Node(key)

	# Otherwise recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)

	# return the (unchanged) node pointer
	return node
	
	
# Task 1. Write a function to find the minimum value in the tree
def findMin(node):
	while node.left != None:
		node = node.left
	return node
    

# Task 2. Write a recursive findMinRec function
def findMinRec(node):
    if node.left == None:
        return node
	
    return findMinRec(node.left)
    
# Task 3. Write a findMaxRecursive
def findMaxRec(node):
    pass

# print tree inorder
def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.key, end=" ")
		inorder(root.right)
 
# Task 4. Write a pre-order print


# Task 5. Write a post-order print

		
# Task 6. write a findKey recursive function


# This function deletes the key and returns the new root
def deleteNode(root, key):

	# Base Case
	if root is None:
		return root

	# If the key to be deleted 
	# is smaller than the root's
	# key then it lies in left subtree
	if key < root.key:
		root.left = deleteNode(root.left, key)

	# If the kye to be delete 
	# is greater than the root's key
	# then it lies in right subtree
	elif(key > root.key):
		root.right = deleteNode(root.right, key)

	# If key is same as root's key, then this is the node
	# to be deleted
	else:

		# Node with only one child or no child
		if root.left is None:
			temp = root.right
			root = None
			return temp

		elif root.right is None:
			temp = root.left
			root = None
			return temp

		# Node with two children: 
		# Get the inorder successor
		# (smallest in the right subtree)
		temp = findMin(root.right)

		# Copy the inorder successor's 
		# content to this node
		root.key = temp.key

		# Delete the inorder successor
		root.right = deleteNode(root.right, temp.key)

	return root





def main():
    # creating a Tree with root variable "root"
    root = None
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)
    root = insert(root, 19)
    root = insert(root, 18)
    root = insert(root, 17)
    root = insert(root, 16)
    root = insert(root, 15)

    print(findMin(root).key)
    print(findMinRec(root).key)
    # finding values in the tree
    # print(findKey(root, 80))
    # print(findKey(root, 10))
    
    # traversing the tree
    print("Inorder traversal of the given tree")
    inorder(root)
    # PrintTree(root)
    
    ##########################################################
    # Uncomment deleteNode calls after findMin is complete Task 1
    
    # # deleting 
    # print("\nDelete 20")
    # root = deleteNode(root, 20)
    # print("Inorder traversal of the modified tree")
    # inorder(root)
    
    # print("\nDelete 30")
    # root = deleteNode(root, 30)
    # print("Inorder traversal of the modified tree")
    # inorder(root)
    
    # print("\nDelete 50")
    # root = deleteNode(root, 50)
    # print("Inorder traversal of the modified tree")
    # inorder(root)
    #########
    
    print()
    display(root)
    
    
    tree2 = None
    tree2 = insert(tree2, 3)
    tree2 = insert(tree2, 1)
    tree2 = insert(tree2, 4)
    tree2 = insert(tree2, 2)
    tree2 = insert(tree2, 5)
    tree2 = insert(tree2, 9)
    
    inorder(tree2)
    print()
    display(tree2)
    
    
    ###########################################################
    # Uncomment after preorder and postorder have are complete, Task 4 and Task 5
    # inorder(tree2)
    # print()
    # preorder(tree2)
    # print()
    # postorder(tree2)
    #########
    
    
    
    ############################################################
    # Uncomment after findMin is complete Task 1
    
    # print("\nmin value: ", findMin(tree2).key)
    # print("\nmin value recursive: ", findMinRec(tree2).key)
   
    ######################################################
    ######################################################
    ######################################################
    # The following example shows 10000 searches in a bst are 100 times faster than a list
    # While this may seem to good to be true, notice it takes much longer to build the
    # tree than the list.  They are trade offs.
    
    # create a list of 10000 numbers
    # lst = [random.randint(1,10000) for i in range(1000000)]
    # # each number is a random number between 1 and 10000 random.randint(1,10000)
    
    # # in other loop for in 1 to 10000, check to see if i is in the list
    # start1 = time.time()
    # for i in range(1,10001):
    #     for l in lst:
    #         if i == l:
    #             break
    # end1 = time.time()
    # print("search time list (sec): ", end1-start1)
    
    
    
    # root = None
    # for i in range(1000000):
    #     root = insert(root, random.randint(1,10000))
        
    
    # start = time.time()
    # for i in range(10000):
    #     findKey(root, i)
    # end = time.time()
    
    # print("search time tree (sec): ",end-start)
    
    # print("---------------------")
    #########
    
    
main()