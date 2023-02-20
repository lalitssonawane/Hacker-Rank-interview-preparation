#For the purposes of this challenge, we define a binary search tree to be a binary tree with the following properties:

def checkBST(root):
    def is_BST(root):
        if root == None:
            return True, None, None
        bool_left, min_left, max_left = is_BST(root.left)
        bool_right, min_right, max_right = is_BST(root.right)
        if bool_left and bool_right:
            if root.left==None and root.right==None:
                return True, root.data, root.data
            elif root.left==None and not root.right==None:
                if min_right>root.data:
                    return True, root.data, root.right
            elif not root.left==None and root.right==None:
                if max_left.data<root.data:
                    return True, min_left, root.data
            elif not root.left==None and not root.right==None:
                if max_left<root.data and min_right>root.data:
                    return True, min_left, max_right
        return False, None, None
    result, _, _ = is_BST(root)
    return result