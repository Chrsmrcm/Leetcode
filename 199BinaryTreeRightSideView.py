'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values 
of the nodes you can see ordered from top to bottom.

This one was a little difficult as I tried initially to solve it recursively. The use of a queue proved
to be necessary.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #breadth first search from left
    #use a dequeu object to keep track of the nodes in the left
    #move from left to right, overrighting a rightmost node tracker
    #final overwrite of the level will be the rightmost node

    answer = []
    queue = deque()
    queue.append(root)

    #while there are items in the queue
    while queue:
        #assume we do not have a rightmost
        rightmost = False
        #for each item in the queue
        for i in range(len(queue)):
            current = queue.popleft()

            if current:
                #we now have an assumed rightmost
                rightmost = current
                #queue the current node's children
                queue.append(current.left)
                queue.append(current.right)
                
        #on exit of the for, we will have the rightmost node of the level
        if rightmost:
            answer.append(rightmost.val)

    return answer