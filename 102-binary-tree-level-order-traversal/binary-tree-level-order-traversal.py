# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root == None):
            return []
        q = deque([root])
        ans=[]
        while(len(q)>0):
            level = []
            for rashmitha in range(len(q)):
                node = q.popleft()
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
                level.append(node.val)
            ans.append(level)
        return ans